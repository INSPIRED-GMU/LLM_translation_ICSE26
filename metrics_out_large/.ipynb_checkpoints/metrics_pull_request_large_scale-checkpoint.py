#!/usr/bin/env python3
"""
metrics_from_log.py - IMPROVED VERSION
  Read a 'crawl log' text file and emit:
    adoption.csv     (#merged / total translation PRs per repo)
    survival.csv     (improved maintenance gap analysis)
"""

import os, re, subprocess, time, datetime as dt, pathlib, argparse, requests
import pandas as pd
from dateutil import parser as dp
from tqdm import tqdm



REPO_DIR = pathlib.Path("repos")           # where shallow clones go
OUT_DIR  = pathlib.Path("metrics_out_new"); OUT_DIR.mkdir(exist_ok=True)
WINDOW   = 180            # days for survival / maintenance-gap

# ─────────────── parse crawl log (UNCHANGED) ──────────────
REPO_RE = re.compile(r"repo '([^']+)'")
PR_RE   = re.compile(r"-\s+(.*?)\s+\((https://github\.com/[^)]+)\)")

def parse_log(path):
    rows, repo = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        m_repo = REPO_RE.search(line)
        if m_repo: repo = m_repo.group(1); continue
        m_pr   = PR_RE.search(line)
        if m_pr and repo:
            title,url = m_pr.groups()
            rows.append(dict(repo=repo,
                             pr_number=int(url.rstrip('/').split('/')[-1]),
                             pr_title=title, pr_url=url))
    return pd.DataFrame(rows)

# ─────────────── GitHub helpers (UNCHANGED) ──────────────
def gh_get(url):
    r = requests.get(url, headers=GH); r.raise_for_status(); return r.json()

def enrich(df: pd.DataFrame) -> pd.DataFrame:
    """Fetch state / timestamps for every URL that really is a PR."""
    meta_rows = []
    for r in tqdm(df.itertuples(), desc="PR metadata"):
        url = f"https://api.github.com/repos/{r.repo}/pulls/{r.pr_number}"
        try:
            j = gh_get(url)
        except requests.HTTPError as e:
            if e.response is not None and e.response.status_code in (404, 410):
                continue
            raise

        meta_rows.append({
            "repo":      r.repo,
            "pr_number": r.pr_number,
            "merged":    bool(j["merged_at"]),
            "state":     j["state"],
            "created":   dp.parse(j["created_at"]),
            "merged_at": dp.parse(j["merged_at"]) if j["merged_at"] else pd.NaT,
            "base_sha":  j["base"]["sha"],
        })

    meta_df = pd.DataFrame(meta_rows)
    return df.merge(meta_df, on=["repo", "pr_number"], how="inner")

# ─────────────── git helpers (UNCHANGED) ──────────────
def clone(repo_full: str) -> pathlib.Path:
    name = repo_full.split("/")[-1]
    p = REPO_DIR / name
    if p.exists():
        return p

    url = f"https://github.com/{repo_full}.git"
    subprocess.run([
        "git", "clone",
        "--filter=blob:none",
        "--depth", "100",
        "--single-branch",
        "--no-checkout",
        url, str(p)
    ], check=True, stdout=subprocess.DEVNULL)

    return p

def commits(p, file, revspec=None, since=None, until=None):
    """Improved commit counting with better error handling"""
    cmd=["git","-C",str(p),"log","--oneline"]
    if revspec: cmd.append(revspec)
    if since  : cmd.append(f"--after={since}")
    if until  : cmd.append(f"--until={until}")
    cmd+=["--",file]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            return 0
        return len(result.stdout.splitlines()) if result.stdout.strip() else 0
    except subprocess.TimeoutExpired:
        return 0

# ─────────────── metrics — adoption (UNCHANGED) ──────────────
def adoption(df):
    g=(df.groupby("repo").agg(merged=("merged","sum"),
                              closed=("merged",lambda x:(~x).sum()))
          .reset_index())
    g["adoption_rate"]=g["merged"]/(g["merged"]+g["closed"])
    g.to_csv(OUT_DIR/"adoption.csv", index=False)
    return g

# ─────────────── IMPROVED FILE DETECTION ──────────────
def improved_file_detection(files):
    """Better detection of README files and their languages"""
    readme_files = []
    
    for f in files:
        filename = f["filename"]
        
        # Match various README patterns
        readme_patterns = [
            (r'README\.md$', 'en'),                           # English README.md
            (r'README\.([a-z]{2})\.md$', 'lang'),            # README.es.md
            (r'README\.([a-z]{2}-[A-Z]{2})\.md$', 'lang'),   # README.zh-CN.md
            (r'README-([a-z]{2})\.md$', 'lang'),             # README-es.md
            (r'README_([a-z]{2})\.md$', 'lang'),             # README_es.md
            (r'readme\.([a-z]{2})\.md$', 'lang'),            # lowercase variants
            (r'README\.([a-z]+)\.md$', 'lang'),              # README.spanish.md
            # Non-.md files (your original logic)
            (r'README[^/]*\.(?!md$)', 'non_md'),             # Any README not .md
        ]
        
        for pattern, lang_type in readme_patterns:
            match = re.search(pattern, filename, re.I)
            if match:
                if lang_type == 'en':
                    lang = 'en'
                elif lang_type == 'lang':
                    lang = match.group(1)
                elif lang_type == 'non_md':
                    # Try to extract language from filename
                    lang_match = re.search(r'README[._-]?([a-z]{2}(?:-[A-Z]{2})?)', filename, re.I)
                    lang = lang_match.group(1).lower() if lang_match else 'unknown'
                
                readme_files.append({
                    'filename': filename,
                    'language': lang,
                    'is_primary': lang == 'en'
                })
                break
    
    return readme_files

