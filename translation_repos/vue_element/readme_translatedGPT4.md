<p align="center">
  <img width="320" src="https://wpimg.wallstcn.com/ecc53a42-d79b-42e2-8852-5126b810a4c8.svg">
</p>

<p align="center">
  <a href="https://github.com/vuejs/vue">
    <img src="https://img.shields.io/badge/vue-2.6.10-brightgreen.svg" alt="vue">
  </a>
  <a href="https://github.com/ElemeFE/element">
    <img src="https://img.shields.io/badge/element--ui-2.7.0-brightgreen.svg" alt="element-ui">
  </a>
  <a href="https://travis-ci.org/PanJiaChen/vue-element-admin" rel="nofollow">
    <img src="https://travis-ci.org/PanJiaChen/vue-element-admin.svg?branch=master" alt="Build Status">
  </a>
  <a href="https://github.com/PanJiaChen/vue-element-admin/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/mashape/apistatus.svg" alt="license">
  </a>
  <a href="https://github.com/PanJiaChen/vue-element-admin/releases">
    <img src="https://img.shields.io/github/release/PanJiaChen/vue-element-admin.svg" alt="GitHub release">
  </a>
  <a href="https://gitter.im/vue-element-admin/discuss">
    <img src="https://badges.gitter.im/Join%20Chat.svg" alt="gitter">
  </a>
  <a href="https://panjiachen.github.io/vue-element-admin-site/donate">
    <img src="https://img.shields.io/badge/%24-donate-ff69b4.svg" alt="donate">
  </a>
</p>

Englisch | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Spanisch](./README.es.md)

## Einführung

