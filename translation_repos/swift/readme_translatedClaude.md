<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://www.swift.org/assets/images/swift~dark.svg">
  <img src="https://www.swift.org/assets/images/swift.svg" alt="Swift Logo" height="70">
</picture>

# Swift Programmiersprache

| | **Architektur** | **Build** |
|---|:---:|:---:|
| **macOS**        | x86_64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-macos/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-macos)|
| **Ubuntu 20.04** | x86_64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-ubuntu-20_04/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-ubuntu-20_04)|
| **Ubuntu 20.04** | AArch64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-ubuntu-20_04-aarch64/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-ubuntu-20_04-aarch64)|
| **Ubuntu 22.04** | x86_64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-ubuntu-22_04/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-ubuntu-22_04)|
| **Ubuntu 22.04** | AArch64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-ubuntu-22_04-aarch64/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-ubuntu-22_04-aarch64)|
| **Ubuntu 24.04** | x86_64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-ubuntu-24_04/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-ubuntu-24_04)|
| **Ubuntu 24.04** | AArch64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-ubuntu-24_04-aarch64/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-ubuntu-24_04-aarch64)|
| **Amazon Linux 2** | x86_64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-amazon-linux-2/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-amazon-linux-2)|
| **Amazon Linux 2** | AArch64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-amazon-linux-2-aarch64/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-amazon-linux-2-aarch64)|
| **Universal Base Image 9** | x86_64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-ubi-9/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-ubi-9)|
| **Debian 12** | x86_64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-debian-12/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-debian-12)|
| **Debian 12** | AArch64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-debian-12-aarch64/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-debian-12-aarch64)|
| **Fedora 39** | x86_64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-fedora-39/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-fedora-39)|
| **Fedora 39** | AArch64 |[![Build Status](https://ci.swift.org/job/oss-swift-package-fedora-39-aarch64/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-package-fedora-39-aarch64)|
| **Windows 10** | x86_64 |[![Build Status](https://ci-external.swift.org/job/swift-main-windows-toolchain/lastCompletedBuild/badge/icon)](https://ci-external.swift.org/job/swift-main-windows-toolchain)|
| **Windows 10** | ARM64 |[![Build Status](https://ci-external.swift.org/job/swift-main-windows-toolchain-arm64/lastCompletedBuild/badge/icon)](https://ci-external.swift.org/job/swift-main-windows-toolchain-arm64)|

**Cross-Compilation Ziele**

| **Ziel** | **Build** |
|:---:|:---:|
| **wasm32-unknown-wasi** |[![Build Status](https://ci.swift.org/job/oss-swift-pr-test-crosscompile-wasm-ubuntu-20_04/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-pr-test-crosscompile-wasm-ubuntu-20_04)|

**Von der Swift-Community gehostete CI-Plattformen**

| **Betriebssystem** | **Architektur** | **Build** |
|---|:---:|:---:|
|**[Android](https://github.com/apple/swift-community-hosted-continuous-integration/blob/main/nodes/x86_64_ubuntu_16_04_LTS_android.json)** | ARMv7 |[![Build Status](https://ci-external.swift.org/job/oss-swift-RA-linux-ubuntu-16.04-android/lastCompletedBuild/badge/icon)](https://ci-external.swift.org/job/oss-swift-RA-linux-ubuntu-16.04-android)|
|**[Android](https://github.com/apple/swift-community-hosted-continuous-integration/blob/main/nodes/x86_64_ubuntu_16_04_LTS_android.json)** | AArch64 |[![Build Status](https://ci-external.swift.org/job/oss-swift-RA-linux-ubuntu-16.04-android-arm64/lastCompletedBuild/badge/icon)](https://ci-external.swift.org/job/oss-swift-RA-linux-ubuntu-16.04-android-arm64)|
|**[Windows 2019 (VS 2019)](https://github.com/apple/swift-community-hosted-continuous-integration/blob/main/nodes/x86_64_windows_2019_VS2019.json)** | x86_64 | [![Build Status](https://ci-external.swift.org/job/oss-swift-windows-x86_64-vs2019/lastCompletedBuild/badge/icon)](https://ci-external.swift.org/job/oss-swift-windows-x86_64-vs2019)|

## Willkommen bei Swift

Swift ist eine hochperformante Systemprogrammiersprache. Sie verfügt über eine klare
und moderne Syntax, bietet nahtlosen Zugriff auf bestehenden C- und Objective-C-Code
und Frameworks und ist standardmäßig speichersicher.

Obwohl von Objective-C und vielen anderen Sprachen inspiriert, ist Swift selbst keine
C-abgeleitete Sprache. Als vollständige und unabhängige Sprache vereint Swift Kernfunktionen
wie Ablaufsteuerung, Datenstrukturen und Funktionen mit High-Level-Konstrukten wie Objekten,
Protokollen, Closures und Generics. Swift unterstützt Module und eliminiert damit die
Notwendigkeit von Headern und die damit verbundene Code-Duplizierung.

Um mehr über die Programmiersprache zu erfahren, besuchen Sie [swift.org](https://swift.org/documentation/).

- [Zu Swift beitragen](#zu-swift-beitragen)
- [Erste Schritte](#erste-schritte)
  - [Swift Toolchains](#swift-toolchains)
  - [Build-Fehler](#build-fehler)
- [Mehr erfahren](#mehr-erfahren)

## Zu Swift beitragen

Beiträge zu Swift sind willkommen und werden gefördert! Bitte lesen Sie den
[Leitfaden zum Beitragen zu Swift](https://swift.org/contributing/).

Bevor Sie den Pull Request einreichen, stellen Sie bitte sicher, dass Sie [Ihre
Änderungen getestet haben](https://github.com/apple/swift/blob/main/docs/ContinuousIntegration.md)
und dass sie den [Richtlinien des Swift-Projekts für das Beitragen von
Code](https://swift.org/contributing/#contributing-code) folgen.

Um eine wirklich großartige Community zu sein, muss [Swift.org](https://swift.org/) Entwickler
aus allen Lebensbereichen, mit unterschiedlichen Hintergründen und einem breiten
Erfahrungsspektrum willkommen heißen. Eine vielfältige und freundliche Community wird mehr großartige
Ideen, mehr einzigartige Perspektiven und besseren Code hervorbringen. Wir werden
sorgfältig daran arbeiten, die Swift-Community für jeden einladend zu gestalten.

Um Klarheit darüber zu schaffen, was von unseren Mitgliedern erwartet wird, hat Swift den
vom Contributor Covenant definierten Verhaltenskodex übernommen. Dieses Dokument wird
in vielen Open-Source-Communities verwendet, und wir denken, es artikuliert unsere Werte
gut. Weitere Informationen finden Sie im [Verhaltenskodex](https://swift.org/code-of-conduct/).

## Erste Schritte

Wenn Sie interessiert sind an:
- Fehlerbehebungen und Features für den Compiler beizutragen: Lesen Sie unseren
  [Leitfaden für Ihren ersten Pull Request](/docs/HowToGuides/FirstPullRequest.md).
- Einmaligem Aufbau des Compilers: Lesen Sie unseren [Erste-Schritte-Leitfaden][].
- Einmaligem Aufbau einer Toolchain: Folgen Sie dem [Erste-Schritte-Leitfaden][]
  bis zum Abschnitt "Building the project". Danach folgen Sie den
  Anweisungen im Abschnitt [Swift Toolchains](#swift-toolchains) unten.

Wir haben auch eine [FAQ](/docs/HowToGuides/FAQ.md), die häufige Fragen beantwortet.

[Erste-Schritte-Leitfaden]: /docs/HowToGuides/GettingStarted.md

### Swift Toolchains

#### Erstellen

Swift Toolchains werden mit dem Skript
[build-toolchain](https://github.com/apple/swift/blob/main/utils/build-toolchain) erstellt. Dieses
Skript wird von swift.org's CI verwendet, um Snapshots zu erstellen, und ermöglicht es,
solche Builds lokal für Entwicklungs- oder Vertriebszwecke zu reproduzieren. Ein typischer
Aufruf sieht wie folgt aus:

```sh
  $ ./swift/utils/build-toolchain $BUNDLE_PREFIX
```

wobei ``$BUNDLE_PREFIX`` eine Zeichenkette ist, die dem Build-Datum vorangestellt wird,
um die Bundle-ID der ``Info.plist`` der Toolchain zu bilden. Wenn zum
Beispiel ``$BUNDLE_PREFIX`` ``com.example`` wäre, hätte die erstellte Toolchain
die Bundle-ID ``com.example.YYYYMMDD``. Sie wird in dem Verzeichnis erstellt,
in dem Sie das Skript ausführen, mit einem Dateinamen der Form:
``swift-LOCAL-YYYY-MM-DD-a-osx.tar.gz``.

Neben dem Erstellen der Toolchain unterstützt ``build-toolchain`` auch die
folgenden (nicht erschöpfenden) nützlichen Optionen:

- ``--dry-run``: Führt einen Testlauf durch. Standardmäßig deaktiviert.
- ``--test``: Testet die Toolchain nach der Kompilierung. Standardmäßig deaktiviert.
- ``--distcc``: Verwendet distcc zur Beschleunigung des Builds durch Verteilung des C++-Teils
  des Swift-Builds. Standardmäßig deaktiviert.
- ``--sccache``: Verwendet sccache zur Beschleunigung nachfolgender Compiler-Builds durch
  Caching weiterer C++-Build-Artefakte. Standardmäßig deaktiviert.

Mit der Zeit können weitere Optionen hinzukommen. Bitte verwenden Sie ``--help`` bei
``build-toolchain``, um die vollständige Liste der Optionen zu sehen.

#### Installation in Xcode

Unter macOS, wenn man eine solche Toolchain in Xcode installieren möchte:

1. Entpacken und kopieren Sie die Toolchain in eines der Verzeichnisse `/Library/Developer/Toolchains/` oder
   `~/Library/Developer/Toolchains/`. Zum Beispiel:

```sh
  $ sudo tar -xzf swift-LOCAL-YYYY-MM-DD-a-osx.tar.gz -C /
  $ tar -xzf swift-LOCAL-YYYY-MM-DD-a-osx.tar.gz -C ~/
```

Das Skript generiert auch ein Archiv mit Debug-Symbolen, das über dem
Hauptarchiv installiert werden kann, um die Symbolisierung von
Compiler-Abstürzen zu ermöglichen.

```sh
  $ sudo tar -xzf swift-LOCAL-YYYY-MM-DD-a-osx-symbols.tar.gz -C /
  $ tar -xzf swift-LOCAL-YYYY-MM-DD-a-osx-symbols.tar.gz -C ~/
```

2. Legen Sie die lokale Toolchain für Xcode über `Xcode->Toolchains` fest.

### Build-Fehler

Probieren Sie die Vorschläge in
[Problembehebung bei Build-Problemen](/docs/HowToGuides/GettingStarted.md#troubleshooting-build-issues).

Stellen Sie sicher, dass Sie die
[korrekte Version](/docs/HowToGuides/GettingStarted.md#installing-dependencies)
von Xcode verwenden.

Wenn Sie die Xcode-Version geändert haben, aber immer noch Fehler auftreten, die mit
der Xcode-Version zusammenzuhängen scheinen, versuchen Sie `--clean` bei `build-script`.

Wenn eine neue Version von Xcode veröffentlicht wird, können Sie Ihren Build ohne
Neukompilierung des gesamten Projekts aktualisieren, indem Sie `--reconfigure` bei `build-script` verwenden.

## Mehr erfahren

Werfen Sie einen Blick auf den [Dokumentationsindex](/docs/README.md) für einen Überblick
über die verfügbare Dokumentation. Insbesondere die Dokumente
[Debugging des Swift Compilers](docs/DebuggingTheCompiler.md) und
[Continuous Integration für Swift](docs/ContinuousIntegration.md) sind sehr
hilfreich, um sie vor dem Einreichen Ihres ersten PRs zu verstehen.