def get_file_last_modified(repo_dir, filepath, since_date, until_date):
    """Get the last modification date of a file within a date range"""
    cmd = ["git", "-C", str(repo_dir), "log", "-1", "--format=%ci",
           f"--after={since_date}", f"--until={until_date}", "--", filepath]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.stdout.strip():
            return dp.parse(result.stdout.strip())
    except (subprocess.TimeoutExpired, Exception):
        pass
    return None

# ─────────────── IMPROVED SURVIVAL ANALYSIS ──────────────
def survival(df):
    """Improved survival analysis – drops rows whose health is 'unknown'."""
    results = []

    for r in tqdm(df.itertuples(), desc="Improved survival gap"):
        # ── 1. PR not merged → keep (still useful for adoption stats)
        if not r.merged:
            results.append({
                'repo': r.repo, 'pr_number': r.pr_number,
                'maint_gap': None, 'maintenance_health': 'not_merged',
                'primary_commits': 0, 'translation_commits': 0,
                'time_gap_days': None, 'files_detected': 0
            })
            continue

        try:
            repo_dir   = clone(r.repo)
            since_date = r.merged_at.isoformat()
            until_date = (r.merged_at + dt.timedelta(days=WINDOW)).isoformat()

            files        = gh_get(f"https://api.github.com/repos/{r.repo}/pulls/{r.pr_number}/files")
            readme_files = improved_file_detection(files)

            # ── 2. No README-like files detected → keep but flag
            if not readme_files:
                results.append({
                    'repo': r.repo, 'pr_number': r.pr_number,
                    'maint_gap': None, 'maintenance_health': 'no_readme_files',
                    'primary_commits': 0, 'translation_commits': 0,
                    'time_gap_days': None, 'files_detected': 0
                })
                continue

            primary_files      = [f for f in readme_files if f['is_primary']]
            translation_files  = [f for f in readme_files if not f['is_primary']]

            primary_commits     = sum(commits(repo_dir, f['filename'],
                                              since=since_date, until=until_date)
                                      for f in primary_files)

            translation_commits = sum(commits(repo_dir, f['filename'],
                                              since=since_date, until=until_date)
                                      for f in translation_files)

            maint_gap = primary_commits - translation_commits

            # ── 3. Last-modified timestamps for time-gap health label
            def last_mod(path_list):
                lm = None
                for f in path_list:
                    t = get_file_last_modified(repo_dir, f['filename'],
                                               since_date, until_date)
                    if t and (lm is None or t > lm):
                        lm = t
                return lm

            primary_last      = last_mod(primary_files)
            translation_last  = last_mod(translation_files)

            if primary_last and translation_last:
                time_gap_days = (primary_last - translation_last).days
                if abs(time_gap_days) <= 7:   maintenance_health = 'excellent'
                elif abs(time_gap_days) <= 30: maintenance_health = 'good'
                elif abs(time_gap_days) <= 90: maintenance_health = 'fair'
                else:                          maintenance_health = 'poor'
            elif primary_last and not translation_last:
                maintenance_health, time_gap_days = 'abandoned', None
            elif not primary_last and not translation_last:
                maintenance_health, time_gap_days = 'inactive',  None
            else:
                maintenance_health, time_gap_days = 'unknown',   None

            # ── 4. Skip rows labelled 'unknown'
            if maintenance_health == 'unknown':
                continue

            results.append({
                'repo': r.repo,
                'pr_number': r.pr_number,
                'maint_gap': maint_gap,
                'maintenance_health': maintenance_health,
                'primary_commits': primary_commits,
                'translation_commits': translation_commits,
                'time_gap_days': time_gap_days,
                'files_detected': len(readme_files)
            })

        except Exception as e:
            print(f"Error processing {r.repo}#{r.pr_number}: {e}")
            results.append({
                'repo': r.repo, 'pr_number': r.pr_number,
                'maint_gap': None, 'maintenance_health': 'error',
                'primary_commits': 0, 'translation_commits': 0,
                'time_gap_days': None, 'files_detected': 0
            })

    # ── 5. Save & print summary
    out = pd.DataFrame(results)
    out.to_csv(OUT_DIR / "survival.csv", index=False)

    print("\n=== MAINTENANCE ANALYSIS ===")
    for health, count in out['maintenance_health'].value_counts().items():
        pct = 100 * count / len(out)
        print(f"  {health:<12}: {count}  ({pct:.1f}%)")

    gaps = out['time_gap_days'].dropna()
    if len(gaps):
        print(f"\nTime-gap stats (n={len(gaps)}): "
              f"mean={gaps.mean():.1f} d, median={gaps.median():.1f} d, "
              f"min={gaps.min()} d, max={gaps.max()} d")

    return out

# ─────────────── run (UPDATED) ──────────────
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("logfile", help="crawl log file (e.g., new.txt)")
    ap.add_argument("--legacy", action="store_true", 
                    help="Use legacy survival calculation instead of improved version")
    args=ap.parse_args()

    raw=parse_log(pathlib.Path(args.logfile))
    if raw.empty: raise SystemExit("Log parsed but found no PR bullets.")
    
    print(f"Found {len(raw)} PRs in log file")
    meta=enrich(raw)
    print(f"Successfully enriched {len(meta)} PRs with GitHub metadata")
    
    adoption(meta)
    
    if args.legacy:
        print("Using legacy survival calculation...")
        # Your original survival function would go here
    else:
        print("Using improved survival calculation...")
        survival(meta)
    
    print(f"\n✅  Files saved in {OUT_DIR}/")
    print("    - adoption.csv: Adoption rates per repository")
    print("    - survival.csv: Maintenance gap analysis with health metrics")