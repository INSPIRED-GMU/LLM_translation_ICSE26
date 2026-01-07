Bitcoin Core Integrations-/Staging-Baum
=====================================

https://bitcoincore.org

Für eine sofort nutzbare Binärversion der Bitcoin Core Software, siehe
https://bitcoincore.org/en/download/.

Was ist Bitcoin Core?
---------------------

Bitcoin Core verbindet sich mit dem Bitcoin Peer-to-Peer-Netzwerk, um Blöcke und Transaktionen herunterzuladen und vollständig zu validieren. Es enthält auch eine Wallet und eine grafische Benutzeroberfläche, die optional erstellt werden können.

Weitere Informationen über Bitcoin Core finden Sie im [doc Ordner](/doc).

Lizenz
-------

Bitcoin Core wird unter den Bedingungen der MIT-Lizenz veröffentlicht. Siehe [COPYING](COPYING) für weitere
Informationen oder siehe https://opensource.org/licenses/MIT.

Entwicklungsprozess
-------------------

Der `master` Branch wird regelmäßig gebaut (siehe `doc/build-*.md` für Anweisungen) und getestet, aber es wird nicht garantiert, dass er komplett stabil ist. [Tags](https://github.com/bitcoin/bitcoin/tags) werden regelmäßig aus Release-Branches erstellt, um neue offizielle, stabile Versionen von Bitcoin Core anzuzeigen.

Das https://github.com/bitcoin-core/gui Repository wird ausschließlich für die Entwicklung der GUI verwendet. Sein Master-Branch ist in allen Monotree-Repositories identisch. Release-Branches und Tags existieren nicht, also forken Sie dieses Repository bitte nur aus Entwicklungsgründen.

Der Beitragsprozess wird in [CONTRIBUTING.md](CONTRIBUTING.md) beschrieben,
und nützliche Hinweise für Entwickler finden Sie in [doc/developer-notes.md](doc/developer-notes.md).

Testen
-------

Testen und Code-Review sind der Engpass für die Entwicklung; wir erhalten mehr Pull
Requests, als wir kurzfristig überprüfen und testen können. Bitte haben Sie Geduld und helfen Sie, indem Sie die Pull Requests anderer Personen testen, und denken Sie daran, dass dies ein sicherheitskritisches Projekt ist, bei dem jeder Fehler Menschen viel Geld kosten könnte.

### Automatisiertes Testen

Entwickler werden nachdrücklich ermutigt, [Unit-Tests](src/test/README.md) für neuen Code zu schreiben und neue Unit-Tests für alten Code einzureichen. Unit-Tests können kompiliert und ausgeführt werden
(vorausgesetzt, sie wurden während der Generierung des Build-Systems nicht deaktiviert) mit: `ctest`. Weitere Details zum Ausführen und Erweitern von Unit-Tests finden Sie in [/src/test/README.md](/src/test/README.md).

Es gibt auch [Regressions- und Integrationstests](/test), die in Python geschrieben sind.
Diese Tests können ausgeführt werden (wenn die [Test-Abhängigkeiten](/test) installiert sind) mit: `build/test/functional/test_runner.py`
(angenommen `build` ist Ihr Build-Verzeichnis).

Die CI (Continuous Integration) Systeme stellen sicher, dass jeder Pull Request für Windows, Linux und macOS gebaut wird und dass Unit-/Sanity-Tests automatisch ausgeführt werden.

### Manuelle Qualitätssicherung (QA) Tests

Änderungen sollten von jemand anderem als dem Entwickler getestet werden, der den Code geschrieben hat. Dies ist besonders wichtig für große oder risikoreiche Änderungen. Es ist nützlich, der Pull-Request-Beschreibung einen Testplan hinzuzufügen, wenn das Testen der Änderungen nicht unkompliziert ist.

Übersetzungen
------------

Änderungen an Übersetzungen sowie neue Übersetzungen können auf
[Bitcoin Core's Transifex-Seite](https://www.transifex.com/bitcoin/bitcoin/) eingereicht werden.

Übersetzungen werden regelmäßig von Transifex gezogen und in das Git-Repository zusammengeführt. Siehe den
[Übersetzungsprozess](doc/translation_process.md) für Details zur Funktionsweise.

**Wichtig**: Wir akzeptieren keine Übersetzungsänderungen als GitHub Pull Requests, da der nächste
Pull von Transifex diese automatisch wieder überschreiben würde.