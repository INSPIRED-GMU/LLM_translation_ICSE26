[![Express Logo](https://i.cloudup.com/zfY6lL7eFa-3000x3000.png)](https://expressjs.com/)

**Schnelles, minimalistisches und flexibles Web-Framework für [Node.js](https://nodejs.org).**

**Dieses Projekt hat einen [Code of Conduct][].**

## Inhaltsverzeichnis

* [Installation](#Installation)
* [Funktionen](#Funktionen)
* [Dokumentation & Community](#Dokumentation--Community)
* [Schnellstart](#Schnellstart)
* [Tests ausführen](#Tests-ausführen)
* [Philosophie](#Philosophie)
* [Beispiele](#Beispiele)
* [Beiträge zu Express](#Beiträge-zu-Express)
* [TC (Technisches Komitee)](#TC-Technisches-Komitee)
* [Triager](#Triager)
* [Lizenz](#Lizenz)

[![NPM-Version][npm-version-image]][npm-url]
[![NPM-Downloads][npm-downloads-image]][npm-downloads-url]
[![OpenSSF Scorecard Badge][ossf-scorecard-badge]][ossf-scorecard-visualizer]

```js
import express from 'express'

const app = express()

app.get('/', (req, res) => {
  res.send('Hallo Welt')
})

app.listen(3000)
```

## Installation

Dies ist ein [Node.js](https://nodejs.org/en/) Modul, das über das
[npm-Registry](https://www.npmjs.com/) verfügbar ist.

Bevor Sie installieren, [laden Sie Node.js herunter und installieren Sie es](https://nodejs.org/en/download/).
Node.js 18 oder höher wird benötigt.

Wenn dies ein komplett neues Projekt ist, stellen Sie sicher, dass Sie zuerst eine `package.json`-Datei mit dem
[`npm init`-Befehl](https://docs.npmjs.com/creating-a-package-json-file) erstellen.

Die Installation erfolgt mit dem
[`npm install`-Befehl](https://docs.npmjs.com/getting-started/installing-npm-packages-locally):

```bash
npm install express
```

Folgen Sie [unserer Installationsanleitung](https://expressjs.com/en/starter/installing.html)
weitere Informationen.

## Funktionen

  * Robustes Routing
  * Fokus auf hohe Leistung
  * Sehr hohe Testabdeckung
  * HTTP-Hilfsmittel (Weiterleitung, Caching usw.)
  * View-System mit Unterstützung für über 14 Template-Engines
  * Inhaltsverhandlung
  * Ausführbares Tool für schnelles Erstellen von Anwendungen

## Dokumentation & Community

  * [Website und Dokumentation](https://expressjs.com/) - [[Website-Repo](https://github.com/expressjs/expressjs.com)]
  * [GitHub-Organisation](https://github.com/expressjs) für offizielle Middleware & Module
  * [GitHub Discussions](https://github.com/expressjs/discussions) für Diskussionen zur Entwicklung und Nutzung von Express

**TIPP:** Lesen Sie unbedingt den [Migrationsleitfaden zu v5](https://expressjs.com/en/guide/migrating-5).

## Schnellstart

Der schnellste Weg, um mit Express zu beginnen, ist die Nutzung des ausführbaren Tools [`express(1)`](https://github.com/expressjs/generator) zur Generierung einer Anwendung:

Installieren Sie das ausführbare Tool. Die Hauptversion des Tools wird mit der von Express übereinstimmen:

```bash
npm install -g express-generator@4
```

Erstellen Sie die App:

```bash
express /tmp/foo && cd /tmp/foo
```

Installieren Sie die Abhängigkeiten:

```bash
npm install
```

Starten Sie den Server:

```bash
npm start
```

Betrachten Sie die Website unter: http://localhost:3000

## Philosophie

Die Philosophie von Express ist es, kleine, robuste Werkzeuge für HTTP-Server bereitzustellen, was es zu einer großartigen Lösung für Single-Page-Anwendungen, Websites, Hybride oder öffentliche HTTP-APIs macht.

Express zwingt Sie nicht, eine spezifische ORM oder Template-Engine zu verwenden. Mit Unterstützung für über
14 Template-Engines via [@ladjs/consolidate](https://github.com/ladjs/consolidate)
können Sie schnell Ihr perfektes Framework erstellen.

## Beispiele

Um die Beispiele anzusehen, klonen Sie das Express-Repository:

```bash
git clone https://github.com/expressjs/express.git --depth 1 && cd express
```

Installieren Sie dann die Abhängigkeiten:

```bash
npm install
```

Führen Sie dann das gewünschte Beispiel aus:

```bash
node examples/content-negotiation
```

## Beiträge

[![Linux-Build][github-actions-ci-image]][github-actions-ci-url]
[![Testabdeckung][coveralls-image]][coveralls-url]

Das Express.js-Projekt heißt alle konstruktiven Beiträge willkommen. Beiträge nehmen viele Formen an,
von Code für Bugfixes und Erweiterungen über Ergänzungen und Korrekturen in der Dokumentation bis hin zu zusätzlichen Tests, dem Triagieren eingehender Pull Requests und Issues und mehr!

Lesen Sie den [Beitragsleitfaden](Contributing.md) für weitere technische Details.

### Sicherheitsprobleme

Wenn Sie eine Sicherheitslücke in Express entdecken, lesen Sie bitte die [Sicherheitsrichtlinien und Verfahren](Security.md).

### Tests ausführen

Um die Testsuite auszuführen, installieren Sie zuerst die Abhängigkeiten:

```bash
npm install
```

Führen Sie dann `npm test` aus:

```bash
npm test
```

## Personen

Der ursprüngliche Autor von Express ist [TJ Holowaychuk](https://github.com/tj).

[Liste aller Mitwirkenden](https://github.com/expressjs/express/graphs/contributors)

### TC (Technisches Komitee)

* [UlisesGascon](https://github.com/UlisesGascon) - **Ulises Gascón** (er/ihm)
* [jonchurch](https://github.com/jonchurch) - **Jon Church**
* [wesleytodd](https://github.com/wesleytodd) - **Wes Todd**
* [LinusU](https://github.com/LinusU) - **Linus Unnebäck**
* [blakeembrey](https://github.com/blakeembrey) - **Blake Embrey**
* [sheplu](https://github.com/sheplu) - **Jean Burellier**
* [crandmck](https://github.com/crandmck) - **Rand McKinney**
* [ctcpip](https://github.com/ctcpip) - **Chris de Almeida**

<details>
<summary>TC Emeriti Mitglieder</summary>

#### TC Emeriti Mitglieder

  * [dougwilson](https://github.com/dougwilson) - **Douglas Wilson**
  * [hacksparrow](https://github.com/hacksparrow) - **Hage Yaapa**
  * [jonathanong](https://github.com/jonathanong) - **jongleberry**
  * [niftylettuce](https://github.com/niftylettuce) - **niftylettuce**
  * [troygoode](https://github.com/troygoode) - **Troy Goode**
</details>

### Triager

* [aravindvnair99](https://github.com/aravindvnair99) - **Aravind Nair**
* [bjohansebas](https://github.com/bjohansebas) - **Sebastian Beltran**
* [carpasse](https://github.com/carpasse) - **Carlos Serrano**
* [CBID2](https://github.com/CBID2) - **Christine Belzie**
* [enyoghasim](https://github.com/enyoghasim) - **David Enyoghasim**
* [UlisesGascon](https://github.com/UlisesGascon) - **Ulises Gascón** (er/ihm)
* [mertcanaltin](https://github.com/mertcanaltin) - **Mert Can Altin**
* [0ss](https://github.com/0ss) - **Salah**
* [import-brain](https://github.com/import-brain) - **Eric Cheng** (er/ihm)
* [3imed-jaberi](https://github.com/3imed-jaberi) - **Imed Jaberi**
* [dakshkhetan](https://github.com/dakshkhetan) - **Daksh Khetan** (er/ihm)
* [lucasraziel](https://github.com/lucasraziel) - **Lucas Soares Do Rego**
* [IamLizu](https://github.com/IamLizu) - **S M Mahmudul Hasan** (er/ihm)
* [Sushmeet](https://github.com/Sushmeet) - **Sushmeet Sunger**
* [rxmarbles](https://github.com/rxmarbles) **Rick Markins** (Er/ihm)

<details>
<summary>Emeriti Triager Mitglieder</summary>

#### Emeriti Triager Mitglieder

  * [AuggieH](https://github.com/AuggieH) - **Auggie Hudak**
  * [G-Rath](https://github.com/G-Rath) - **Gareth Jones**
  * [MohammadXroid](https://github.com/MohammadXroid) - **Mohammad Ayashi**
  * [NawafSwe](https://github.com/NawafSwe) - **Nawaf Alsharqi**
  * [NotMoni](https://github.com/NotMoni) - **Moni**
  * [VigneshMurugan](https://github.com/VigneshMurugan) - **Vignesh Murugan**
  * [davidmashe](https://github.com/davidmashe) - **David Ashe**
  * [digitaIfabric](https://github.com/digitaIfabric) - **David**
  * [e-l-i-s-e](https://github.com/e-l-i-s-e) - **Elise Bonner**
  * [fed135](https://github.com/fed135) - **Frederic Charette**
  * [firmanJS](https://github.com/firmanJS) - **Firman Abdul Hakim**
  * [getspooky](https://github.com/getspooky) - **Yasser Ameur**
  * [ghinks](https://github.com/ghinks) - **Glenn**
  * [ghousemohamed](https://github.com/ghousemohamed) - **Ghouse Mohamed**
  * [gireeshpunathil](https://github.com/gireeshpunathil) - **Gireesh Punathil**
  * [jake32321](https://github.com/jake32321) - **Jake Reed**
  * [jonchurch](https://github.com/jonchurch) - **Jon Church**
  * [lekanikotun](https://github.com/lekanikotun) - **Troy Goode**
  * [marsonya](https://github.com/marsonya) - **Lekan Ikotun**
  * [mastermatt](https://github.com/mastermatt) - **Matt R. Wilson**
  * [maxakuru](https://github.com/maxakuru) - **Max Edell**
  * [mlrawlings](https://github.com/mlrawlings) - **Michael Rawlings**
  * [rodion-arr](https://github.com/rodion-arr) - **Rodion Abdurakhimov**
  * [sheplu](https://github.com/sheplu) - **Jean Burellier**
  * [tarunyadav1](https://github.com/tarunyadav1) - **Tarun yadav**
  * [tunniclm](https://github.com/tunniclm) - **Mike Tunnicliffe**
</details>

## Lizenz

  [MIT](LICENSE)

[coveralls-image]: https://badgen.net/coveralls/c/github/expressjs/express/master
[coveralls-url]: https://coveralls.io/r/expressjs/express?branch=master
[github-actions-ci-image]: https://badgen.net/github/checks/expressjs/express/master?label=CI
[github-actions-ci-url]: https://github.com/expressjs/express/actions/workflows/ci.yml
[npm-downloads-image]: https://badgen.net/npm/dm/express
[npm-downloads-url]: https://npmcharts.com/compare/express?minimal=true
[npm-url]: https://npmjs.org/package/express
[npm-version-image]: https://badgen.net/npm/v/express
[ossf-scorecard-badge]: https://api.scorecard.dev/projects/github.com/expressjs/express/badge
[ossf-scorecard-visualizer]: https://ossf.github.io/scorecard-visualizer/#/projects/github.com/expressjs/express
[Code of Conduct]: https://github.com/expressjs/express/blob/master/Code-Of-Conduct.md
