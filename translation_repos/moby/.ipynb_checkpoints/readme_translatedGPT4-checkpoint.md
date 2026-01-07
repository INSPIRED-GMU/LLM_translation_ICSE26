# Das Moby Projekt

[![PkgGoDev](https://pkg.go.dev/badge/github.com/docker/docker)](https://pkg.go.dev/github.com/docker/docker)
[![Go Report Card](https://goreportcard.com/badge/github.com/docker/docker)](https://goreportcard.com/report/github.com/docker/docker)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/moby/moby/badge)](https://scorecard.dev/viewer/?uri=github.com/moby/moby)

![Moby Projekt Logo](docs/static_files/moby-project-logo.png "Das Moby Projekt")

Moby ist ein Open-Source-Projekt, das von Docker ins Leben gerufen wurde, um die Software-Containerisierung zu ermöglichen und zu beschleunigen.

Es bietet einen "Lego-Baukasten" von Toolkit-Komponenten, das Framework zur Zusammenstellung dieser in benutzerdefinierte containerbasierte Systeme und eine Plattform für alle Container-Enthusiasten und -Profis, um zu experimentieren und Ideen auszutauschen. Komponenten umfassen Werkzeuge zum Erstellen von Containern, ein Container-Register, Orchestrierungswerkzeuge, eine Laufzeitumgebung und mehr. Diese können als Bausteine zusammen mit anderen Tools und Projekten verwendet werden.

## Prinzipien

Moby ist ein offenes Projekt, das von starken Prinzipien geleitet wird und darauf abzielt, modular, flexibel und ohne zu starke Meinungen zur Benutzererfahrung zu sein. Es steht der Community offen, um seine Richtung mitzubestimmen.

- **Modular:** Das Projekt umfasst viele Komponenten mit klar definierten Funktionen und APIs, die zusammenarbeiten.
- **Mitgelieferte, aber austauschbare Komponenten:** Moby enthält genügend Komponenten, um vollständig ausgestattete Container-Systeme zu bauen, aber seine modulare Architektur ermöglicht es, die meisten Komponenten durch andere Implementierungen zu ersetzen.
- **Benutzerfreundliche Sicherheit:** Moby bietet sichere Standardeinstellungen, ohne die Benutzerfreundlichkeit zu beeinträchtigen.
- **Entwicklerzentriert:** Die APIs sind darauf ausgelegt, funktional und nützlich zu sein, um leistungsstarke Werkzeuge zu erstellen. Sie sind nicht unbedingt als Endbenutzer-Tools gedacht, sondern als Komponenten für Entwickler. Dokumentation und Benutzererfahrung richten sich an Entwickler, nicht an Endnutzer.

## Zielgruppe

Das Moby Projekt richtet sich an Ingenieure, Integratoren und Enthusiasten, die Systeme auf Basis von Containern verändern, hacken, reparieren, experimentieren, erfinden und bauen möchten. Es ist nicht für Personen gedacht, die ein kommerziell unterstütztes System suchen, sondern für diejenigen, die mit Open-Source-Code arbeiten und lernen wollen.

## Beziehung zu Docker

Die Komponenten und Werkzeuge im Moby Projekt sind ursprünglich die Open-Source-Komponenten, die Docker und die Community für das Docker Projekt entwickelt haben. Neue Projekte können hinzugefügt werden, wenn sie mit den Zielen der Community übereinstimmen. Docker hat sich verpflichtet, Moby als Upstream für das Docker Produkt zu nutzen. Allerdings werden auch andere Projekte ermutigt, Moby als Upstream zu verwenden und die Komponenten auf vielfältige Weise wiederzuverwenden. Alle diese Nutzungen werden gleich behandelt. Externe Maintainer und Mitwirkende sind willkommen.

Das Moby Projekt ist nicht als Anlaufstelle für Support- oder Funktionsanfragen für Docker-Produkte gedacht, sondern als Plattform für Mitwirkende, um an Open-Source-Code zu arbeiten, Fehler zu beheben und den Code nützlicher zu machen. Die Releases werden von den Maintainern, der Community und den Nutzern nur nach bestem Wissen und Gewissen unterstützt. Für Kunden, die unternehmensweite oder kommerzielle Unterstützung wünschen, sind [Docker Desktop](https://www.docker.com/products/docker-desktop/) und [Mirantis Container Runtime](https://www.mirantis.com/software/mirantis-container-runtime/) die passenden Produkte für diese Anwendungsfälle.

-----

# Rechtliches

*Bereitgestellt durch unsere Rechtsabteilung. Für mehr Kontext siehe bitte das [NOTICE](https://github.com/moby/moby/blob/master/NOTICE)-Dokument in diesem Repository.*

Die Nutzung und Weitergabe von Moby kann bestimmten Einschränkungen durch die Vereinigten Staaten und andere Regierungen unterliegen.

Es liegt in Ihrer Verantwortung sicherzustellen, dass Ihre Nutzung und/oder Weitergabe keine geltenden Gesetze verletzt.

Für weitere Informationen besuchen Sie bitte https://www.bis.doc.gov

# Lizenzierung

Moby ist unter der Apache-Lizenz, Version 2.0, lizenziert. Den vollständigen Lizenztext finden Sie in der [LICENSE](https://github.com/moby/moby/blob/master/LICENSE).

