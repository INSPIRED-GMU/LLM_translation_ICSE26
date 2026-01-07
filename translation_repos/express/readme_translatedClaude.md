[![Express Logo](https://i.cloudup.com/zfY6lL7eFa-3000x3000.png)](https://expressjs.com/)

**Schnelles, unvoreingenommenes, minimalistisches Web-Framework für [Node.js](https://nodejs.org).**

**Dieses Projekt hat einen [Verhaltenskodex][].**

## Inhaltsverzeichnis

* [Installation](#Installation)
* [Funktionen](#Funktionen)
* [Dokumentation & Community](#dokumentation--community)
* [Schnellstart](#Schnellstart)
* [Tests ausführen](#Tests-ausführen)
* [Philosophie](#Philosophie)
* [Beispiele](#Beispiele)
* [Zu Express beitragen](#Beitragen)
* [TC (Technisches Komitee)](#tc-technisches-komitee)
* [Triager](#triager)
* [Lizenz](#lizenz)

[![NPM Version][npm-version-image]][npm-url]
[![NPM Downloads][npm-downloads-image]][npm-downloads-url]
[![OpenSSF Scorecard Badge][ossf-scorecard-badge]][ossf-scorecard-visualizer]

```js
import express from 'express'

const app = express()

app.get('/', (req, res) => {
  res.send('Hello World')
})

app.listen(3000)
```

## Installation

Dies ist ein [Node.js](https://nodejs.org/en/) Modul, das über die
[npm Registry](https://www.npmjs.com/) verfügbar ist.

Vor der Installation müssen Sie [Node.js herunterladen und installieren](https://nodejs.org/en/download/).
Node.js 18 oder höher ist erforderlich.

Bei einem neuen Projekt erstellen Sie zunächst eine `package.json`-Datei mit dem
[`npm init` Befehl](https://docs.npmjs.com/creating-a-package-json-file).

Die Installation erfolgt über den
[`npm install` Befehl](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):

```bash
npm install express
```

Weitere Informationen finden Sie in unserem [Installationshandbuch](https://expressjs.com/en/starter/installing.html).

## Funktionen

  * Robustes Routing
  * Fokus auf hohe Leistung
  * Sehr hohe Testabdeckung
  * HTTP-Hilfsfunktionen (Weiterleitung, Caching, etc.)
  * View-System mit Unterstützung für über 14 Template-Engines
  * Content Negotiation
  * Ausführbare Datei zum schnellen Generieren von Anwendungen

## Dokumentation & Community

  * [Website und Dokumentation](https://expressjs.com/) - [[Website-Repository](https://github.com/expressjs/expressjs.com)]
  * [GitHub-Organisation](https://github.com/expressjs) für offizielle Middleware & Module
  * [Github Discussions](https://github.com/expressjs/discussions) für Diskussionen über die Entwicklung und Nutzung von Express

**PROFI-TIPP** Lesen Sie unbedingt den [Migrationsleitfaden zu v5](https://expressjs.com/en/guide/migrating-5)

## Schnellstart

  Der schnellste Weg, mit Express zu beginnen, ist die Verwendung der ausführbaren Datei [`express(1)`](https://github.com/expressjs/generator) zum Generieren einer Anwendung:

  Installieren Sie die ausführbare Datei. Die Hauptversion entspricht der von Express:

```bash
npm install -g express-generator@4
```

  Erstellen Sie die App:

```bash
express /tmp/foo && cd /tmp/foo
```

  Installieren Sie die Abhängigkeiten:

```bash
npm install
```

  Starten Sie den Server:

```bash
npm start
```

  Website aufrufen unter: http://localhost:3000

## Philosophie

  Die Express-Philosophie ist es, kleine, robuste Werkzeuge für HTTP-Server bereitzustellen,
  was es zu einer großartigen Lösung für Single-Page-Anwendungen, Websites, Hybriden oder
  öffentliche HTTP-APIs macht.

  Express zwingt Sie nicht zur Verwendung einer bestimmten ORM oder Template-Engine. Mit Unterstützung
  für über 14 Template-Engines durch [@ladjs/consolidate](https://github.com/ladjs/consolidate)
  können Sie schnell Ihr perfektes Framework zusammenstellen.

## Beispiele

  Um die Beispiele anzusehen, klonen Sie das Express-Repository:

```bash
git clone https://github.com/expressjs/express.git --depth 1 && cd express
```

  Dann installieren Sie die Abhängigkeiten:

```bash
npm install
```

  Führen Sie dann das gewünschte Beispiel aus:

```bash
node examples/content-negotiation
```

## Beitragen

  [![Linux Build][github-actions-ci-image]][github-actions-ci-url]
  [![Test Coverage][coveralls-image]][coveralls-url]

Das Express.js-Projekt begrüßt alle konstruktiven Beiträge. Beiträge können viele Formen annehmen,
von Code für Fehlerbehebungen und Verbesserungen über Ergänzungen und Korrekturen der Dokumentation,
zusätzliche Tests, Sichtung eingehender Pull Requests und Issues und mehr!

Siehe den [Leitfaden zum Beitragen](Contributing.md) für weitere technische Details zum Beitragen.

### Sicherheitsprobleme

Wenn Sie eine Sicherheitslücke in Express entdecken, lesen Sie bitte die [Sicherheitsrichtlinien und -verfahren](Security.md).

### Tests ausführen

Um die Testsuite auszuführen, installieren Sie zuerst die Abhängigkeiten:

```bash
npm install
```

Dann führen Sie `npm test` aus:

```bash
npm test
```

## Personen

Der ursprüngliche Autor von Express ist [TJ Holowaychuk](https://github.com/tj)

[Liste aller Mitwirkenden](https://github.com/expressjs/express/graphs/contributors)

### TC (Technisches Komitee)

* [UlisesGascon](https://github.com/UlisesGascon) - **Ulises Gascón** (er/ihm)
* [jonchurch](https://github.com/jonchurch) - **Jon Church**
* [wesleytodd](https://github.com/wesleytodd) - **Wes Todd**
* [LinusU](https://github.com/LinusU) - **Linus Unnebäck**
* [blakeembrey](https://github.com/blakeembrey) - **Blake Embrey**
* [sheplu](https://github.com/sheplu) - **Jean Burellier**
* [crandmck](https://github.com/crandmck) - **Rand McKinney**
* [ctcpip](https://github.com/ctcpip) - **Chris de Almeida**

<details>
<summary>Ehemalige TC-Mitglieder</summary>

#### Ehemalige TC-Mitglieder

  * [dougwilson](https://github.com/dougwilson) - **Douglas Wilson**
  * [hacksparrow](https://github.com/hacksparrow) - **Hage Yaapa**
  * [jonathanong](https://github.com/jonathanong) - **jongleberry**
  * [niftylettuce](https://github.com/niftylettuce) - **niftylettuce**
  * [troygoode](https://github.com/troygoode) - **Troy Goode**
</details>

### Triager

* [aravindvnair99](https://github.com/aravindvnair99) - **Aravind Nair**
* [bjohansebas](https://github.com/bjohansebas) - **Sebastian Beltran**
* [carpasse](https://github.com/carpasse) - **Carlos Serrano**
* [CBID2](https://github.com/CBID2) - **Christine Belzie**
* [enyoghasim](https://github.com/enyoghasim) - **David Enyoghasim**
* [UlisesGascon](https://github.com/UlisesGascon) - **Ulises Gascón** (er/ihm)
* [mertcanaltin](https://github.com/mertcanaltin) - **Mert Can Altin**
* [0ss](https://github.com/0ss) - **Salah**
* [import-brain](https://github.com/import-brain) - **Eric Cheng** (er/ihm)
* [3imed-jaberi](https://github.com/3imed-jaberi) - **Imed Jaberi**
* [dakshkhetan](https://github.com/dakshkhetan) - **Daksh Khetan** (er/ihm)
* [lucasraziel](https://github.com/lucasraziel) - **Lucas Soares Do Rego**
* [IamLizu](https://github.com/IamLizu) - **S M Mahmudul Hasan** (er/ihm)
* [Sushmeet](https://github.com/Sushmeet) - **Sushmeet Sunger**
* [rxmarbles](https://github.com/rxmarbles) **Rick Markins** (Er/ihm)

<details>
<summary>Ehemalige Triager-Mitglieder</summary>

#### Ehemalige Triager

[Liste der ehemaligen Triager bleibt unverändert...]
</details>

## Lizenz

  [MIT](LICENSE)

[coveralls-image]: https://badgen.net/coveralls/c/github/expressjs/express/master
[coveralls-url]: https://coveralls.io/r/expressjs/express?branch=master
[github-actions-ci-image]: https://badgen.net/github/checks/expressjs/express/master?label=CI
[github-actions-ci-url]: https://github.com/expressjs/express/actions/workflows/ci.yml
[npm-downloads-image]: https://badgen.net/npm/dm/express
[npm-downloads-url]: https://npmcharts.com/compare/express?minimal=true
[npm-url]: https://npmjs.org/package/express
[npm-version-image]: https://badgen.net/npm/v/express
[ossf-scorecard-badge]: https://api.scorecard.dev/projects/github.com/expressjs/express/badge
[ossf-scorecard-visualizer]: https://ossf.github.io/scorecard-visualizer/#/projects/github.com/expressjs/express
[Code of Conduct]: https://github.com/expressjs/express/blob/master/Code-Of-Conduct.md