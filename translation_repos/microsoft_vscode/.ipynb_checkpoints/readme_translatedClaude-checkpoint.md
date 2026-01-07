# Visual Studio Code - Open Source ("Code - OSS")

[![Feature Requests](https://img.shields.io/github/issues/microsoft/vscode/feature-request.svg)](https://github.com/microsoft/vscode/issues?q=is%3Aopen+is%3Aissue+label%3Afeature-request+sort%3Areactions-%2B1-desc)
[![Bugs](https://img.shields.io/github/issues/microsoft/vscode/bug.svg)](https://github.com/microsoft/vscode/issues?utf8=✓&q=is%3Aissue+is%3Aopen+label%3Abug)
[![Gitter](https://img.shields.io/badge/chat-on%20gitter-yellow.svg)](https://gitter.im/Microsoft/vscode)

## Das Repository

Dieses Repository ("`Code - OSS`") ist der Ort, an dem wir (Microsoft) das [Visual Studio Code](https://code.visualstudio.com) Produkt gemeinsam mit der Community entwickeln. Wir arbeiten hier nicht nur an Code und Problemen, sondern veröffentlichen auch unsere [Roadmap](https://github.com/microsoft/vscode/wiki/Roadmap), [monatlichen Iterationspläne](https://github.com/microsoft/vscode/wiki/Iteration-Plans) und unsere [Endgame-Pläne](https://github.com/microsoft/vscode/wiki/Running-the-Endgame). Dieser Quellcode steht allen unter der Standard-[MIT-Lizenz](https://github.com/microsoft/vscode/blob/main/LICENSE.txt) zur Verfügung.

## Visual Studio Code

<p align="center">
  <img alt="VS Code in Aktion" src="https://user-images.githubusercontent.com/35271042/118224532-3842c400-b438-11eb-923d-a5f66fa6785a.png">
</p>

[Visual Studio Code](https://code.visualstudio.com) ist eine Distribution des `Code - OSS` Repositories mit Microsoft-spezifischen Anpassungen, die unter einer traditionellen [Microsoft-Produktlizenz](https://code.visualstudio.com/License/) veröffentlicht wird.

[Visual Studio Code](https://code.visualstudio.com) verbindet die Einfachheit eines Code-Editors mit den Funktionen, die Entwickler für ihren grundlegenden Bearbeiten-Erstellen-Debuggen-Zyklus benötigen. Es bietet umfassende Unterstützung für Code-Bearbeitung, -Navigation und -Verständnis sowie leichtgewichtiges Debugging, ein reichhaltiges Erweiterungsmodell und eine unkomplizierte Integration mit bestehenden Werkzeugen.

Visual Studio Code wird monatlich mit neuen Funktionen und Fehlerkorrekturen aktualisiert. Sie können es für Windows, macOS und Linux auf der [Visual Studio Code-Website](https://code.visualstudio.com/Download) herunterladen. Um täglich die neuesten Versionen zu erhalten, installieren Sie den [Insiders Build](https://code.visualstudio.com/insiders).

## Mitwirken

Es gibt viele Möglichkeiten, an diesem Projekt mitzuwirken, zum Beispiel:

* [Fehler und Funktionswünsche einreichen](https://github.com/microsoft/vscode/issues) und bei der Überprüfung helfen
* [Quellcode-Änderungen überprüfen](https://github.com/microsoft/vscode/pulls)
* Die [Dokumentation](https://github.com/microsoft/vscode-docs) überprüfen und Pull Requests für alles von Tippfehlern bis hin zu zusätzlichen und neuen Inhalten erstellen

Wenn Sie daran interessiert sind, Probleme zu beheben und direkt zum Code beizutragen,
lesen Sie bitte das Dokument [How to Contribute](https://github.com/microsoft/vscode/wiki/How-to-Contribute), das Folgendes behandelt:

* [Aus dem Quellcode erstellen und ausführen](https://github.com/microsoft/vscode/wiki/How-to-Contribute)
* [Der Entwicklungsworkflow, einschließlich Debugging und Ausführen von Tests](https://github.com/microsoft/vscode/wiki/How-to-Contribute#debugging)
* [Coding-Richtlinien](https://github.com/microsoft/vscode/wiki/Coding-Guidelines)
* [Pull Requests einreichen](https://github.com/microsoft/vscode/wiki/How-to-Contribute#pull-requests)
* [Ein Problem zum Bearbeiten finden](https://github.com/microsoft/vscode/wiki/How-to-Contribute#where-to-contribute)
* [Zu Übersetzungen beitragen](https://aka.ms/vscodeloc)

## Feedback

* Stellen Sie eine Frage auf [Stack Overflow](https://stackoverflow.com/questions/tagged/vscode)
* [Neue Funktion vorschlagen](CONTRIBUTING.md)
* [Beliebte Funktionswünsche](https://github.com/microsoft/vscode/issues?q=is%3Aopen+is%3Aissue+label%3Afeature-request+sort%3Areactions-%2B1-desc) mit Ihrer Stimme unterstützen
* [Ein Problem melden](https://github.com/microsoft/vscode/issues)
* Verbinden Sie sich mit der Erweiterungs-Entwickler-Community auf [GitHub Discussions](https://github.com/microsoft/vscode-discussions/discussions) oder [Slack](https://aka.ms/vscode-dev-community)
* Folgen Sie [@code](https://twitter.com/code) und lassen Sie uns wissen, was Sie denken!

In unserem [Wiki](https://github.com/microsoft/vscode/wiki/Feedback-Channels) finden Sie eine Beschreibung dieser Kanäle und Informationen zu weiteren verfügbaren Community-getriebenen Kanälen.

## Verwandte Projekte

Viele der Kernkomponenten und Erweiterungen von VS Code befinden sich in eigenen Repositories auf GitHub. Zum Beispiel sind die Repositories für den [Node Debug Adapter](https://github.com/microsoft/vscode-node-debug) und den [Mono Debug Adapter](https://github.com/microsoft/vscode-mono-debug) voneinander getrennt. Eine vollständige Liste finden Sie auf der Seite [Verwandte Projekte](https://github.com/microsoft/vscode/wiki/Related-Projects) in unserem [Wiki](https://github.com/microsoft/vscode/wiki).

## Mitgelieferte Erweiterungen

VS Code enthält eine Reihe von eingebauten Erweiterungen im Ordner [extensions](extensions), einschließlich Grammatiken und Snippets für viele Sprachen. Erweiterungen, die umfangreiche Sprachunterstützung (Code-Vervollständigung, Gehe zu Definition) für eine Sprache bieten, haben das Suffix `language-features`. Zum Beispiel bietet die `json`-Erweiterung Färbung für `JSON` und die `json-language-features`-Erweiterung bietet umfangreiche Sprachunterstützung für `JSON`.

## Entwicklungscontainer

Dieses Repository enthält einen Visual Studio Code Dev Containers / GitHub Codespaces Entwicklungscontainer.

* Für [Dev Containers](https://aka.ms/vscode-remote/download/containers) verwenden Sie den Befehl **Dev Containers: Clone Repository in Container Volume...**, der ein Docker-Volume für bessere Festplatten-I/O unter macOS und Windows erstellt.
  * Wenn Sie bereits VS Code und Docker installiert haben, können Sie auch [hier](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/vscode) klicken, um loszulegen. Dies veranlasst VS Code, die Dev Containers-Erweiterung bei Bedarf automatisch zu installieren, den Quellcode in ein Container-Volume zu klonen und einen Dev Container zur Verwendung zu starten.

* Für Codespaces installieren Sie die [GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces) Erweiterung in VS Code und verwenden den Befehl **Codespaces: Create New Codespace**.

Docker / der Codespace sollte mindestens **4 Kerne und 6 GB RAM (8 GB empfohlen)** haben, um den vollständigen Build ausführen zu können. Weitere Informationen finden Sie in der [Development Container README](.devcontainer/README.md).

## Verhaltenskodex

Dieses Projekt hat den [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/) übernommen. Weitere Informationen finden Sie in den [Häufig gestellten Fragen zum Verhaltenskodex](https://opensource.microsoft.com/codeofconduct/faq/) oder kontaktieren Sie [opencode@microsoft.com](mailto:opencode@microsoft.com) bei weiteren Fragen oder Kommentaren.

## Lizenz

Copyright (c) Microsoft Corporation. Alle Rechte vorbehalten.

Lizenziert unter der [MIT](LICENSE.txt)-Lizenz.