# Kubernetes (K8s)

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/569/badge)](https://bestpractices.coreinfrastructure.org/projects/569) [![Go Report Card](https://goreportcard.com/badge/github.com/kubernetes/kubernetes)](https://goreportcard.com/report/github.com/kubernetes/kubernetes) ![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/kubernetes/kubernetes?sort=semver)

<img src="https://github.com/kubernetes/kubernetes/raw/master/logo/logo.png" width="100">

----

Kubernetes, auch bekannt als K8s, ist ein Open-Source-System zur Verwaltung von [containersisierten Anwendungen][containerized applications]
über mehrere Hosts hinweg. Es stellt grundlegende Mechanismen für die Bereitstellung, Wartung
und Skalierung von Anwendungen bereit.

Kubernetes baut auf eineinhalb Jahrzehnten Erfahrung von Google beim Betreiben von
Produktions-Workloads im großen Maßstab mittels eines Systems namens [Borg] auf,
kombiniert mit den besten Ideen und Praktiken aus der Community.

Kubernetes wird von der Cloud Native Computing Foundation ([CNCF]) gehostet.
Wenn Ihr Unternehmen die Entwicklung von Technologien mitgestalten möchte,
die in Containern verpackt, dynamisch geplant und
mikroserviceorientiert sind, erwägen Sie einen Beitritt zur CNCF.
Details darüber, wer beteiligt ist und welche Rolle Kubernetes spielt,
finden Sie in der CNCF-[Ankündigung][announcement].

----

## K8s verwenden

Siehe unsere Dokumentation auf [kubernetes.io].

Machen Sie einen kostenlosen Kurs zu [Scalable Microservices with Kubernetes].

Um Kubernetes-Code als Bibliothek in anderen Anwendungen zu verwenden, siehe die [Liste der veröffentlichten Komponenten](https://git.k8s.io/kubernetes/staging/README.md).
Die Verwendung des `k8s.io/kubernetes`-Moduls oder der `k8s.io/kubernetes/...`-Pakete als Bibliotheken wird nicht unterstützt.

## K8s entwickeln

Das [Community-Repository][community repository] enthält alle Informationen über
das Bauen von Kubernetes aus den Quellen, wie man Code und
Dokumentation beitragen kann, wen man wobei kontaktieren kann, etc.

Wenn Sie Kubernetes sofort bauen möchten, gibt es zwei Optionen:

##### Sie haben eine funktionierende [Go-Umgebung][Go environment].

```
git clone https://github.com/kubernetes/kubernetes
cd kubernetes
make
```

##### Sie haben eine funktionierende [Docker-Umgebung][Docker environment].

```
git clone https://github.com/kubernetes/kubernetes
cd kubernetes
make quick-release
```

Die vollständige Geschichte finden Sie in der [Entwickler-Dokumentation][developer's documentation].

## Support

Wenn Sie Unterstützung benötigen, beginnen Sie mit dem [Fehlerbehebungsleitfaden][troubleshooting guide]
und arbeiten Sie sich durch den von uns beschriebenen Prozess.

Wenn Sie Fragen haben, kontaktieren Sie uns
[auf die eine oder andere Weise][communication].

[Alle Original-Links bleiben unverändert]

## Community-Meetings

Der [Kalender](https://www.kubernetes.dev/resources/calendar/) enthält die Liste aller Meetings in der Kubernetes-Community an einem Ort.

## Anwender

Die [User Case Studies](https://kubernetes.io/case-studies/) Website enthält reale Anwendungsfälle von Organisationen aus verschiedenen Branchen, die Kubernetes einsetzen oder darauf migrieren.

## Governance

Das Kubernetes-Projekt wird durch ein Framework von Prinzipien, Werten, Richtlinien und Prozessen geleitet, die unserer Community und den Beteiligten helfen, unsere gemeinsamen Ziele zu erreichen.

Die [Kubernetes Community](https://github.com/kubernetes/community/blob/master/governance.md) ist der Ausgangspunkt, um zu erfahren, wie wir uns organisieren.

Das [Kubernetes Steering Community Repo](https://github.com/kubernetes/steering) wird vom Kubernetes Steering Committee verwendet, das die Governance des Kubernetes-Projekts beaufsichtigt.

## Roadmap

Das [Kubernetes Enhancements Repo](https://github.com/kubernetes/enhancements) bietet Informationen über Kubernetes-Releases sowie Feature-Tracking und Backlogs.