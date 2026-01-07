# Create React App [![Build & Test](https://github.com/facebook/create-react-app/actions/workflows/build-and-test.yml/badge.svg?branch=main)](https://github.com/facebook/create-react-app/actions/workflows/build-and-test.yml) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-green.svg)](https://github.com/facebook/create-react-app/blob/main/CONTRIBUTING.md)

<img alt="Logo" align="right" src="https://create-react-app.dev/img/logo.svg" width="20%" />

Erstelle React-Apps ohne Build-Konfiguration.

- [Erstellen einer App](#erstellen-einer-app) – Wie man eine neue App erstellt.
- [Benutzerhandbuch](https://facebook.github.io/create-react-app/) – Wie man Apps entwickelt, die mit Create React App erstellt wurden.

Create React App funktioniert unter macOS, Windows und Linux.<br>
Falls etwas nicht funktioniert, [erstellen Sie ein Issue](https://github.com/facebook/create-react-app/issues/new).<br>
Falls Sie Fragen haben oder Hilfe benötigen, stellen Sie diese bitte in [GitHub Discussions](https://github.com/facebook/create-react-app/discussions).

## Schneller Überblick

```sh
npx create-react-app my-app
cd my-app
npm start
```

Falls Sie `create-react-app` zuvor global über `npm install -g create-react-app` installiert haben, empfehlen wir Ihnen, das Paket mit `npm uninstall -g create-react-app` oder `yarn global remove create-react-app` zu deinstallieren, um sicherzustellen, dass npx immer die neueste Version verwendet.

_([npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) ist ab npm 5.2+ verfügbar, siehe [Anweisungen für ältere npm-Versionen](https://gist.github.com/gaearon/4064d3c23a77c74a3614c498a8bb1c5f))_

Öffnen Sie dann [http://localhost:3000/](http://localhost:3000/), um Ihre App zu sehen.<br>
Wenn Sie bereit sind, die App in Produktion zu bringen, erstellen Sie mit `npm run build` ein minifiziertes Bundle.

<p align='center'>
<img src='https://cdn.jsdelivr.net/gh/facebook/create-react-app@27b42ac7efa018f2541153ab30d63180f5fa39e0/screencast.svg' width='600' alt='npm start'>
</p>

### Sofort loslegen

Sie **müssen nicht** Tools wie webpack oder Babel installieren oder konfigurieren.<br>
Diese sind vorkonfiguriert und verborgen, damit Sie sich auf den Code konzentrieren können.

Erstellen Sie ein Projekt und legen Sie los.

## Erstellen einer App

**Sie benötigen Node 14.0.0 oder eine neuere Version auf Ihrem lokalen Entwicklungsrechner** (aber nicht auf dem Server). Wir empfehlen die neueste LTS-Version. Sie können [nvm](https://github.com/creationix/nvm#installation) (macOS/Linux) oder [nvm-windows](https://github.com/coreybutler/nvm-windows#node-version-manager-nvm-for-windows) verwenden, um zwischen Node-Versionen für verschiedene Projekte zu wechseln.

Um eine neue App zu erstellen, können Sie eine der folgenden Methoden wählen:

### npx

```sh
npx create-react-app my-app
```

_([npx](https://medium.com/@maybekatz/introducing-npx-an-npm-package-runner-55f7d4bd282b) ist ein Tool, das mit npm 5.2+ verfügbar ist, siehe [Anweisungen für ältere npm-Versionen](https://gist.github.com/gaearon/4064d3c23a77c74a3614c498a8bb1c5f))_

### npm

```sh
npm init react-app my-app
```

_`npm init <initializer>` ist ab npm 6+ verfügbar_

### Yarn

```sh
yarn create react-app my-app
```

_[`yarn create <starter-kit-package>`](https://yarnpkg.com/lang/en/docs/cli/create/) ist ab Yarn 0.25+ verfügbar_

Es wird ein Verzeichnis namens `my-app` im aktuellen Ordner erstellt.<br>
Innerhalb dieses Verzeichnisses wird die anfängliche Projektstruktur generiert und die transitiven Abhängigkeiten installiert:

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

Keine Konfiguration oder komplizierte Ordnerstrukturen, nur die Dateien, die Sie benötigen, um Ihre App zu erstellen.<br>
Nach Abschluss der Installation können Sie Ihren Projektordner öffnen:

```sh
cd my-app
```

Innerhalb des neu erstellten Projekts können Sie einige eingebaute Befehle ausführen:

### `npm start` oder `yarn start`

Startet die App im Entwicklungsmodus.<br>
Öffnen Sie [http://localhost:3000](http://localhost:3000), um sie im Browser anzuzeigen.

Die Seite wird automatisch neu geladen, wenn Sie Änderungen am Code vornehmen.<br>
Sie werden Build-Fehler und Lint-Warnungen in der Konsole sehen.

<p align='center'>
<img src='https://cdn.jsdelivr.net/gh/marionebl/create-react-app@9f6282671c54f0874afd37a72f6689727b562498/screencast-error.svg' width='600' alt='Build errors'>
</p>

### `npm test` oder `yarn test`

Startet den Test-Watcher im interaktiven Modus.<br>
Standardmäßig werden Tests ausgeführt, die mit Dateien zusammenhängen, die seit dem letzten Commit geändert wurden.

[Lesen Sie mehr über das Testen.](https://facebook.github.io/create-react-app/docs/running-tests)

### `npm run build` oder `yarn build`

Erstellt die App für die Produktion im `build`-Ordner.<br>
Es bündelt React korrekt im Produktionsmodus und optimiert den Build für die beste Performance.

Der Build ist minifiziert und die Dateinamen enthalten Hashes.<br>

Ihre App ist bereit für die Bereitstellung.

## Benutzerhandbuch

Detaillierte Anweisungen zur Nutzung von Create React App und viele Tipps finden Sie in [der Dokumentation](https://facebook.github.io/create-react-app/).

## Wie wird auf neue Versionen aktualisiert?

Bitte lesen Sie [das Benutzerhandbuch](https://facebook.github.io/create-react-app/docs/updating-to-new-releases) für diese und andere Informationen.

## Philosophie

- **Eine Abhängigkeit:** Es gibt nur eine Build-Abhängigkeit. Es verwendet webpack, Babel, ESLint und andere fantastische Projekte, bietet jedoch eine zusammenhängende, kuratierte Erfahrung darüber hinaus.

- **Keine Konfiguration erforderlich:** Sie müssen nichts konfigurieren. Eine angemessene Konfiguration sowohl für Entwicklungs- als auch für Produktions-Builds wird für Sie übernommen, sodass Sie sich auf das Schreiben von Code konzentrieren können.

- **Keine Bindung:** Sie können jederzeit zu einem benutzerdefinierten Setup "ausscheren". Führen Sie einen einzigen Befehl aus, und alle Konfigurations- und Build-Abhängigkeiten werden direkt in Ihr Projekt übernommen, sodass Sie genau dort weitermachen können, wo Sie aufgehört haben.

## Was ist enthalten?

Ihre Umgebung wird alles haben, was Sie benötigen, um eine moderne Single-Page-React-App zu erstellen:

- React-, JSX-, ES6-, TypeScript- und Flow-Syntax-Unterstützung.
- Sprachergänzungen über ES6 hinaus wie den Objekt-Spread-Operator.
- Autoprefixed CSS, sodass Sie nicht `-webkit-` oder andere Prefixe benötigen.
- Ein schneller, interaktiver Unit-Test-Runner mit integrierter Unterstützung für Berichterstattung.
- Ein Live-Entwicklungsserver, der vor häufigen Fehlern warnt.
- Ein Build-Skript zum Bündeln von JS, CSS und Bildern für die Produktion, mit Hashes und Sourcemaps.
- Ein Offline-First-[Service-Worker](https://developers.google.com/web/fundamentals/getting-started/primers/service-workers) und ein [Web-App-Manifest](https://developers.google.com/web/fundamentals/engage-and-retain/web-app-manifest/), das alle [Progressive Web App](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)-Kriterien erfüllt. (_Hinweis: Die Nutzung des Service Workers ist ab `react-scripts@2.0.0` optional)_
- Mühelose Updates für die oben genannten Tools mit einer einzigen Abhängigkeit.

Sehen Sie sich [diesen Leitfaden](https://github.com/nitishdayal/cra_closer_look) für einen Überblick darüber an, wie diese Tools zusammenpassen.

Der Kompromiss ist, dass **diese Tools vorkonfiguriert sind, um auf eine bestimmte Weise zu arbeiten**. Falls Ihr Projekt mehr Anpassung erfordert, können Sie ["ausscheren"](https://facebook.github.io/create-react-app/docs/available-scripts#npm-run-eject) und es anpassen, aber dann müssen Sie diese Konfiguration selbst pflegen.

## Beitragen

Wir würden uns über Ihre Hilfe bei `create-react-app` freuen! Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für weitere Informationen dazu, wonach wir suchen und wie Sie anfangen können.

## Create React App unterstützen

Create React App ist ein Community-Projekt und alle Mitwirkenden sind Freiwillige. Wenn Sie die zukünftige Entwicklung von Create React App unterstützen möchten, sollten Sie überlegen, an unser [Open Collective](https://opencollective.com/create-react-app) zu spenden.

## Credits

Dieses Projekt existiert dank all der Menschen, die [beitragen](CONTRIBUTING.md).<br>
<a href="https://github.com/facebook/create-react-app/graphs/contributors"><img src="https://opencollective.com/create-react-app/contributors.svg?width=890&button=false" /></a>

Vielen Dank an [Netlify](https://www.netlify.com/) für das Hosting unserer Dokumentation.

## Lizenz

Create React App ist Open-Source-Software und unter [MIT lizenziert](https://github.com/facebook/create-react-app/blob/main/LICENSE). Das Create React App-Logo ist unter einer [Creative Commons Attribution 4.0 International Lizenz](https://creativecommons.org/licenses/by/4.0/) lizenziert.

