Protocol Buffers - Googles Datenaustauschformat
===================================================

[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/protocolbuffers/protobuf/badge)](https://securityscorecards.dev/viewer/?uri=github.com/protocolbuffers/protobuf)

Copyright 2023 Google LLC

Überblick
--------

Protocol Buffers (auch bekannt als protobuf) ist Googles sprachneutraler,
plattformneutraler, erweiterbarer Mechanismus zur Serialisierung strukturierter Daten. Mehr
darüber erfahren Sie in der [protobuf-Dokumentation](https://protobuf.dev).

Diese README-Datei enthält Installationsanweisungen für protobuf. Um protobuf zu installieren,
müssen Sie den Protocol Compiler (zum Kompilieren von .proto-Dateien) und die Protobuf-Runtime
für Ihre gewählte Programmiersprache installieren.

Arbeiten mit Protobuf-Quellcode
---------------------------------

Für die meisten Benutzer ist das Arbeiten mit [unterstützten Releases](https://github.com/protocolbuffers/protobuf/releases)
der einfachste Weg.

Wenn Sie sich entscheiden, mit der Head-Revision des Hauptzweigs zu arbeiten, kann Ihr Build
gelegentlich durch quellencodeinkompatible Änderungen und unzureichend getestetes
(und daher fehlerhaftes) Verhalten unterbrochen werden.

Wenn Sie C++ verwenden oder protobuf anderweitig als Teil Ihres Projekts aus dem Quellcode
erstellen müssen, sollten Sie sich an einen Release-Commit in einem Release-Branch halten.

Dies liegt daran, dass selbst Release-Branches zwischen Release-Commits eine gewisse
Instabilität aufweisen können.

### Bazel mit Bzlmod

Protobuf unterstützt [Bzlmod](https://bazel.build/external/module) mit Bazel 7 +.
Benutzer sollten eine Abhängigkeit von protobuf in ihrer MODULE.bazel-Datei wie folgt angeben.

```
bazel_dep(name = "protobuf", version = <VERSION>)
```

Benutzer können optional den Repo-Namen überschreiben, zum Beispiel für die Kompatibilität mit
WORKSPACE.

```
bazel_dep(name = "protobuf", version = <VERSION>, repo_name = "com_google_protobuf")
```

### Bazel mit WORKSPACE

Benutzer können auch Folgendes zu ihrer Legacy-[WORKSPACE](https://bazel.build/external/overview#workspace-system)-Datei hinzufügen.

Beachten Sie, dass die `protobuf_extra_deps.bzl` im Release `v30.x` hinzugefügt wurde.

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
------------------------------

Der protobuf-Compiler ist in C++ geschrieben. Wenn Sie C++ verwenden, folgen Sie bitte
den [C++-Installationsanweisungen](src/README.md), um protoc zusammen mit
der C++-Runtime zu installieren.

Für Nicht-C++-Benutzer ist der einfachste Weg zur Installation des Protocol Compilers der
Download einer vorkompilierten Binärdatei von unserer [GitHub Release-Seite](https://github.com/protocolbuffers/protobuf/releases).

Im Download-Bereich jedes Releases finden Sie vorkompilierte Binärdateien in
ZIP-Paketen: `protoc-$VERSION-$PLATFORM.zip`. Diese enthalten die protoc-Binärdatei
sowie einen Satz Standard-`.proto`-Dateien, die mit protobuf ausgeliefert werden.

Wenn Sie eine alte Version suchen, die nicht auf der Release-Seite verfügbar ist,
schauen Sie im [Maven-Repository](https://repo1.maven.org/maven2/com/google/protobuf/protoc/) nach.

Diese vorkompilierten Binärdateien werden nur für veröffentlichte Versionen bereitgestellt. Wenn Sie
die GitHub-Hauptversion bei HEAD verwenden möchten, oder Sie den protobuf-Code modifizieren müssen,
oder Sie C++ verwenden, wird empfohlen, Ihre eigene protoc-Binärdatei aus dem
Quellcode zu erstellen.

Wenn Sie die protoc-Binärdatei aus dem Quellcode erstellen möchten, lesen Sie die [C++-Installationsanweisungen](src/README.md).

Installation der Protobuf-Runtime
-----------------------------

Protobuf unterstützt verschiedene Programmiersprachen. Für jede Programmiersprache
finden Sie im entsprechenden Quellverzeichnis Anweisungen zur Installation
der protobuf-Runtime für diese spezifische Sprache:

| Sprache                              | Quelle                                                      |
|--------------------------------------|-------------------------------------------------------------|
| C++ (inkl. C++-Runtime und protoc)   | [src](src)                                                  |
| Java                                 | [java](java)                                                |
| Python                               | [python](python)                                            |
| Objective-C                          | [objectivec](objectivec)                                    |
| C#                                   | [csharp](csharp)                                            |
| Ruby                                 | [ruby](ruby)                                                |
| Go                                   | [protocolbuffers/protobuf-go](https://github.com/protocolbuffers/protobuf-go)|
| PHP                                  | [php](php)                                                  |
| Dart                                 | [dart-lang/protobuf](https://github.com/dart-lang/protobuf) |
| JavaScript                           | [protocolbuffers/protobuf-javascript](https://github.com/protocolbuffers/protobuf-javascript)|

Schnellstart
-----------

Der beste Weg, die Verwendung von protobuf zu erlernen, ist das Befolgen der [Tutorials in unserem
Entwicklerhandbuch](https://protobuf.dev/getting-started).

Wenn Sie aus Codebeispielen lernen möchten, werfen Sie einen Blick auf die Beispiele im
[examples](examples)-Verzeichnis.

Dokumentation
-------------

Die vollständige Dokumentation ist auf der [Protocol Buffers-Dokumentationsseite](https://protobuf.dev) verfügbar.

Support-Richtlinie
--------------

Lesen Sie unsere [Versionssupport-Richtlinie](https://protobuf.dev/version-support/),
um über die Supportzeiträume für die Sprachbibliotheken auf dem Laufenden zu bleiben.

Entwickler-Community
-------------------

Um über bevorstehende Änderungen in Protocol Buffers informiert zu werden und sich mit protobuf-Entwicklern und -Benutzern zu vernetzen,
[treten Sie der Google Group bei](https://groups.google.com/g/protobuf).