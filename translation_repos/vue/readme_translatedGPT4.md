## Vue 2 hat das Ende seiner Lebensdauer erreicht

**Sie betrachten das nun inaktive Repository für Vue 2. Das aktiv gewartete Repository für die neueste Version von Vue ist [vuejs/core](https://github.com/vuejs/core).**

Vue hat am 31. Dezember 2023 das Ende seiner Lebensdauer erreicht. Es erhält keine neuen Funktionen, Updates oder Fehlerbehebungen mehr. Es ist jedoch weiterhin über alle bestehenden Distributionskanäle (CDNs, Paketmanager, GitHub usw.) verfügbar.

Wenn Sie ein neues Projekt starten, verwenden Sie bitte die neueste Version von Vue (3.x). Wir empfehlen auch allen aktuellen Nutzern von Vue 2, ein Upgrade vorzunehmen ([Anleitung](https://v3-migration.vuejs.org/)), erkennen jedoch an, dass nicht alle Nutzer die Kapazitäten oder Anreize haben, dies zu tun. Wenn Sie bei Vue 2 bleiben müssen, aber Compliance- oder Sicherheitsanforderungen bezüglich nicht mehr gewarteter Software haben, schauen Sie sich [Vue 2 NES](https://www.herodevs.com/support/nes-vue?utm_source=vuejs-github&utm_medium=vue2-readme) an.

<p align="center"><a href="https://vuejs.org" target="_blank" rel="noopener noreferrer"><img width="100" src="https://vuejs.org/images/logo.png" alt="Vue-Logo"></a></p>

<p align="center">
  <a href="https://circleci.com/gh/vuejs/vue/tree/dev"><img src="https://img.shields.io/circleci/project/github/vuejs/vue/dev.svg?sanitize=true" alt="Build Status"></a>
  <a href="https://codecov.io/github/vuejs/vue?branch=dev"><img src="https://img.shields.io/codecov/c/github/vuejs/vue/dev.svg?sanitize=true" alt="Coverage Status"></a>
  <a href="https://npmcharts.com/compare/vue?minimal=true"><img src="https://img.shields.io/npm/dm/vue.svg?sanitize=true" alt="Downloads"></a>
  <a href="https://www.npmjs.com/package/vue"><img src="https://img.shields.io/npm/v/vue.svg?sanitize=true" alt="Version"></a>
  <a href="https://www.npmjs.com/package/vue"><img src="https://img.shields.io/npm/l/vue.svg?sanitize=true" alt="Lizenz"></a>
  <a href="https://chat.vuejs.org/"><img src="https://img.shields.io/badge/chat-on%20discord-7289da.svg?sanitize=true" alt="Chat"></a>
</p>

## Sponsoren

Vue.js ist ein unter der MIT-Lizenz stehendes Open-Source-Projekt, dessen kontinuierliche Entwicklung ausschließlich durch die Unterstützung dieser großartigen [Unterstützer](https://github.com/vuejs/core/blob/main/BACKERS.md) möglich ist. Wenn Sie sich ihnen anschließen möchten, ziehen Sie bitte in Betracht, die Entwicklung von Vue [zu sponsern](https://vuejs.org/sponsor/).

<p align="center">
  <h3 align="center">Spezieller Sponsor</h3>
</p>

<p align="center">
  <a target="_blank" href="https://github.com/appwrite/appwrite">
  <img alt="Spezial-Sponsor Appwrite" src="https://sponsors.vuejs.org/images/appwrite.svg" width="300">
  </a>
</p>

<p align="center">
  <a target="_blank" href="https://vuejs.org/sponsor/">
    <img alt="Sponsoren" src="https://sponsors.vuejs.org/sponsors.svg?v3">
  </a>
</p>

---

## Einführung

Vue (ausgesprochen `/vjuː/`, wie "view") ist ein **progressives Framework** zum Erstellen von Benutzeroberflächen. Es wurde von Grund auf so entwickelt, dass es schrittweise anpassbar ist und je nach Anwendungsfall leicht zwischen einer Bibliothek und einem Framework skaliert werden kann. Es besteht aus einer zugänglichen Kernbibliothek, die sich nur auf die Ansichtsebene konzentriert, und einem Ökosystem von Unterstützungsbibliotheken, die Ihnen helfen, die Komplexität großer Single-Page-Anwendungen zu bewältigen.

#### Browserkompatibilität

Vue.js unterstützt alle [ES5-konformen](https://compat-table.github.io/compat-table/es5/) Browser (IE8 und ältere Versionen werden nicht unterstützt).

## Ökosystem

| Projekt                | Status                                                       | Beschreibung                                             |
| ---------------------  | ------------------------------------------------------------ | ------------------------------------------------------- |
| [vue-router]           | [![vue-router-status]][vue-router-package]                   | Routing für Single-Page-Anwendungen                     |
| [vuex]                 | [![vuex-status]][vuex-package]                               | Zustandsverwaltung für große Anwendungen               |
| [vue-cli]              | [![vue-cli-status]][vue-cli-package]                         | Projektgerüst                                           |
| [vue-loader]           | [![vue-loader-status]][vue-loader-package]                   | Loader für Single File Component (`*.vue`-Dateien) für Webpack |
| [vue-server-renderer]  | [![vue-server-renderer-status]][vue-server-renderer-package] | Serverseitiges Rendering                                 |
| [vue-class-component]  | [![vue-class-component-status]][vue-class-component-package] | TypeScript-Dekorator für eine klassenbasierte API        |
| [vue-rx]               | [![vue-rx-status]][vue-rx-package]                           | RxJS-Integration                                        |
| [vue-devtools]         | [![vue-devtools-status]][vue-devtools-package]               | Browser-DevTools-Erweiterung                            |

[vue-router]: https://github.com/vuejs/vue-router
[vuex]: https://github.com/vuejs/vuex
[vue-cli]: https://github.com/vuejs/vue-cli
[vue-loader]: https://github.com/vuejs/vue-loader
[vue-server-renderer]: https://github.com/vuejs/vue/tree/dev/packages/vue-server-renderer
[vue-class-component]: https://github.com/vuejs/vue-class-component
[vue-rx]: https://github.com/vuejs/vue-rx
[vue-devtools]: https://github.com/vuejs/vue-devtools

## Dokumentation

Schauen Sie sich [Live-Beispiele](https://v2.vuejs.org/v2/examples/) und die Dokumentation auf [vuejs.org](https://v2.vuejs.org) an.

## Fragen

Für Fragen und Unterstützung verwenden Sie bitte [das offizielle Forum](https://forum.vuejs.org) oder den [Community-Chat](https://chat.vuejs.org/). Die Issue-Liste dieses Repositories ist **ausschließlich** für Fehlerberichte und Funktionsanfragen gedacht.

## Probleme

Bitte lesen Sie die [Richtlinien für die Problemberichterstattung](https://github.com/vuejs/vue/blob/dev/.github/CONTRIBUTING.md#issue-reporting-guidelines), bevor Sie ein Problem öffnen. Probleme, die nicht den Richtlinien entsprechen, können sofort geschlossen werden.

## Changelog

Detaillierte Änderungen für jede Version sind in den [Release Notes](https://github.com/vuejs/vue/releases) dokumentiert.

## Bleiben Sie in Kontakt

- [Twitter](https://twitter.com/vuejs)
- [Blog](https://medium.com/the-vue-point)
- [Job Board](https://vuejobs.com/?ref=vuejs)

## Beitrag leisten

Bitte lesen Sie die [Beitragsrichtlinien](https://github.com/vuejs/vue/blob/dev/.github/CONTRIBUTING.md), bevor Sie einen Pull Request erstellen. Wenn Sie ein Vue-bezogenes Projekt/Komponente/Tool haben, fügen Sie es mit einem Pull Request zu [dieser kuratierten Liste](https://github.com/vuejs/awesome-vue) hinzu!

Vielen Dank an alle, die bereits zu Vue beigetragen haben!

<a href="https://github.com/vuejs/vue/graphs/contributors"><img src="https://opencollective.com/vuejs/contributors.svg?width=890" /></a>

## Lizenz

[MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2013-present, Yuxi (Evan) You