[vue-element-admin](https://panjiachen.github.io/vue-element-admin) ist eine produktionsreife Frontend-Lösung für Admin-Oberflächen. Es basiert auf [vue](https://github.com/vuejs/vue) und verwendet das UI-Toolkit [element-ui](https://github.com/ElemeFE/element).

[vue-element-admin](https://panjiachen.github.io/vue-element-admin) basiert auf dem neuesten Entwicklungsstack von Vue, bietet eine integrierte i18n-Lösung, typische Templates für Unternehmensanwendungen und viele weitere tolle Features. Es hilft Ihnen, große und komplexe Single-Page-Anwendungen zu erstellen. Egal welche Anforderungen Sie haben, dieses Projekt wird Ihnen helfen.

- [Vorschau](https://panjiachen.github.io/vue-element-admin)

- [Dokumentation](https://panjiachen.github.io/vue-element-admin-site/)

- [Gitter](https://gitter.im/vue-element-admin/discuss)

- [Spenden](https://panjiachen.github.io/vue-element-admin-site/donate/)

- [Wiki](https://github.com/PanJiaChen/vue-element-admin/wiki)

- [Gitee](https://panjiachen.gitee.io/vue-element-admin/) 国内用户可访问该地址在线预览

- Basisvorlage wird empfohlen: [vue-admin-template](https://github.com/PanJiaChen/vue-admin-template)
- Desktop: [electron-vue-admin](https://github.com/PanJiaChen/electron-vue-admin)
- Typescript: [vue-typescript-admin-template](https://github.com/Armour/vue-typescript-admin-template) (Dank an: [@Armour](https://github.com/Armour))
- [awesome-project](https://github.com/PanJiaChen/vue-element-admin/issues/2312)

**Ab der Version `v4.1.0+` wird der Standard-Master-Branch i18n nicht unterstützen. Bitte verwenden Sie den [i18n Branch](https://github.com/PanJiaChen/vue-element-admin/tree/i18n), der mit den Master-Updates synchronisiert wird.**

**Die aktuelle Version ist `v4.0+`, gebaut auf `vue-cli`. Falls Sie ein Problem finden, erstellen Sie bitte ein [Issue](https://github.com/PanJiaChen/vue-element-admin/issues/new). Falls Sie die alte Version verwenden möchten, wechseln Sie bitte zum Branch [tag/3.11.0](https://github.com/PanJiaChen/vue-element-admin/tree/tag/3.11.0), der nicht von `vue-cli` abhängt.**

**Dieses Projekt unterstützt keine veralteten Browser (z. B. IE). Bitte fügen Sie Polyfills selbst hinzu.**

## Vorbereitung

Sie müssen [node](https://nodejs.org/) und [git](https://git-scm.com/) lokal installieren. Das Projekt basiert auf [ES2015+](https://es6.ruanyifeng.com/), [vue](https://cn.vuejs.org/index.html), [vuex](https://vuex.vuejs.org/zh-cn/), [vue-router](https://router.vuejs.org/zh-cn/), [vue-cli](https://github.com/vuejs/vue-cli), [axios](https://github.com/axios/axios) und [element-ui](https://github.com/ElemeFE/element). Alle Anfragedaten werden mit [Mock.js](https://github.com/nuysoft/Mock) simuliert. Das Verständnis und das Lernen dieser Technologien im Voraus wird die Nutzung dieses Projekts erheblich erleichtern.

[![Bearbeiten auf CodeSandbox](https://codesandbox.io/static/img/play-codesandbox.svg)](https://codesandbox.io/s/github/PanJiaChen/vue-element-admin/tree/CodeSandbox)

<p align="center">
  <img width="900" src="https://wpimg.wallstcn.com/a5894c1b-f6af-456e-82df-1151da0839bf.png">
</p>

## Sponsoren

Werden Sie Sponsor und erhalten Sie Ihr Logo in unserer README auf GitHub mit einem Link zu Ihrer Website. [[Sponsor werden]](https://www.patreon.com/panjiachen)

### Akveo
<a href="https://store.akveo.com/products/vue-java-admin-dashboard-spring?utm_campaign=akveo_store-Vue-Vue_demo%2Fgithub&utm_source=vue_admin&utm_medium=referral&utm_content=github_banner"><img width="500px" src="https://raw.githubusercontent.com/PanJiaChen/vue-element-admin-site/master/docs/.vuepress/public/images/vue-java-banner.png" /></a><p>Erhalten Sie ein Java-Backend für Vue-Admin mit 20 % Rabatt für 39 $ mit dem Gutscheincode SWB0RAZPZR1M</p>

### Flatlogic

<a href="https://flatlogic.com/admin-dashboards?from=vue-element-admin"><img width="150px" src="https://wpimg.wallstcn.com/9c0b719b-5551-4c1e-b776-63994632d94a.png" /></a><p>Admin-Dashboard-Vorlagen erstellt mit Vue, React und Angular.</p>

## Funktionen

```
- Login / Logout

- Berechtigungsauthentifizierung
  - Seitenberechtigung
  - Direktivenberechtigung
  - Berechtigungskonfigurationsseite
  - Zwei-Schritt-Login

- Multi-Environment-Build
  - Entwicklung (dev)
  - sit
  - Staging-Test (stage)
  - Produktion (prod)

- Globale Funktionen
  - I18n
  - Mehrere dynamische Themes
  - Dynamische Seitenleiste (unterstützt mehrstufige Routen)
  - Dynamische Breadcrumbs
  - Tags-Ansicht (Tab-Unterstützung mit Rechtsklick-Operationen)
  - Svg Sprite
  - Mock-Daten
  - Vollbildmodus
  - Responsive Seitenleiste

- Editor
  - Rich-Text-Editor
  - Markdown-Editor
  - JSON-Editor

- Excel
  - Export Excel
  - Upload Excel
  - Visualisierung Excel
  - Export zip

- Tabelle
  - Dynamische Tabelle
  - Drag-and-Drop-Tabelle
  - Inline-Bearbeitungstabelle

- Fehlerseiten
  - 401
  - 404

- Komponenten
  - Avatar-Upload
  - Nach oben scrollen
  - Dialog ziehen
  - Auswahl ziehen
  - Kanban ziehen
  - Liste ziehen
  - SplitPane
  - Dropzone
  - Sticky
  - CountTo

- Erweitertes Beispiel
- Fehlerprotokoll
- Dashboard
- Leitfaden
- ECharts
- Zwischenablage
- Markdown zu HTML
``

