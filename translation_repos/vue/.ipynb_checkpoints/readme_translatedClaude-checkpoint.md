## Vue 2 hat das Ende seines Lebenszyklus erreicht

**Sie betrachten hier das inaktive Repository für Vue 2. Das aktiv gepflegte Repository für die neueste Version von Vue ist [vuejs/core](https://github.com/vuejs/core).**

Vue hat am 31. Dezember 2023 das Ende seines Lebenszyklus erreicht. Es erhält keine neuen Funktionen, Updates oder Fehlerbehebungen mehr. Es ist jedoch weiterhin über alle bestehenden Vertriebskanäle verfügbar (CDNs, Paketmanager, Github, etc.).

Wenn Sie ein neues Projekt starten, beginnen Sie bitte mit der neuesten Version von Vue (3.x). Wir empfehlen aktuellen Vue 2-Nutzern dringend ein Upgrade ([Leitfaden](https://v3-migration.vuejs.org/)), erkennen aber auch an, dass nicht alle Nutzer die Kapazität oder den Anreiz dafür haben. Wenn Sie bei Vue 2 bleiben müssen, aber auch Compliance- oder Sicherheitsanforderungen bezüglich nicht gewarteter Software haben, informieren Sie sich über [Vue 2 NES](https://www.herodevs.com/support/nes-vue?utm_source=vuejs-github&utm_medium=vue2-readme).

<p align="center"><a href="https://vuejs.org" target="_blank" rel="noopener noreferrer"><img width="100" src="https://vuejs.org/images/logo.png" alt="Vue Logo"></a></p>

<p align="center">
  <a href="https://circleci.com/gh/vuejs/vue/tree/dev"><img src="https://img.shields.io/circleci/project/github/vuejs/vue/dev.svg?sanitize=true" alt="Build Status"></a>
  <a href="https://codecov.io/github/vuejs/vue?branch=dev"><img src="https://img.shields.io/codecov/c/github/vuejs/vue/dev.svg?sanitize=true" alt="Coverage Status"></a>
  <a href="https://npmcharts.com/compare/vue?minimal=true"><img src="https://img.shields.io/npm/dm/vue.svg?sanitize=true" alt="Downloads"></a>
  <a href="https://www.npmjs.com/package/vue"><img src="https://img.shields.io/npm/v/vue.svg?sanitize=true" alt="Version"></a>
  <a href="https://www.npmjs.com/package/vue"><img src="https://img.shields.io/npm/l/vue.svg?sanitize=true" alt="License"></a>
  <a href="https://chat.vuejs.org/"><img src="https://img.shields.io/badge/chat-on%20discord-7289da.svg?sanitize=true" alt="Chat"></a>
</p>

## Sponsoren

Vue.js ist ein MIT-lizenziertes Open-Source-Projekt, dessen laufende Entwicklung vollständig durch die Unterstützung dieser großartigen [Unterstützer](https://github.com/vuejs/core/blob/main/BACKERS.md) ermöglicht wird. Wenn Sie sich ihnen anschließen möchten, erwägen Sie bitte die [Förderung der Vue-Entwicklung](https://vuejs.org/sponsor/).

<p align="center">
  <h3 align="center">Spezieller Sponsor</h3>
</p>

<p align="center">
  <a target="_blank" href="https://github.com/appwrite/appwrite">
  <img alt="spezieller Sponsor appwrite" src="https://sponsors.vuejs.org/images/appwrite.svg" width="300">
  </a>
</p>

<p align="center">
  <a target="_blank" href="https://vuejs.org/sponsor/">
    <img alt="Sponsoren" src="https://sponsors.vuejs.org/sponsors.svg?v3">
  </a>
</p>

---

## Einführung

Vue (ausgesprochen `/vjuː/`, wie view) ist ein **progressives Framework** zum Erstellen von Benutzeroberflächen. Es wurde von Grund auf so konzipiert, dass es schrittweise übernommen werden kann und sich je nach Anwendungsfall einfach zwischen einer Bibliothek und einem Framework skalieren lässt. Es besteht aus einer zugänglichen Kernbibliothek, die sich ausschließlich auf die View-Schicht konzentriert, und einem Ökosystem unterstützender Bibliotheken, die Ihnen helfen, die Komplexität in großen Single-Page-Anwendungen zu bewältigen.

#### Browser-Kompatibilität

Vue.js unterstützt alle Browser, die [ES5-konform](https://compat-table.github.io/compat-table/es5/) sind (IE8 und älter werden nicht unterstützt).

## Ökosystem

| Projekt               | Status                                                       | Beschreibung                                             |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------- |
| [vue-router]          | [![vue-router-status]][vue-router-package]                   | Routing für Single-Page-Anwendungen                      |
| [vuex]                | [![vuex-status]][vuex-package]                               | Großskaliges Zustandsmanagement                          |
| [vue-cli]             | [![vue-cli-status]][vue-cli-package]                         | Projekt-Scaffolding                                      |
| [vue-loader]          | [![vue-loader-status]][vue-loader-package]                   | Single File Component (`*.vue` Datei) Loader für webpack |
| [vue-server-renderer] | [![vue-server-renderer-status]][vue-server-renderer-package] | Server-seitiges Rendering                                |
| [vue-class-component] | [![vue-class-component-status]][vue-class-component-package] | TypeScript-Dekorator für klassenbasierte API             |
| [vue-rx]              | [![vue-rx-status]][vue-rx-package]                           | RxJS-Integration                                         |
| [vue-devtools]        | [![vue-devtools-status]][vue-devtools-package]               | Browser DevTools-Erweiterung                             |

[vue-router]: https://github.com/vuejs/vue-router
[vuex]: https://github.com/vuejs/vuex
[vue-cli]: https://github.com/vuejs/vue-cli
[vue-loader]: https://github.com/vuejs/vue-loader
[vue-server-renderer]: https://github.com/vuejs/vue/tree/dev/packages/vue-server-renderer
[vue-class-component]: https://github.com/vuejs/vue-class-component
[vue-rx]: https://github.com/vuejs/vue-rx
[vue-devtools]: https://github.com/vuejs/vue-devtools
[vue-router-status]: https://img.shields.io/npm/v/vue-router.svg
[vuex-status]: https://img.shields.io/npm/v/vuex.svg
[vue-cli-status]: https://img.shields.io/npm/v/@vue/cli.svg
[vue-loader-status]: https://img.shields.io/npm/v/vue-loader.svg
[vue-server-renderer-status]: https://img.shields.io/npm/v/vue-server-renderer.svg
[vue-class-component-status]: https://img.shields.io/npm/v/vue-class-component.svg
[vue-rx-status]: https://img.shields.io/npm/v/vue-rx.svg
[vue-devtools-status]: https://img.shields.io/chrome-web-store/v/nhdogjmejiglipccpnnnanhbledajbpd.svg
[vue-router-package]: https://npmjs.com/package/vue-router
[vuex-package]: https://npmjs.com/package/vuex
[vue-cli-package]: https://npmjs.com/package/@vue/cli
[vue-loader-package]: https://npmjs.com/package/vue-loader
[vue-server-renderer-package]: https://npmjs.com/package/vue-server-renderer
[vue-class-component-package]: https://npmjs.com/package/vue-class-component
[vue-rx-package]: https://npmjs.com/package/vue-rx
[vue-devtools-package]: https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd

## Dokumentation

Um [Live-Beispiele](https://v2.vuejs.org/v2/examples/) und Dokumentation einzusehen, besuchen Sie [vuejs.org](https://v2.vuejs.org).

## Fragen

Für Fragen und Support nutzen Sie bitte das [offizielle Forum](https://forum.vuejs.org) oder den [Community-Chat](https://chat.vuejs.org/). Die Issues-Liste dieses Repositories ist **ausschließlich** für Fehlerberichte und Feature-Anfragen gedacht.

## Issues

Bitte lesen Sie unbedingt die [Checkliste für Issue-Berichte](https://github.com/vuejs/vue/blob/dev/.github/CONTRIBUTING.md#issue-reporting-guidelines), bevor Sie ein Issue erstellen. Issues, die nicht den Richtlinien entsprechen, können sofort geschlossen werden.

## Changelog

Detaillierte Änderungen für jede Version sind in den [Release Notes](https://github.com/vuejs/vue/releases) dokumentiert.

## Bleiben Sie in Kontakt

- [Twitter](https://twitter.com/vuejs)
- [Blog](https://medium.com/the-vue-point)
- [Job Board](https://vuejobs.com/?ref=vuejs)

## Mitwirken

Bitte lesen Sie unbedingt den [Leitfaden zum Mitwirken](https://github.com/vuejs/vue/blob/dev/.github/CONTRIBUTING.md), bevor Sie einen Pull Request erstellen. Wenn Sie ein Vue-bezogenes Projekt/eine Komponente/ein Tool haben, fügen Sie es mit einem Pull Request zu [dieser kuratierten Liste](https://github.com/vuejs/awesome-vue) hinzu!

Vielen Dank an alle Menschen, die bereits zu Vue beigetragen haben!

<a href="https://github.com/vuejs/vue/graphs/contributors"><img src="https://opencollective.com/vuejs/contributors.svg?width=890" /></a>

## Lizenz

[MIT](https://opensource.org/licenses/MIT)

Copyright (c) 2013-heute, Yuxi (Evan) You