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

[English](./README.md) | [简体中文](./README.zh-CN.md) | [日本語](./README.ja.md) | [Spanish](./README.es.md)

## Einführung

[vue-element-admin](https://panjiachen.github.io/vue-element-admin) ist eine produktionsreife Frontend-Lösung für Admin-Interfaces. Es basiert auf [vue](https://github.com/vuejs/vue) und verwendet das UI-Toolkit [element-ui](https://github.com/ElemeFE/element).

[vue-element-admin](https://panjiachen.github.io/vue-element-admin) basiert auf dem neuesten Entwicklungs-Stack von Vue und verfügt über eine integrierte i18n-Lösung, typische Templates für Unternehmensanwendungen und viele großartige Features. Es hilft Ihnen beim Aufbau großer und komplexer Single-Page-Anwendungen. Ich bin überzeugt, dass dieses Projekt Ihnen bei all Ihren Anforderungen helfen wird.

- [Vorschau](https://panjiachen.github.io/vue-element-admin)

- [Dokumentation](https://panjiachen.github.io/vue-element-admin-site/)

- [Gitter](https://gitter.im/vue-element-admin/discuss)

- [Spenden](https://panjiachen.github.io/vue-element-admin-site/donate/)

- [Wiki](https://github.com/PanJiaChen/vue-element-admin/wiki)

- [Gitee](https://panjiachen.gitee.io/vue-element-admin/) Für Benutzer in China verfügbare Online-Vorschau

**Ab Version `v4.1.0+` unterstützt der Standard-Master-Branch kein i18n mehr. Bitte verwenden Sie den [i18n Branch](https://github.com/PanJiaChen/vue-element-admin/tree/i18n), dieser wird mit den Master-Updates Schritt halten**

**Die aktuelle Version ist `v4.0+` basierend auf `vue-cli`. Wenn Sie ein Problem finden, erstellen Sie bitte ein [Issue](https://github.com/PanJiaChen/vue-element-admin/issues/new). Wenn Sie die alte Version verwenden möchten, können Sie zum Branch [tag/3.11.0](https://github.com/PanJiaChen/vue-element-admin/tree/tag/3.11.0) wechseln, dieser ist nicht von `vue-cli` abhängig**

**Dieses Projekt unterstützt keine älteren Browser (z.B. IE). Bitte fügen Sie selbst Polyfills hinzu.**

## Vorbereitung

Sie müssen [node](https://nodejs.org/) und [git](https://git-scm.com/) lokal installieren. Das Projekt basiert auf [ES2015+](https://es6.ruanyifeng.com/), [vue](https://cn.vuejs.org/index.html), [vuex](https://vuex.vuejs.org/zh-cn/), [vue-router](https://router.vuejs.org/zh-cn/), [vue-cli](https://github.com/vuejs/vue-cli), [axios](https://github.com/axios/axios) und [element-ui](https://github.com/ElemeFE/element). Alle Anfragedaten werden mit [Mock.js](https://github.com/nuysoft/Mock) simuliert.
Das Verständnis und Erlernen dieser Technologien im Voraus wird die Nutzung dieses Projekts erheblich erleichtern.

## Features

```
- Login / Logout

- Berechtigungsauthentifizierung
  - Seitenberechtigung
  - Direktive-Berechtigung
  - Berechtigungskonfigurationsseite
  - Zwei-Stufen-Login

- Multi-Umgebungs-Build
  - Entwicklung (dev)
  - sit
  - Staging-Test (stage)
  - Produktion (prod)

- Globale Features
  - I18n
  - Mehrere dynamische Themes
  - Dynamische Seitenleiste (unterstützt mehrstufiges Routing)
  - Dynamische Breadcrumbs
  - Tags-view (Tab-Seite unterstützt Rechtsklick-Operationen)
  - Svg Sprite
  - Mock-Daten
  - Vollbildschirm
  - Responsive Seitenleiste

- Editor
  - Rich Text Editor
  - Markdown Editor
  - JSON Editor

- Excel
  - Export Excel
  - Upload Excel
  - Excel-Visualisierung
  - Export zip

- Tabelle
  - Dynamische Tabelle
  - Drag & Drop Tabelle
  - Inline-Edit Tabelle

- Fehlerseiten
  - 401
  - 404

- Komponenten
  - Avatar Upload
  - Zurück nach oben
  - Drag Dialog
  - Drag Select
  - Drag Kanban
  - Drag Liste
  - SplitPane
  - Dropzone
  - Sticky
  - CountTo

- Fortgeschrittene Beispiele
- Fehlerprotokollierung
- Dashboard
- Führungsseite
- ECharts
- Zwischenablage
- Markdown zu HTML
```

## Erste Schritte

```bash
# Projekt klonen
git clone https://github.com/PanJiaChen/vue-element-admin.git

# Projektverzeichnis betreten
cd vue-element-admin

# Abhängigkeiten installieren
npm install

# Entwicklungsserver starten
npm run dev
```

Dies öffnet automatisch http://localhost:9527

## Build

```bash
# Build für Testumgebung
npm run build:stage

# Build für Produktionsumgebung
npm run build:prod
```

## Erweitert

```bash
# Vorschau der Release-Umgebung
npm run preview

# Vorschau der Release-Umgebung + statische Ressourcenanalyse
npm run preview -- --report

# Code-Format-Überprüfung
npm run lint

# Code-Format-Überprüfung und automatische Behebung
npm run lint -- --fix
```

Weitere Informationen finden Sie in der [Dokumentation](https://panjiachen.github.io/vue-element-admin-site/guide/essentials/deploy.html)

## Änderungsprotokoll

Detaillierte Änderungen für jedes Release sind in den [Release Notes](https://github.com/PanJiaChen/vue-element-admin/releases) dokumentiert.

## Online-Demo

[Vorschau](https://panjiachen.github.io/vue-element-admin)

## Browser-Unterstützung

Moderne Browser und Internet Explorer 10+.

| [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/edge/edge_48x48.png" alt="IE / Edge" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)</br>IE / Edge | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/firefox/firefox_48x48.png" alt="Firefox" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)</br>Firefox | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png" alt="Chrome" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)</br>Chrome | [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/safari/safari_48x48.png" alt="Safari" width="24px" height="24px" />](https://godban.github.io/browsers-support-badges/)</br>Safari |
| --------- | --------- | --------- | --------- |
| IE10, IE11, Edge | letzte 2 Versionen | letzte 2 Versionen | letzte 2 Versionen |

## Lizenz

[MIT](https://github.com/PanJiaChen/vue-element-admin/blob/master/LICENSE)

Copyright (c) 2017-heute PanJiaChen