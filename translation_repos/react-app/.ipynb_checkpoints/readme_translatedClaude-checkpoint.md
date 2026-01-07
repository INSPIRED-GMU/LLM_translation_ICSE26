# Create React App [![Build & Test](https://github.com/facebook/create-react-app/actions/workflows/build-and-test.yml/badge.svg?branch=main)](https://github.com/facebook/create-react-app/actions/workflows/build-and-test.yml) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/facebook/create-react-app/blob/main/CONTRIBUTING.md)

<img alt="Logo" align="right" src="https://create-react-app.dev/img/logo.svg" width="20%" />

Erstellen Sie React-Apps ohne Build-Konfiguration.

- [Eine App erstellen](#eine-app-erstellen) – So erstellen Sie eine neue App.
- [Benutzerhandbuch](https://facebook.github.io/create-react-app/) – So entwickeln Sie Apps, die mit Create React App erstellt wurden.

Create React App funktioniert auf macOS, Windows und Linux.<br>
Wenn etwas nicht funktioniert, [erstellen Sie bitte ein Issue](https://github.com/facebook/create-react-app/issues/new).<br>
Bei Fragen oder wenn Sie Hilfe benötigen, fragen Sie bitte in den [GitHub Discussions](https://github.com/facebook/create-react-app/discussions).

## Schnellübersicht

```sh
npx create-react-app my-app
cd my-app
npm start
```

Wenn Sie `create-react-app` zuvor global über `npm install -g create-react-app` installiert haben, empfehlen wir, das Paket mit `npm uninstall -g create-react-app` oder `yarn global remove create-react-app` zu deinstallieren, um sicherzustellen, dass npx immer die neueste Version verwendet.

_([npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) wird mit npm 5.2+ und höher mitgeliefert, siehe [Anweisungen für ältere npm-Versionen](https://gist.github.com/gaearon/4064d3c23a77c74a3614c498a8bb1c5f))_

Öffnen Sie dann [http://localhost:3000/](http://localhost:3000/), um Ihre App zu sehen.<br>
Wenn Sie bereit für die Produktionsbereitstellung sind, erstellen Sie ein minimiertes Bundle mit `npm run build`.

<p align='center'>
<img src='https://cdn.jsdelivr.net/gh/facebook/create-react-app@27b42ac7efa018f2541153ab30d63180f5fa39e0/screencast.svg' width='600' alt='npm start'>
</p>

### Sofort loslegen

Sie müssen Tools wie webpack oder Babel **nicht** installieren oder konfigurieren.<br>
Sie sind vorkonfiguriert und verborgen, damit Sie sich auf den Code konzentrieren können.

Erstellen Sie ein Projekt und los geht's.

## Eine App erstellen

**Sie benötigen Node 14.0.0 oder eine neuere Version auf Ihrem lokalen Entwicklungsrechner** (aber nicht auf dem Server). Wir empfehlen die Verwendung der neuesten LTS-Version. Sie können [nvm](https://github.com/creationix/nvm#installation) (macOS/Linux) oder [nvm-windows](https://github.com/coreybutler/nvm-windows#node-version-manager-nvm-for-windows) verwenden, um zwischen verschiedenen Node-Versionen für verschiedene Projekte zu wechseln.

Um eine neue App zu erstellen, können Sie eine der folgenden Methoden wählen:

### npx

```sh
npx create-react-app my-app
```

_([npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) ist ein Paket-Runner-Tool, das mit npm 5.2+ und höher mitgeliefert wird, siehe [Anweisungen für ältere npm-Versionen](https://gist.github.com/gaearon/4064d3c23a77c74a3614c498a8bb1c5f))_

### npm

```sh
npm init react-app my-app
```

_`npm init <initializer>` ist in npm 6+ verfügbar_

### Yarn

```sh
yarn create react-app my-app
```

_[`yarn create <starter-kit-package>`](https://yarnpkg.com/lang/en/docs/cli/create/) ist in Yarn 0.25+ verfügbar_

Es wird ein Verzeichnis namens `my-app` im aktuellen Ordner erstellt.<br>
In diesem Verzeichnis wird die anfängliche Projektstruktur generiert und die transitiven Abhängigkeiten werden installiert:

```
my-app
├── README.md
├── node_modules
├── package.json
├── .gitignore
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
└── src
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    ├── logo.svg
    └── serviceWorker.js
    └── setupTests.js
```

Keine Konfiguration oder komplizierte Ordnerstrukturen, nur die Dateien, die Sie zum Erstellen Ihrer App benötigen.<br>
Nach Abschluss der Installation können Sie Ihren Projektordner öffnen:

```sh
cd my-app
```

Im neu erstellten Projekt können Sie einige integrierte Befehle ausführen:

### `npm start` oder `yarn start`

Startet die App im Entwicklungsmodus.<br>
Öffnen Sie [http://localhost:3000](http://localhost:3000), um sie im Browser anzuzeigen.

Die Seite wird automatisch neu geladen, wenn Sie Änderungen am Code vornehmen.<br>
Build-Fehler und Lint-Warnungen werden in der Konsole angezeigt.

<p align='center'>
<img src='https://cdn.jsdelivr.net/gh/marionebl/create-react-app@9f6282671c54f0874afd37a72f6689727b562498/screencast-error.svg' width='600' alt='Build errors'>
</p>

### `npm test` oder `yarn test`

Startet den Test-Watcher im interaktiven Modus.<br>
Standardmäßig werden Tests ausgeführt, die sich auf seit dem letzten Commit geänderte Dateien beziehen.

[Mehr über das Testen lesen.](https://facebook.github.io/create-react-app/docs/running-tests)

### `npm run build` oder `yarn build`

Erstellt die App für die Produktion im `build`-Ordner.<br>
Es bündelt React im Produktionsmodus und optimiert den Build für die beste Performance.

Der Build wird minimiert und die Dateinamen enthalten Hashes.<br>

Ihre App ist bereit für die Bereitstellung.

## Benutzerhandbuch

Detaillierte Anweisungen zur Verwendung von Create React App und viele Tipps finden Sie in der [Dokumentation](https://facebook.github.io/create-react-app/).

## Wie aktualisiere ich auf neue Versionen?

Bitte lesen Sie das [Benutzerhandbuch](https://facebook.github.io/create-react-app/docs/updating-to-new-releases) für diese und andere Informationen.

## Philosophie

- **Eine Abhängigkeit:** Es gibt nur eine Build-Abhängigkeit. Es verwendet webpack, Babel, ESLint und andere großartige Projekte, bietet aber eine kohärente kuratierte Erfahrung darüber.

- **Keine Konfiguration erforderlich:** Sie müssen nichts konfigurieren. Eine vernünftig gute Konfiguration sowohl für Entwicklungs- als auch für Produktions-Builds wird für Sie übernommen, damit Sie sich auf das Schreiben von Code konzentrieren können.

- **Keine Bindung:** Sie können jederzeit zu einer benutzerdefinierten Einrichtung "auswerfen" (eject). Führen Sie einen einzigen Befehl aus, und alle Konfigurations- und Build-Abhängigkeiten werden direkt in Ihr Projekt verschoben, sodass Sie genau dort weitermachen können, wo Sie aufgehört haben.

## Was ist enthalten?

Ihre Umgebung wird alles haben, was Sie zum Erstellen einer modernen Single-Page React-App benötigen:

- Unterstützung für React, JSX, ES6, TypeScript und Flow-Syntax.
- Zusätzliche Sprachfunktionen über ES6 hinaus wie der Objekt-Spread-Operator.
- Autoprefixed CSS, sodass Sie keine `-webkit-` oder andere Präfixe benötigen.
- Ein schneller interaktiver Unit-Test-Runner mit eingebauter Unterstützung für Coverage-Reporting.
- Ein Live-Entwicklungsserver, der vor häufigen Fehlern warnt.
- Ein Build-Skript zum Bündeln von JS, CSS und Bildern für die Produktion, mit Hashes und Sourcemaps.
- Ein [Service Worker](https://developers.google.com/web/fundamentals/getting-started/primers/service-workers) mit Offline-First-Ansatz und ein [Web App Manifest](https://developers.google.com/web/fundamentals/engage-and-retain/web-app-manifest/), die alle [Progressive Web App](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)-Kriterien erfüllen. (_Hinweis: Die Verwendung des Service Workers ist ab `react-scripts@2.0.0` und höher optional_)
- Problemlose Updates für die oben genannten Tools mit einer einzigen Abhängigkeit.

In [diesem Leitfaden](https://github.com/nitishdayal/cra_closer_look) finden Sie einen Überblick darüber, wie diese Tools zusammenpassen.

Der Kompromiss ist, dass **diese Tools vorkonfiguriert sind, um auf eine bestimmte Weise zu arbeiten**. Wenn Ihr Projekt mehr Anpassung benötigt, können Sie ["auswerfen"](https://facebook.github.io/create-react-app/docs/available-scripts#npm-run-eject) und anpassen, aber dann müssen Sie diese Konfiguration selbst pflegen.

## Beliebte Alternativen

Create React App ist ideal für:

- **React lernen** in einer komfortablen und funktionsreichen Entwicklungsumgebung.
- **Neue Single-Page React-Anwendungen starten.**
- **Beispiele erstellen** mit React für Ihre Bibliotheken und Komponenten.

Hier sind einige häufige Fälle, in denen Sie etwas anderes ausprobieren möchten:

- Wenn Sie **React ausprobieren** möchten, ohne Hunderte von transitiven Build-Tool-Abhängigkeiten, erwägen Sie [die Verwendung einer einzelnen HTML-Datei oder einer Online-Sandbox](https://reactjs.org/docs/getting-started.html#try-react).

- Wenn Sie **React-Code in ein serverseitiges Template-Framework** wie Rails, Django oder Symfony integrieren müssen oder wenn Sie **keine Single-Page-App erstellen**, erwägen Sie [nwb](https://github.com/insin/nwb) oder [Neutrino](https://neutrino.js.org/), die flexibler sind. Speziell für Rails können Sie [Rails Webpacker](https://github.com/rails/webpacker) verwenden. Für Symfony versuchen Sie [Symfony's webpack Encore](https://symfony.com/doc/current/frontend/encore/reactjs.html).

- Wenn Sie eine **React-Komponente veröffentlichen** müssen, kann [nwb](https://github.com/insin/nwb) [dies auch tun](https://github.com/insin/nwb#react-components-and-libraries), ebenso wie [Neutrinos react-components preset](https://neutrino.js.org/packages/react-components/).

- Wenn Sie **Server-Rendering** mit React und Node.js machen möchten, schauen Sie sich [Next.js](https://nextjs.org/) oder [Razzle](https://github.com/jaredpalmer/razzle) an. Create React App ist Backend-agnostisch und produziert nur statische HTML/JS/CSS-Bundles.

- Wenn Ihre Website **überwiegend statisch** ist (zum Beispiel ein Portfolio oder ein Blog), erwägen Sie [Gatsby](https://www.gatsbyjs.org/) oder [Next.js](https://nextjs.org/). Im Gegensatz zu Create React App rendert Gatsby die Website zur Build-Zeit in HTML. Next.js unterstützt sowohl Server-Rendering als auch Pre-Rendering.

- Wenn Sie schließlich **mehr Anpassung** benötigen, schauen Sie sich [Neutrino](https://neutrino.js.org/) und dessen [React preset](https://neutrino.js.org/packages/react/) an.

Alle oben genannten Tools können mit wenig oder gar keiner Konfiguration arbeiten.

Wenn Sie den Build lieber selbst konfigurieren möchten, folgen Sie [diesem Leitfaden](https://reactjs.org/docs/add-react-to-a-website.html).

## React Native

Suchen Sie nach etwas Ähnlichem, aber für React Native?<br>
Schauen Sie sich [Expo CLI](https://github.com/expo/expo-cli) an.

## Mitwirken

Wir würden uns sehr über Ihre Hilfe bei `create-react-app` freuen! Weitere Informationen darüber, wonach wir suchen und wie Sie beginnen können, finden Sie in [CONTRIBUTING.md](CONTRIBUTING.md).

## Create React App unterstützen

Create React App ist ein von der Community gepflegtes Projekt und alle Mitwirkenden sind Freiwillige. Wenn Sie die zukünftige Entwicklung von Create React App unterstützen möchten, erwägen Sie bitte eine Spende an unser [Open Collective](https://opencollective.com/create-react-app).

## Danksagungen

Dieses Projekt existiert dank all der Menschen, die [beitragen](CONTRIBUTING.md).<br>
<a href="https://github.com/facebook/create-react-app/graphs/contributors"><img src="https://opencollective.com/create-react-app/contributors.svg?width=890&button=false" /></a>

Danke an [Netlify](https://www.netlify.com/) für das Hosting unserer Dokumentation.

## Würdigungen

Wir sind den Autoren bestehender verwandter Projekte für ihre Ideen und Zusammenarbeit dankbar:

- [@eanplatter](https://github.com/eanplatter)
- [@insin](https://github.com/insin)
- [@mxstbr