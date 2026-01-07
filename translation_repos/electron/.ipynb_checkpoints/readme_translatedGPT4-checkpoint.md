[![Electron Logo](https://electronjs.org/images/electron-logo.svg)](https://electronjs.org)

[![GitHub Actions Build Status](https://github.com/electron/electron/actions/workflows/build.yml/badge.svg)](https://github.com/electron/electron/actions/workflows/build.yml)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/4lggi9dpjc1qob7k/branch/main?svg=true)](https://ci.appveyor.com/project/electron-bot/electron-ljo26/branch/main)
[![Electron Discord Invite](https://img.shields.io/discord/745037351163527189?color=%237289DA&label=chat&logo=discord&logoColor=white)](https://discord.gg/electronjs)

:memo: Verfügbare Übersetzungen: 🇨🇳 🇧🇷 🇪🇸 🇯🇵 🇷🇺 🇫🇷 🇺🇸 🇩🇪.
Sieh dir diese Dokumente in anderen Sprachen in unserem [Crowdin](https://crowdin.com/project/electron)-Projekt an.

Das Electron-Framework ermöglicht es dir, plattformübergreifende Desktop-Anwendungen mit JavaScript, HTML und CSS zu entwickeln. Es basiert auf [Node.js](https://nodejs.org/) und [Chromium](https://www.chromium.org) und wird unter anderem von [Visual Studio Code](https://github.com/Microsoft/vscode/) und vielen anderen [Apps](https://electronjs.org/apps) verwendet.

Folge [@electronjs](https://twitter.com/electronjs) auf Twitter für wichtige Ankündigungen.

Dieses Projekt folgt dem Contributor Covenant [Verhaltenskodex](https://github.com/electron/electron/tree/main/CODE_OF_CONDUCT.md). Mit deiner Teilnahme erklärst du dich bereit, diesen Kodex einzuhalten. Unangemessenes Verhalten kann an [coc@electronjs.org](mailto:coc@electronjs.org) gemeldet werden.

## Installation

Um vorgefertigte Electron-Binärdateien zu installieren, verwende [`npm`](https://docs.npmjs.com/).
Der bevorzugte Weg ist, Electron als Entwicklungsabhängigkeit in deiner App zu installieren:

```sh
npm install electron --save-dev
```

Weitere Installationsoptionen und Tipps zur Fehlerbehebung findest du unter [Installation](docs/tutorial/installation.md). Informationen zur Verwaltung von Electron-Versionen in deinen Apps findest du unter [Electron-Versionierung](docs/tutorial/electron-versioning.md).

## Plattformunterstützung

Jede Electron-Version stellt Binärdateien für macOS, Windows und Linux bereit.

* **macOS (Big Sur und neuer)**: Electron bietet 64-Bit Intel- und Apple Silicon-/ARM-Binärdateien für macOS.
* **Windows (Windows 10 und neuer)**: Electron bietet `ia32` (`x86`), `x64` (`amd64`) und `arm64`-Binärdateien für Windows. Unterstützung für Windows 7, 8 und 8.1 wurde in [Electron 23 entfernt](https://www.electronjs.org/blog/windows-7-to-8-1-deprecation-notice).
* **Linux**: Die vorgefertigten Binärdateien von Electron werden auf Ubuntu 20.04 erstellt und funktionieren auch auf:
  * Ubuntu 18.04 und neuer
  * Fedora 32 und neuer
  * Debian 10 und neuer

## Schnellstart & Electron Fiddle

Verwende [`Electron Fiddle`](https://github.com/electron/fiddle), um kleine Electron-Experimente zu erstellen, auszuführen und zu verpacken.

Alternativ kannst du das Repository [electron/electron-quick-start](https://github.com/electron/electron-quick-start) klonen und ausführen, um eine minimale Electron-App in Aktion zu sehen:

```sh
git clone https://github.com/electron/electron-quick-start
cd electron-quick-start
npm install
npm start
```

## Ressourcen zum Lernen von Electron

* [electronjs.org/docs](https://electronjs.org/docs) – Sämtliche Electron-Dokumentation
* [electron/fiddle](https://github.com/electron/fiddle) – Ein Tool zum Entwickeln von kleinen Electron-Experimenten
* [electron/electron-quick-start](https://github.com/electron/electron-quick-start) – Ein einfaches Starterprojekt
* [electronjs.org/community#boilerplates](https://electronjs.org/community#boilerplates) – Community-Boilerplates

## Programmatische Nutzung

Die meisten nutzen Electron über die Kommandozeile, aber du kannst `electron` auch in deiner **Node-App** einbinden:

```javascript
const electron = require('electron')
const proc = require('node:child_process')

console.log(electron)

const child = proc.spawn(electron)
```

### Mirrors

* [China](https://npmmirror.com/mirrors/electron/)

Siehe die [erweiterten Installationsanweisungen](https://www.electronjs.org/docs/latest/tutorial/installation#mirror) für die Verwendung eines benutzerdefinierten Mirrors.

## Dokumentationsübersetzungen

Wir sammeln Übersetzungen unserer Dokumentation über [Crowdin](https://crowdin.com/project/electron). Aktuell akzeptieren wir Übersetzungen für Chinesisch, Französisch, Deutsch, Japanisch, Portugiesisch, Russisch und Spanisch.

## Mitwirken

Wenn du daran interessiert bist, Probleme zu melden, zu beheben oder direkt zum Code beizutragen, sieh dir bitte [CONTRIBUTING.md](CONTRIBUTING.md) an.

## Community

Informationen zum Melden von Fehlern, zur Hilfe, zu Drittanbieter-Tools und mehr findest du auf der [Community-Seite](https://www.electronjs.org/community).

## Lizenz

[MIT](https://github.com/electron/electron/blob/main/LICENSE)

Bei der Verwendung von Electron-Logos beachte bitte die [OpenJS Foundation Trademark Policy](https://trademark-policy.openjsf.org/).

