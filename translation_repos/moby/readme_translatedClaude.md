Das Moby Projekt
================

[![PkgGoDev](https://pkg.go.dev/badge/github.com/docker/docker)](https://pkg.go.dev/github.com/docker/docker)
[![Go Report Card](https://goreportcard.com/badge/github.com/docker/docker)](https://goreportcard.com/report/github.com/docker/docker)
[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/moby/moby/badge)](https://scorecard.dev/viewer/?uri=github.com/moby/moby)

![Moby Project logo](docs/static_files/moby-project-logo.png "The Moby Project")

Moby ist ein Open-Source-Projekt, das von Docker entwickelt wurde, um die Software-Containerisierung zu ermöglichen und zu beschleunigen.

Es stellt einen "Lego-Baukasten" von Toolkit-Komponenten bereit, ein Framework für deren Zusammenstellung zu benutzerdefinierten containerbasierten Systemen und einen Ort für alle Container-Enthusiasten und Profis zum Experimentieren und Ideenaustausch.

Zu den Komponenten gehören Container-Build-Tools, eine Container-Registry, Orchestrierungs-Tools, eine Laufzeitumgebung und mehr. Diese können als Bausteine in Verbindung mit anderen Tools und Projekten verwendet werden.

## Prinzipien

Moby ist ein offenes Projekt, das von starken Prinzipien geleitet wird und darauf abzielt, modular und flexibel zu sein, ohne zu starke Vorgaben für die Benutzererfahrung zu machen.
Die Community ist eingeladen, bei der Festlegung der Richtung zu helfen.

- Modular: Das Projekt umfasst viele Komponenten mit klar definierten Funktionen und APIs, die zusammenarbeiten.
- Batterien inklusive, aber austauschbar: Moby enthält genügend Komponenten, um vollständig funktionsfähige Container-Systeme zu erstellen, aber seine modulare Architektur stellt sicher, dass die meisten Komponenten durch verschiedene Implementierungen ausgetauscht werden können.
- Nutzbare Sicherheit: Moby bietet sichere Standardeinstellungen, ohne die Benutzerfreundlichkeit zu beeinträchtigen.
- Entwicklerfokussiert: Die APIs sollen funktional und nützlich sein, um leistungsfähige Tools zu erstellen.
Sie sind nicht unbedingt als Endbenutzer-Tools gedacht, sondern als Komponenten für Entwickler.
Dokumentation und UX sind auf Entwickler und nicht auf Endbenutzer ausgerichtet.

## Zielgruppe

Das Moby-Projekt richtet sich an Ingenieure, Integratoren und Enthusiasten, die Systeme auf Basis von Containern modifizieren, hacken, reparieren, experimentieren, erfinden und entwickeln möchten.
Es ist nicht für Menschen gedacht, die ein kommerziell unterstütztes System suchen, sondern für Menschen, die mit Open-Source-Code arbeiten und lernen möchten.

## Beziehung zu Docker

Die Komponenten und Tools im Moby-Projekt sind zunächst die Open-Source-Komponenten, die Docker und die Community für das Docker-Projekt entwickelt haben.
Neue Projekte können hinzugefügt werden, wenn sie zu den Community-Zielen passen. Docker verpflichtet sich, Moby als Upstream für das Docker-Produkt zu nutzen.
Allerdings werden auch andere Projekte ermutigt, Moby als Upstream zu nutzen und die Komponenten auf verschiedene Weise wiederzuverwenden, und all diese Nutzungen werden gleich behandelt. Externe Maintainer und Mitwirkende sind willkommen.

Das Moby-Projekt ist nicht als Anlaufstelle für Support oder Feature-Anfragen für Docker-Produkte gedacht, sondern als Ort, an dem Mitwirkende an Open-Source-Code arbeiten, Fehler beheben und den Code nützlicher machen können.
Die Releases werden von den Maintainern, der Community und den Benutzern nach bestem Wissen und Gewissen unterstützt. Für Kunden, die Enterprise- oder kommerziellen Support wünschen, sind [Docker Desktop](https://www.docker.com/products/docker-desktop/) und [Mirantis Container Runtime](https://www.mirantis.com/software/mirantis-container-runtime/) die geeigneten Produkte für diese Anwendungsfälle.

-----

Rechtliches
=====

*Mit freundlicher Genehmigung unserer Rechtsberater. Für mehr Kontext
siehe bitte das [NOTICE](https://github.com/moby/moby/blob/master/NOTICE)-Dokument in diesem Repository.*

Die Nutzung und Übertragung von Moby kann bestimmten Beschränkungen durch die
Vereinigten Staaten und andere Regierungen unterliegen.

Es liegt in Ihrer Verantwortung sicherzustellen, dass Ihre Nutzung und/oder Übertragung keine
geltenden Gesetze verletzt.

Weitere Informationen finden Sie unter https://www.bis.doc.gov

Lizenzierung
=========

Moby ist unter der Apache License, Version 2.0 lizenziert. Siehe
[LICENSE](https://github.com/moby/moby/blob/master/LICENSE) für den vollständigen
Lizenztext.