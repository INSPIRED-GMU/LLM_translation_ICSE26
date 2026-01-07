Protocol Buffers - Googles Datenformat zum Austausch von Daten
===========================================================

[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/protocolbuffers/protobuf/badge)](https://securityscorecards.dev/viewer/?uri=github.com/protocolbuffers/protobuf)

Copyright 2023 Google LLC

Übersicht
-----------

Protocol Buffers (auch bekannt als protobuf) sind Googles sprachneutrales,
plattformneutrales und erweiterbares Mechanismus zur Serialisierung strukturierter Daten.
Weitere Informationen finden Sie in der [protobuf-Dokumentation](https://protobuf.dev).

Diese README-Datei enthält Installationsanweisungen für protobuf. Um protobuf zu installieren,
müssen Sie den Protokoll-Compiler (zum Kompilieren von .proto-Dateien) und das protobuf-Laufzeitsystem
für Ihre bevorzugte Programmiersprache installieren.

Arbeiten mit dem Protobuf-Quellcode
-----------------------------------

Die meisten Nutzer finden es am einfachsten, mit
[unterstützten Releases](https://github.com/protocolbuffers/protobuf/releases) zu arbeiten.

Wenn Sie sich entscheiden, mit der neuesten Version des Hauptbranches zu arbeiten,
kann es vorkommen, dass der Build aufgrund von quellinkompatiblen Änderungen oder
unzureichend getesteten (und daher fehlerhaften) Verhaltensweisen unterbrochen wird.

Wenn Sie C++ verwenden oder protobuf als Teil Ihres Projekts aus dem Quellcode bauen müssen,
sollten Sie einen Release-Commit auf einem Release-Branch verwenden.

Auch Release-Branches können zwischen den Release-Commits instabil sein.

### Bazel mit Bzlmod

Protobuf unterstützt [Bzlmod](https://bazel.build/external/module) ab Bazel 7.
Benutzer sollten eine Abhängigkeit von protobuf in ihrer MODULE.bazel-Datei wie folgt angeben:

```
bazel_dep(name = "protobuf", version = <VERSION>)
```

Optional können Benutzer den Repository-Namen überschreiben, z.B. zur Kompatibilität mit WORKSPACE.

```
bazel_dep(name = "protobuf", version = <VERSION>, repo_name = "com_google_protobuf")
```

### Bazel mit WORKSPACE

Benutzer können Folgendes zu ihrer älteren
[WORKSPACE](https://bazel.build/external/overview#workspace-system)-Datei hinzufügen.

Hinweis: `protobuf_extra_deps.bzl` wurde im Release `v30.x` hinzugefügt.

```
http_archive(
    name = "com_google_protobuf",
    strip_prefix = "protobuf-VERSION",
    sha256 = ...,
    url = ...,
)

load("@com_google_protobuf//:protobuf_deps.bzl", "protobuf_deps")

protobuf_deps()

load("@com_google_protobuf//:protobuf_extra_deps.bzl", "protobuf_extra_deps")

protobuf_extra_deps();
```

Installation des Protobuf-Compilers
-----------------------------------

Der Protobuf-Compiler ist in C++ geschrieben. Wenn Sie C++ verwenden, folgen Sie bitte den
[C++-Installationsanweisungen](src/README.md), um `protoc` zusammen mit dem C++-Laufzeitsystem zu installieren.

Für Nicht-C++-Benutzer ist der einfachste Weg, den Protokoll-Compiler zu installieren,
das Herunterladen einer vorgefertigten Binärdatei von unserer [GitHub-Release-Seite](https://github.com/protocolbuffers/protobuf/releases).

Im Download-Bereich jeder Version finden Sie vorgefertigte Binärdateien in ZIP-Paketen:
`protoc-$VERSION-$PLATFORM.zip`. Dieses Paket enthält die `protoc`-Binärdatei sowie
einen Satz standardmäßiger `.proto`-Dateien, die mit protobuf verteilt werden.

Ältere Versionen, die nicht auf der Release-Seite verfügbar sind, finden Sie im
[Maven-Repository](https://repo1.maven.org/maven2/com/google/protobuf/protoc/).

Diese vorgefertigten Binärdateien werden nur für veröffentlichte Versionen bereitgestellt.
Wenn Sie die neueste Version aus dem Hauptbranch verwenden oder den protobuf-Code ändern möchten,
wird empfohlen, `protoc` aus dem Quellcode zu bauen.

Anweisungen zum Bauen von `protoc` aus dem Quellcode finden Sie in den
[C++-Installationsanweisungen](src/README.md).

Installation des Protobuf-Laufzeitsystems
----------------------------------------

Protobuf unterstützt verschiedene Programmiersprachen. Für jede Sprache finden Sie Anweisungen
im entsprechenden Quellverzeichnis zur Installation des Protobuf-Laufzeitsystems:

| Sprache                              | Quelle                                                      |
|-------------------------------------|-------------------------------------------------------------|
| C++ (inklusive C++-Runtime und protoc) | [src](src)                                                  |
| Java                                | [java](java)                                                |
| Python                              | [python](python)                                            |
| Objective-C                         | [objectivec](objectivec)                                     |
| C#                                  | [csharp](csharp)                                            |
| Ruby                                | [ruby](ruby)                                                |
| Go                                  | [protocolbuffers/protobuf-go](https://github.com/protocolbuffers/protobuf-go) |
| PHP                                 | [php](php)                                                  |
| Dart                                | [dart-lang/protobuf](https://github.com/dart-lang/protobuf) |
| JavaScript                          | [protocolbuffers/protobuf-javascript](https://github.com/protocolbuffers/protobuf-javascript) |

Schnellstart
------------

Der beste Weg, protobuf zu lernen, ist das Folgen der [Tutorials in unserem Entwicklerhandbuch](https://protobuf.dev/getting-started).

Wenn Sie lieber von Codebeispielen lernen, schauen Sie sich die Beispiele im [examples](examples)-Verzeichnis an.

Dokumentation
-------------

Die komplette Dokumentation finden Sie auf der [Protocol Buffers Dokumentationsseite](https://protobuf.dev).

Unterstützungsrichtlinie
-------------------------

Lesen Sie unsere [Version Support Policy](https://protobuf.dev/version-support/),
um über die Unterstützungszeiträume für Sprachbibliotheken informiert zu bleiben.

Entwickler-Community
--------------------

Um über bevorstehende Änderungen in Protocol Buffers informiert zu bleiben und sich mit Entwicklern und Nutzern auszutauschen,
treten Sie der [Google-Gruppe](https://groups.google.com/g/protobuf) bei.

