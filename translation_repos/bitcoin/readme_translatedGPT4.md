Bitcoin Core Integrations-/Staging-Tree
=====================================

https://bitcoincore.org

Für eine sofort nutzbare, binäre Version der Bitcoin Core Software siehe
https://bitcoincore.org/en/download/.

Was ist Bitcoin Core?
---------------------

Bitcoin Core verbindet sich mit dem Peer-to-Peer-Netzwerk von Bitcoin, um Blöcke und Transaktionen herunterzuladen und vollständig zu validieren. Es enthält auch eine Wallet und eine grafische Benutzeroberfläche, die optional gebaut werden kann.

Weitere Informationen zu Bitcoin Core findest du im [doc-Ordner](/doc).

Lizenz
------

Bitcoin Core wird unter den Bedingungen der MIT-Lizenz veröffentlicht. Siehe [COPYING](COPYING) für weitere Informationen oder besuche https://opensource.org/licenses/MIT.

Entwicklungsprozess
-------------------

Der `master`-Branch wird regelmäßig gebaut (siehe `doc/build-*.md` für Anweisungen) und getestet, jedoch ist nicht garantiert, dass er vollkommen stabil ist. [Tags](https://github.com/bitcoin/bitcoin/tags) werden regelmäßig von Release-Branches erstellt, um neue offizielle, stabile Versionen von Bitcoin Core anzuzeigen.

Das Repository https://github.com/bitcoin-core/gui wird ausschließlich für die Entwicklung der GUI verwendet. Der `master`-Branch ist in allen Monotree-Repositories identisch. Es gibt keine Release-Branches oder Tags, daher bitte das Repository nur aus Entwicklungsgründen forken.

Der Beitrag-Workflow ist in [CONTRIBUTING.md](CONTRIBUTING.md) beschrieben, und hilfreiche Hinweise für Entwickler finden sich in [doc/developer-notes.md](doc/developer-notes.md).

Tests
-----

Tests und Code-Reviews sind der Engpass in der Entwicklung; wir erhalten mehr Pull Requests, als wir kurzfristig überprüfen und testen können. Bitte sei geduldig und hilf mit, indem du Pull Requests anderer testest. Denk daran, dass dies ein sicherheitskritisches Projekt ist, bei dem Fehler viel Geld kosten können.

### Automatisierte Tests

Entwickler werden dringend ermutigt, [Unit-Tests](src/test/README.md) für neuen Code zu schreiben und neue Unit-Tests für alten Code einzureichen. Unit-Tests können (vorausgesetzt, sie wurden nicht während der Build-System-Erstellung deaktiviert) mit `ctest` kompiliert und ausgeführt werden. Weitere Details zum Ausführen und Erweitern von Unit-Tests findest du in [/src/test/README.md](/src/test/README.md).

Es gibt auch [Regressions- und Integrationstests](/test), die in Python geschrieben sind. Diese Tests können (wenn die [Testabhängigkeiten](/test) installiert sind) mit folgendem Befehl ausgeführt werden: `build/test/functional/test_runner.py` (angenommen, `build` ist dein Build-Verzeichnis).

Die CI-Systeme (Continuous Integration) stellen sicher, dass jeder Pull Request für Windows, Linux und macOS gebaut wird und dass Unit-/Sanity-Tests automatisch ausgeführt werden.

### Manuelles QA-Testing (Qualitätssicherung)

Änderungen sollten von jemand anderem getestet werden als dem Entwickler, der den Code geschrieben hat. Dies ist besonders wichtig bei großen oder risikoreichen Änderungen. Es ist hilfreich, einen Testplan zur Pull-Request-Beschreibung hinzuzufügen, wenn das Testen der Änderungen nicht selbsterklärend ist.

Übersetzungen
--------------

Änderungen an Übersetzungen sowie neue Übersetzungen können über die [Transifex-Seite von Bitcoin Core](https://www.transifex.com/bitcoin/bitcoin/) eingereicht werden.

Übersetzungen werden regelmäßig von Transifex abgerufen und ins Git-Repository übernommen. Details dazu findest du im [Übersetzungsprozess](doc/translation_process.md).

**Wichtig**: Wir akzeptieren keine Übersetzungsänderungen als GitHub-Pull-Requests, da sie beim nächsten Abruf von Transifex automatisch überschrieben werden würden.

