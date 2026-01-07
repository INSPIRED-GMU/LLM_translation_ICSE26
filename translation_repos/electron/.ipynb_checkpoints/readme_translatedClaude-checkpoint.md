[![Electron Logo](https://electronjs.org/images/electron-logo.svg)](https://electronjs.org)

[![GitHub Actions Build Status](https://github.com/electron/electron/actions/workflows/build.yml/badge.svg)](https://github.com/electron/electron/actions/workflows/build.yml)
[![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/4lggi9dpjc1qob7k/branch/main?svg=true)](https://ci.appveyor.com/project/electron-bot/electron-ljo26/branch/main)
[![Electron Discord Invite](https://img.shields.io/discord/745037351163527189?color=%237289DA&label=chat&logo=discord&logoColor=white)](https://discord.gg/electronjs)

:memo: Verfügbare Übersetzungen: 🇨🇳 🇧🇷 🇪🇸 🇯🇵 🇷🇺 🇫🇷 🇺🇸 🇩🇪.
Diese Dokumentation in anderen Sprachen finden Sie in unserem [Crowdin](https://crowdin.com/project/electron) Projekt.

Das Electron Framework ermöglicht es Ihnen, plattformübergreifende Desktop-Anwendungen mit JavaScript, HTML und CSS zu entwickeln. Es basiert auf [Node.js](https://nodejs.org/) und [Chromium](https://www.chromium.org) und wird von [Visual Studio Code](https://github.com/Microsoft/vscode/) und vielen anderen [Apps](https://electronjs.org/apps) verwendet.

Folgen Sie [@electronjs](https://twitter.com/electronjs) auf Twitter für wichtige Ankündigungen.

Dieses Projekt hält sich an den Contributor Covenant [Verhaltenskodex](https://github.com/electron/electron/tree/main/CODE_OF_CONDUCT.md). Durch Ihre Teilnahme wird von Ihnen erwartet, diesen Kodex einzuhalten. Bitte melden Sie inakzeptables Verhalten an [coc@electronjs.org](mailto:coc@electronjs.org).

## Installation

Um vorkompilierte Electron-Binärdateien zu installieren, verwenden Sie [`npm`](https://docs.npmjs.com/). Die bevorzugte Methode ist die Installation von Electron als Entwicklungsabhängigkeit in Ihrer App:

```sh
npm install electron --save-dev
```

Weitere Installationsoptionen und Fehlerbehebungstipps finden Sie unter [Installation](docs/tutorial/installation.md). Informationen zur Verwaltung von Electron-Versionen in Ihren Apps finden Sie unter [Electron-Versionierung](docs/tutorial/electron-versioning.md).

## Plattform-Unterstützung

Jede Electron-Version stellt Binärdateien für macOS, Windows und Linux bereit.

* macOS (Big Sur und höher): Electron bietet 64-bit Intel und Apple Silicon / ARM Binärdateien für macOS.
* Windows (Windows 10 und höher): Electron bietet `ia32` (`x86`), `x64` (`amd64`) und `arm64` Binärdateien für Windows. Windows auf ARM-Unterstützung wurde in Electron 5.0.8 hinzugefügt. Die Unterstützung für Windows 7, 8 und 8.1 wurde [in Electron 23 entfernt, entsprechend Chromiums Windows-Einstellungspolitik](https://www.electronjs.org/blog/windows-7-to-8-1-deprecation-notice).
* Linux: Die vorkompilierten Binärdateien von Electron werden auf Ubuntu 20.04 erstellt. Sie wurden auch auf folgenden Systemen getestet:
  * Ubuntu 18.04 und neuer
  * Fedora 32 und neuer
  * Debian 10 und neuer

## Schnellstart & Electron Fiddle

Nutzen Sie [`Electron Fiddle`](https://github.com/electron/fiddle), um kleine Electron-Experimente zu erstellen, auszuführen und zu paketieren, Codebeispiele für alle Electron-APIs zu sehen und verschiedene Electron-Versionen auszuprobieren. Es wurde entwickelt, um den Einstieg in Electron zu erleichtern.

Alternativ können Sie das [electron/electron-quick-start](https://github.com/electron/electron-quick-start) Repository klonen und ausführen, um eine minimale Electron-App in Aktion zu sehen:

```sh
git clone https://github.com/electron/electron-quick-start
cd electron-quick-start
npm install
npm start
```

## Ressourcen zum Lernen von Electron

* [electronjs.org/docs](https://electronjs.org/docs) - Die gesamte Electron-Dokumentation
* [electron/fiddle](https://github.com/electron/fiddle) - Ein Tool zum Erstellen, Ausführen und Paketieren kleiner Electron-Experimente
* [electron/electron-quick-start](https://github.com/electron/electron-quick-start) - Eine sehr einfache Electron-Starter-App
* [electronjs.org/community#boilerplates](https://electronjs.org/community#boilerplates) - Beispiel-Starter-Apps, erstellt von der Community

## Programmatische Verwendung

Die meisten Leute verwenden Electron über die Kommandozeile, aber wenn Sie `electron` innerhalb Ihrer **Node-App** (nicht Ihrer Electron-App) importieren, gibt es den Dateipfad zur Binärdatei zurück. Verwenden Sie dies, um Electron von Node-Skripten aus zu starten:

```javascript
const electron = require('electron')
const proc = require('node:child_process')

// wird etwas Ähnliches wie /Users/maf/.../Electron ausgeben
console.log(electron)

// Electron starten
const child = proc.spawn(electron)
```

### Mirrors

* [China](https://npmmirror.com/mirrors/electron/)

In den [Erweiterten Installationsanweisungen](https://www.electronjs.org/docs/latest/tutorial/installation#mirror) erfahren Sie, wie Sie einen benutzerdefinierten Mirror verwenden können.

## Dokumentationsübersetzungen

Wir crowdsourcen Übersetzungen für unsere Dokumentation über [Crowdin](https://crowdin.com/project/electron). Wir akzeptieren derzeit Übersetzungen für Chinesisch (Vereinfacht), Französisch, Deutsch, Japanisch, Portugiesisch, Russisch und Spanisch.

## Mitwirken

Wenn Sie daran interessiert sind, Probleme zu melden/zu beheben und direkt zum Code beizutragen, lesen Sie bitte [CONTRIBUTING.md](CONTRIBUTING.md) für weitere Informationen darüber, wonach wir suchen und wie Sie beginnen können.

## Community

Informationen zum Melden von Fehlern, zum Erhalten von Hilfe, zum Finden von Drittanbieter-Tools und Beispiel-Apps und mehr finden Sie auf der [Community-Seite](https://www.electronjs.org/community).

## Lizenz

[MIT](https://github.com/electron/electron/blob/main/LICENSE)

Bei der Verwendung von Electron-Logos beachten Sie bitte die [OpenJS Foundation Trademark Policy](https://trademark-policy.openjsf.org/).