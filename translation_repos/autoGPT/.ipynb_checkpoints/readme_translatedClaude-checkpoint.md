# AutoGPT: KI-Agenten erstellen, bereitstellen und ausführen

[![Discord Follow](https://dcbadge.vercel.app/api/server/autogpt?style=flat)](https://discord.gg/autogpt) &ensp;
[![Twitter Follow](https://img.shields.io/twitter/follow/Auto_GPT?style=social)](https://twitter.com/Auto_GPT) &ensp;
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**AutoGPT** ist eine leistungsstarke Plattform, mit der Sie kontinuierliche KI-Agenten erstellen, bereitstellen und verwalten können, die komplexe Arbeitsabläufe automatisieren.

## Hosting-Optionen
   - Download zum Selbst-Hosting
   - [Der Warteliste beitreten](https://bit.ly/3ZDijAI) für die Cloud-gehostete Beta

## Einrichtung für Selbst-Hosting
> [!NOTE]
> Das Einrichten und Hosten der AutoGPT-Plattform selbst ist ein technischer Prozess.
> Wenn Sie etwas bevorzugen, das einfach funktioniert, empfehlen wir [der Warteliste beizutreten](https://bit.ly/3ZDijAI) für die Cloud-gehostete Beta.

https://github.com/user-attachments/assets/d04273a5-b36a-4a37-818e-f631ce72d603

Dieses Tutorial setzt voraus, dass Docker, VSCode, git und npm installiert sind.

### 🧱 AutoGPT Frontend

Das AutoGPT Frontend ist die Schnittstelle, über die Benutzer mit unserer leistungsstarken KI-Automatisierungsplattform interagieren. Es bietet mehrere Möglichkeiten, mit unseren KI-Agenten zu arbeiten. Hier setzen Sie Ihre KI-Automatisierungsideen in die Tat um:

   **Agent Builder:** Für diejenigen, die anpassen möchten, ermöglicht unsere intuitive Low-Code-Oberfläche das Design und die Konfiguration eigener KI-Agenten.
   
   **Workflow-Management:** Erstellen, modifizieren und optimieren Sie Ihre Automatisierungs-Workflows mit Leichtigkeit. Sie erstellen Ihren Agenten durch Verbinden von Blöcken, wobei jeder Block eine einzelne Aktion ausführt.
   
   **Bereitstellungssteuerung:** Verwalten Sie den Lebenszyklus Ihrer Agenten vom Test bis zur Produktion.
   
   **Einsatzbereite Agenten:** Keine Lust zu bauen? Wählen Sie einfach aus unserer Bibliothek vorkonfigurierter Agenten und setzen Sie sie sofort ein.
   
   **Agenten-Interaktion:** Ob Sie eigene erstellt haben oder vorkonfigurierte Agenten verwenden, führen Sie diese einfach über unsere benutzerfreundliche Oberfläche aus und interagieren Sie mit ihnen.

   **Überwachung und Analyse:** Behalten Sie die Leistung Ihrer Agenten im Auge und gewinnen Sie Erkenntnisse zur kontinuierlichen Verbesserung Ihrer Automatisierungsprozesse.

[Lesen Sie diese Anleitung](https://docs.agpt.co/platform/new_blocks/), um zu lernen, wie Sie eigene Blöcke erstellen.

### 💽 AutoGPT Server

Der AutoGPT Server ist das Kraftwerk unserer Plattform. Hier laufen Ihre Agenten. Nach der Bereitstellung können Agenten durch externe Quellen ausgelöst werden und kontinuierlich arbeiten. Er enthält alle wesentlichen Komponenten, die AutoGPT reibungslos laufen lassen.

   **Quellcode:** Die Kernlogik, die unsere Agenten und Automatisierungsprozesse antreibt.
   
   **Infrastruktur:** Robuste Systeme, die zuverlässige und skalierbare Leistung gewährleisten.
   
   **Marktplatz:** Ein umfassender Marktplatz, auf dem Sie eine große Auswahl an vorgefertigten Agenten finden und einsetzen können.

### 🐙 Beispiel-Agenten

Hier sind zwei Beispiele, was Sie mit AutoGPT machen können:

1. **Virale Videos aus Trendthemen generieren**
   - Dieser Agent liest Themen auf Reddit.
   - Er identifiziert Trendthemen.
   - Dann erstellt er automatisch ein Kurzform-Video basierend auf dem Inhalt.

2. **Top-Zitate aus Videos für Social Media identifizieren**
   - Dieser Agent abonniert Ihren YouTube-Kanal.
   - Wenn Sie ein neues Video posten, transkribiert er es.
   - Er verwendet KI, um die wirkungsvollsten Zitate zu identifizieren und eine Zusammenfassung zu erstellen.
   - Dann schreibt er einen Beitrag, der automatisch in Ihren sozialen Medien veröffentlicht wird.

Diese Beispiele zeigen nur einen kleinen Einblick dessen, was Sie mit AutoGPT erreichen können! Sie können angepasste Workflows erstellen, um Agenten für jeden Anwendungsfall zu erstellen.

---
### Mission und Lizenzierung
Unsere Mission ist es, die Werkzeuge bereitzustellen, damit Sie sich auf das Wesentliche konzentrieren können:

- 🏗️ **Aufbauen** - Legen Sie den Grundstein für etwas Großartiges.
- 🧪 **Testen** - Optimieren Sie Ihren Agenten zur Perfektion.
- 🤝 **Delegieren** - Lassen Sie KI für Sie arbeiten und Ihre Ideen Wirklichkeit werden.

Seien Sie Teil der Revolution! **AutoGPT** ist gekommen, um zu bleiben, an der Spitze der KI-Innovation.

**📖 [Dokumentation](https://docs.agpt.co)**
&ensp;|&ensp;
**🚀 [Mitwirken](CONTRIBUTING.md)**

**Lizenzierung:**

MIT-Lizenz: Der Großteil des AutoGPT-Repositories steht unter der MIT-Lizenz.

Polyform Shield-Lizenz: Diese Lizenz gilt für den autogpt_platform-Ordner.

Weitere Informationen finden Sie unter https://agpt.co/blog/introducing-the-autogpt-platform

---
## 🤖 AutoGPT Classic
> Nachfolgend finden Sie Informationen zur klassischen Version von AutoGPT.

**🛠️ [Bauen Sie Ihren eigenen Agenten - Schnellstart](classic/FORGE-QUICKSTART.md)**

### 🏗️ Forge

**Schmieden Sie Ihren eigenen Agenten!** &ndash; Forge ist ein einsatzbereites Toolkit zum Erstellen Ihrer eigenen Agenten-Anwendung. Es übernimmt den größten Teil des Boilerplate-Codes und lässt Ihnen alle Kreativität für die Dinge, die *Ihren* Agenten auszeichnen. Alle Tutorials finden Sie [hier](https://medium.com/@aiedge/autogpt-forge-e3de53cc58ec). Komponenten aus [`forge`](/classic/forge/) können auch einzeln verwendet werden, um die Entwicklung zu beschleunigen und Boilerplate in Ihrem Agenten-Projekt zu reduzieren.

🚀 [**Erste Schritte mit Forge**](https://github.com/Significant-Gravitas/AutoGPT/blob/master/classic/forge/tutorials/001_getting_started.md) &ndash;
Diese Anleitung führt Sie durch den Prozess der Erstellung Ihres eigenen Agenten und der Verwendung des Benchmarks und der Benutzeroberfläche.

📘 [Erfahren Sie mehr](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/forge) über Forge

### 🎯 Benchmark

**Messen Sie die Leistung Ihres Agenten!** Der `agbenchmark` kann mit jedem Agenten verwendet werden, der das Agent-Protokoll unterstützt, und die Integration mit der [CLI] des Projekts macht es noch einfacher, ihn mit AutoGPT und Forge-basierten Agenten zu verwenden. Der Benchmark bietet eine strenge Testumgebung. Unser Framework ermöglicht autonome, objektive Leistungsbewertungen und stellt sicher, dass Ihre Agenten für den realen Einsatz bereit sind.

📦 [`agbenchmark`](https://pypi.org/project/agbenchmark/) auf Pypi
&ensp;|&ensp;
📘 [Erfahren Sie mehr](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/benchmark) über den Benchmark

### 💻 UI

**Macht Agenten einfach zu bedienen!** Das `frontend` bietet Ihnen eine benutzerfreundliche Oberfläche zur Steuerung und Überwachung Ihrer Agenten. Es verbindet sich über das [Agent-Protokoll](#-agent-protocol) mit Agenten und gewährleistet die Kompatibilität mit vielen Agenten sowohl innerhalb als auch außerhalb unseres Ökosystems.

Das Frontend funktioniert sofort mit allen Agenten im Repository. Verwenden Sie einfach die [CLI], um Ihren gewünschten Agenten auszuführen!

📘 [Erfahren Sie mehr](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/frontend) über das Frontend

### ⌨️ CLI

[CLI]: #-cli

Um die Verwendung aller vom Repository angebotenen Tools so einfach wie möglich zu gestalten, ist eine CLI im Root des Repos enthalten:

```shell
$ ./run
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  agent      Commands to create, start and stop agents
  benchmark  Commands to start the benchmark and list tests and categories
  setup      Installs dependencies needed for your system.
```

Klonen Sie einfach das Repo, installieren Sie Abhängigkeiten mit `./run setup`, und Sie können loslegen!

## 🤔 Fragen? Probleme? Vorschläge?

### Hilfe erhalten - [Discord 💬](https://discord.gg/autogpt)

[![Join us on Discord](https://invidget.switchblade.xyz/autogpt)](https://discord.gg/autogpt)

Um einen Fehler zu melden oder eine Funktion anzufordern, erstellen Sie ein [GitHub Issue](https://github.com/Significant-Gravitas/AutoGPT/issues/new/choose). Bitte stellen Sie sicher, dass nicht bereits jemand anderes ein Issue für das gleiche Thema erstellt hat.

## 🤝 Schwesterprojekte

### 🔄 Agent-Protokoll

Um einen einheitlichen Standard zu wahren und nahtlose Kompatibilität mit vielen aktuellen und zukünftigen Anwendungen zu gewährleisten, verwendet AutoGPT den [Agent-Protokoll](https://agentprotocol.ai/) Standard der AI Engineer Foundation. Dies standardisiert die Kommunikationswege von Ihrem Agenten zum Frontend und Benchmark.

---

## Sterne-Statistik

<p align="center">
<a href="https://star-history.com/#Significant-Gravitas/AutoGPT">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=Significant-Gravitas/AutoGPT&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=Significant-Gravitas/AutoGPT&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=Significant-Gravitas/AutoGPT&type=Date" />
  </picture>
</a>
</p>

## ⚡ Mitwirkende

<a href="https://github.com/Significant-Gravitas/AutoGPT/graphs/contributors" alt="Mitwirkende anzeigen">
  <img src="https://contrib.rocks/image?repo=Significant-Gravitas/AutoGPT&max=1000&columns=10" alt="Mitwirkende" />
</a>