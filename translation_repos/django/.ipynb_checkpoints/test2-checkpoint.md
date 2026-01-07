[![Express Logo](https://i.cloudup.com/zfY6lL7eFa-3000x3000.png)](https://expressjs.com/)

**Schnelles, unvoreingenommenes, minimalistisches Web-Framework für [Node.js](https://nodejs.org).**

**Dieses Projekt hat einen [Verhaltenskodex][].**

## Inhaltsverzeichnis
* [Installation](#Installation)
* [Funktionen](#Funktionen)
* [Dokumentation & Community](#docs--community)
* [Schnellstart](#Schnellstart)
* [Tests ausführen](#Tests ausführen)
* [Philosophie](#Philosophie)
* [Beispiele](#Beispiele)
* [Beitrag zu Express](#Beitrag)
* [TC (Technischer Ausschuss)](#tc-technical-committee)
* [Triager](#triager)
* [Lizenz](#license)

[![NPM-Version][npm-version-image]][npm-url]
[![NPM-Downloads][npm-downloads-image]][npm-downloads-url]
[![OpenSSF Scorecard-Badge][ossf-scorecard-badge]][ossf-scorecard-visualizer]

```js
import express from 'express'

const app = express()

app.get('/', (req, res) => {
res.send('Hello World')
})

app.listen(3000)
```

## Installation

Dies ist ein [Node.js](https://nodejs.org/en/)-Modul, das über die [npm-Registrierung](https://www.npmjs.com/) verfügbar ist.

Laden Sie vor der Installation Node.js herunter und installieren Sie es.

Node.js 18 oder höher ist erforderlich.

Bei einem neuen Projekt erstellen Sie bitte zunächst eine „package.json“-Datei mit dem Befehl „npm init“.

Die Installation erfolgt mit dem Befehl „npm install“:

bash
npm install express


Weitere Informationen finden Sie in unserer Installationsanleitung.

## Funktionen
* Robustes Routing
* Fokus auf hohe Performance
* Sehr hohe Testabdeckung
* HTTP-Hilfsprogramme (Umleitung, Caching usw.)
* Ansichtssystem mit Unterstützung für mehr als 14 Template-Engines
* Inhaltsverhandlung
* Ausführbare Datei zur schnellen Anwendungsgenerierung

## Dokumentation & Community
* [Website und Dokumentation](https://expressjs.com/) - [[Website-Repository](https://github.com/expressjs/expressjs.com)]
* [GitHub-Organisation](https://github.com/expressjs) für offizielle Middleware und Module
* [GitHub-Diskussionen](https://github.com/expressjs/discussions) für Diskussionen zur Entwicklung und Nutzung von Express

**PROTIPP** Lesen Sie unbedingt den [Migrationsleitfaden zu v5](https://expressjs.com/en/guide/migrating-5)

## Schnellstart
Der schnellste Einstieg in Express ist die Verwendung der ausführbaren Datei [`express(1)`](https://github.com/expressjs/generator), um eine Anwendung wie unten gezeigt zu generieren:

Installieren Sie die ausführbare Datei. Die Hauptversion der ausführbaren Datei entspricht der von Express:

```bash
npm install -g express-generator@4
```

Erstellen Sie die Anwendung:

```bash
express /tmp/foo && cd /tmp/foo
```

Installieren Sie Abhängigkeiten:

```bash
npm install
```

Starten Sie den Server:

```bash
npm start
```
Besuchen Sie die Website unter: http://localhost:3000

## Philosophie
Die Philosophie von Express besteht darin, kleine, robuste Tools für HTTP-Server bereitzustellen. Dies macht es zu einer hervorragenden Lösung für Single-Page-Anwendungen, Websites, Hybride oder öffentliche HTTP-APIs.
Express zwingt Sie nicht zur Verwendung eines bestimmten ORM oder einer bestimmten Template-Engine. Mit Unterstützung für über 14 Template-Engines über [@ladjs/consolidate](https://github.com/ladjs/consolidate)
erstellen Sie schnell Ihr perfektes Framework.

## Beispiele

Um die Beispiele anzuzeigen, klonen Sie das Express-Repository:

```bash
git clone https://github.com/expressjs/express.git --depth 1 && cd express
```

Installieren Sie anschließend die Abhängigkeiten:

```bash
npm install
```

Führen Sie anschließend das gewünschte Beispiel aus:

```bash
node examples/content-negotiation
```

## Mitwirken

[![Linux Build][github-actions-ci-image]][github-actions-ci-url]
[![Test Coverage][coveralls-image]][coveralls-url]

Das Express.js-Projekt freut sich über alle konstruktiven Beiträge. Beiträge können in vielerlei Form erfolgen, von Code für Fehlerbehebungen und Verbesserungen über Ergänzungen und Fehlerbehebungen bis hin zu Dokumentation, zusätzlichen Tests, der Sichtung eingehender Pull Requests und Probleme und vielem mehr!

Weitere technische Informationen zum Beitragen finden Sie im [Leitfaden für Beiträge](Contributing.md).

### Sicherheitsprobleme

Wenn Sie eine Sicherheitslücke in Express entdecken, lesen Sie bitte die [Sicherheitsrichtlinien und -verfahren](Security.md).

### Tests ausführen

Um die Testsuite auszuführen, installieren Sie zunächst die Abhängigkeiten:

```bash
npm install
```

Führen Sie anschließend ````bash
npm test` aus:

```bash
npm test
```

## Personen
Der ursprüngliche Autor von Express ist [TJ Holowaychuk](https://github.com/tj)

[Liste aller Mitwirkenden](https://github.com/expressjs/express/graphs/contributors)

### TC (Technischer Ausschuss)

* [UlisesGascon](https://github.com/UlisesGascon) - **Ulises Gascón** (er/ihn)
* [jonchurch](https://github.com/jonchurch) - **Jon Church**
* [wesleytodd](https://github.com/wesleytodd) - **Wes Todd**
* [LinusU](https://github.com/LinusU) – **Linus Unnebäck**
* [blakeembrey](https://github.com/blakeembrey) – **Blake Embrey**
* [sheplu](https://github.com/sheplu) – **Jean Burellier**
* [crandmck](https://github.com/crandmck) – **Rand McKinney**