# Kubernetes (K8s)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/569/badge)](https://bestpractices.coreinfrastructure.org/projects/569) [![Go Report Card](https://goreportcard.com/badge/github.com/kubernetes/kubernetes)](https://goreportcard.com/report/github.com/kubernetes/kubernetes) ![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/kubernetes/kubernetes?sort=semver)

<img src="https://github.com/kubernetes/kubernetes/raw/master/logo/logo.png" width="100">

----

Kubernetes, auch bekannt als K8s, ist ein Open-Source-System zur Verwaltung von [containerisierten Anwendungen](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) über mehrere Hosts hinweg. Es bietet grundlegende Mechanismen für die Bereitstellung, Wartung und Skalierung von Anwendungen.

Kubernetes baut auf anderthalb Jahrzehnten Erfahrung bei Google auf, wo produktive Arbeitslasten im großen Maßstab mit einem System namens [Borg](https://research.google.com/pubs/pub43438.html?authuser=1) betrieben wurden, kombiniert mit bewährten Ideen und Praktiken aus der Community.

Kubernetes wird von der Cloud Native Computing Foundation ([CNCF](https://www.cncf.io/about)) gehostet.  
Wenn Ihr Unternehmen die Entwicklung von Technologien mitgestalten möchte, die containerbasiert, dynamisch geplant und mikroserviceorientiert sind, sollten Sie der CNCF beitreten.  
Weitere Informationen darüber, wer beteiligt ist und welche Rolle Kubernetes spielt, finden Sie in der CNCF-[Ankündigung](https://cncf.io/news/announcement/2015/07/new-cloud-native-computing-foundation-drive-alignment-among-container).

----

## So startest du mit K8s

Siehe unsere Dokumentation auf [kubernetes.io](https://kubernetes.io).

Besuche einen kostenlosen Kurs zu [Skalierbaren Microservices mit Kubernetes](https://www.udacity.com/course/scalable-microservices-with-kubernetes--ud615).

Wenn du Kubernetes-Code als Bibliothek in anderen Anwendungen verwenden möchtest, sieh dir die [Liste der veröffentlichten Komponenten](https://git.k8s.io/kubernetes/staging/README.md) an.  
Die Nutzung des Moduls `k8s.io/kubernetes` oder der Pakete `k8s.io/kubernetes/...` als Bibliotheken wird nicht unterstützt.

## So entwickelst du für K8s

Das [Community-Repository](https://git.k8s.io/community) enthält alle Informationen zum Bauen von Kubernetes aus dem Quellcode, zum Mitwirken an Code und Dokumentation sowie Kontaktinformationen.

Wenn du Kubernetes direkt bauen möchtest, gibt es zwei Optionen:

##### Du hast eine funktionierende [Go-Umgebung](https://go.dev/doc/install).

```bash
git clone https://github.com/kubernetes/kubernetes
cd kubernetes
make
```

##### Du hast eine funktionierende [Docker-Umgebung](https://docs.docker.com/engine).

```bash
git clone https://github.com/kubernetes/kubernetes
cd kubernetes
make quick-release
```

Für alle Details besuche die [Entwicklerdokumentation](https://git.k8s.io/community/contributors/devel#readme).

## Support

Wenn du Unterstützung benötigst, beginne mit dem [Troubleshooting-Guide](https://kubernetes.io/docs/tasks/debug/) und folge den dort beschriebenen Schritten.

Falls du Fragen hast, melde dich gerne bei uns [über einen der Kommunikationswege](https://git.k8s.io/community/communication).

## Community-Meetings

Der [Kalender](https://www.kubernetes.dev/resources/calendar/) enthält eine Übersicht aller Meetings in der Kubernetes-Community.

## Anwender

Die Website [User Case Studies](https://kubernetes.io/case-studies/) zeigt reale Anwendungsfälle von Organisationen aus verschiedenen Branchen, die Kubernetes einsetzen oder darauf migrieren.

## Governance

Das Kubernetes-Projekt wird durch ein Framework aus Prinzipien, Werten, Richtlinien und Prozessen geleitet, um die Community und Interessengruppen bei der Erreichung gemeinsamer Ziele zu unterstützen.

Die [Kubernetes-Community](https://github.com/kubernetes/community/blob/master/governance.md) ist der Ausgangspunkt, um mehr über unsere Organisation zu erfahren.

Das [Kubernetes Steering Community Repository](https://github.com/kubernetes/steering) wird vom Steering Committee genutzt, das die Governance des Kubernetes-Projekts überwacht.

## Roadmap

Das [Kubernetes Enhancements Repository](https://github.com/kubernetes/enhancements) bietet Informationen zu Kubernetes-Versionen sowie zur Feature-Verwaltung und zum Backlog.

