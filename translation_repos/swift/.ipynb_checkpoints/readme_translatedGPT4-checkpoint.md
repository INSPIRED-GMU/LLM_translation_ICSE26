<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://www.swift.org/assets/images/swift~dark.svg">
  <img src="https://www.swift.org/assets/images/swift.svg" alt="Swift-Logo" height="70">
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

**Cross-Kompilierungsziele**

| **Ziel** | **Build** |
|:---:|:---:|
| **wasm32-unknown-wasi** |[![Build Status](https://ci.swift.org/job/oss-swift-pr-test-crosscompile-wasm-ubuntu-20_04/lastCompletedBuild/badge/icon)](https://ci.swift.org/job/oss-swift-pr-test-crosscompile-wasm-ubuntu-20_04)|

**Swift Community-Hosted CI-Plattformen**

| **OS** | **Architektur** | **Build** |
|---|:---:|:---:|
|**[Android](https://github.com/apple/swift-community-hosted-continuous-integration/blob/main/nodes/x86_64_ubuntu_16_04_LTS_android.json)** | ARMv7 |[![Build Status](https://ci-external.swift.org/job/oss-swift-RA-linux-ubuntu-16.04-android/lastCompletedBuild/badge/icon)](https://ci-external.swift.org/job/oss-swift-RA-linux-ubuntu-16.04-android)|
|**[Android](https://github.com/apple/swift-community-hosted-continuous-integration/blob/main/nodes/x86_64_ubuntu_16_04_LTS_android.json)** | AArch64 |[![Build Status](https://ci-external.swift.org/job/oss-swift-RA-linux-ubuntu-16.04-android-arm64/lastCompletedBuild/badge/icon)](https://ci-external.swift.org/job/oss-swift-RA-linux-ubuntu-16.04-android-arm64)|
|**[Windows 2019 (VS 2019)](https://github.com/apple/swift-community-hosted-continuous-integration/blob/main/nodes/x86_64_windows_2019_VS2019.json)** | x86_64 | [![Build Status](https://ci-external.swift.org/job/oss-swift-windows-x86_64-vs2019/lastCompletedBuild/badge/icon)](https://ci-external.swift.org/job/oss-swift-windows-x86_64-vs2019)|

## Willkommen bei Swift

Swift ist eine leistungsstarke Systemprogrammiersprache. Sie hat eine klare und moderne Syntax, bietet nahtlosen Zugriff auf vorhandenen C- und Objective-C-Code sowie Frameworks und ist standardmäßig speichersicher.

Obwohl von Objective-C und vielen anderen Sprachen inspiriert, ist Swift keine C-abgeleitete Sprache. Als vollständige und unabhängige Sprache kombiniert Swift Kernfunktionen wie Ablaufsteuerung, Datenstrukturen und Funktionen mit High-Level-Konstrukten wie Objekten, Protokollen, Closures und Generics. Swift verwendet Module und eliminiert die Notwendigkeit für Header und damit verbundene Code-Duplikationen.

Um mehr über die Programmiersprache zu erfahren, besuchen Sie [swift.org](https://swift.org/documentation/).

- [Beitragen zu Swift](#contributing-to-swift)
- [Erste Schritte](#getting-started)
  - [Swift-Toolchains](#swift-toolchains)
  - [Build-Fehler](#build-failures)
- [Mehr erfahren](#learning-more)

## Beitragen zu Swift

Beiträge zu Swift sind willkommen und werden gefördert! Lesen Sie den
[Leitfaden zum Beitragen zu Swift](https://swift.org/contributing/).

Bevor Sie eine Pull-Anfrage einreichen, stellen Sie bitte sicher, dass Sie Ihre 
[Änderungen getestet haben](https://github.com/apple/swift/blob/main/docs/ContinuousIntegration.md) 
und dass sie den [Richtlinien für das Beitragen zu Swift](https://swift.org/contributing/#contributing-code) entsprechen.

Um eine wirklich großartige Community zu sein, muss [Swift.org](https://swift.org/) Entwickler aus allen Lebensbereichen willkommen heißen, mit unterschiedlichen Hintergründen und einem breiten Erfahrungsspektrum. Eine vielfältige und freundliche Community wird mehr großartige Ideen, einzigartigere Perspektiven und besseren Code hervorbringen. Wir werden uns bemühen, die Swift-Community für alle offen und einladend zu gestalten.

Um Klarheit darüber zu geben, was von unseren Mitgliedern erwartet wird, hat Swift den Verhaltenskodex des Contributor Covenant übernommen. Dieses Dokument wird in vielen Open-Source-Communities verwendet und wir glauben, dass es unsere Werte gut ausdrückt. Weitere Informationen finden Sie im [Verhaltenskodex](https://swift.org/code-of-conduct/).

## Erste Schritte

Wenn Sie interessiert sind an:
- Beiträgen von Korrekturen und Funktionen zum Compiler: Lesen Sie unseren 
  [Leitfaden zum Einreichen der ersten Pull-Anfrage](/docs/HowToGuides/FirstPullRequest.md).
- Einmaligem Erstellen des Compilers: Lesen Sie unseren [Leitfaden für den Einstieg][].
- Einmaligem Erstellen einer Toolchain: Befolgen Sie den [Leitfaden für den Einstieg][] bis zum Abschnitt "Projekt erstellen". Danach folgen Sie den Anweisungen im Abschnitt [Swift-Toolchains](#swift-toolchains) unten.

Wir haben auch eine [FAQ](/docs/HowToGuides/FAQ.md), die häufig gestellte Fragen beantwortet.

[Leitfaden für den Einstieg]: /docs/HowToGuides/GettingStarted.md

### Swift-Toolchains

#### Erstellen

Swift-Toolchains werden mit dem Skript 
[build-toolchain](https://github.com/apple/swift/blob/main/utils/build-toolchain) erstellt. Dieses 
Skript wird von der CI von swift.org verwendet, um Snapshots zu erstellen, und kann lokal genutzt werden, um solche Builds für Entwicklungs- oder Distributionszwecke zu reproduzieren. Ein typischer 
Aufruf sieht wie folgt aus:

```sh
  $ ./swift/utils/build-toolchain $BUNDLE_PREFIX
```

wobei ``$BUNDLE_PREFIX`` ein String ist, der dem Erstellungsdatum vorangestellt wird, um die Bundle-ID des ``Info.plist`` der Toolchain zu bilden. Wenn ``$BUNDLE_PREFIX`` beispielsweise ``com.example`` wäre, hätte die erzeugte Toolchain die Bundle-ID ``com.example.YYYYMMDD``. Sie wird im Verzeichnis erstellt, in dem Sie das Skript ausführen, mit einem Dateinamen im Format: ``swift-LOCAL-YYYY-MM-DD-a-osx.tar.gz``.

Neben dem Erstellen der Toolchain unterstützt ``build-toolchain`` auch die folgenden (nicht erschöpfenden) nützlichen Optionen:

- ``--dry-run``: Führt einen Trockentest durch. Standardmäßig deaktiviert.
- ``--test``: Testet die Toolchain, nachdem sie kompiliert wurde. Standardmäßig deaktiviert.
- ``--distcc``: Verwendet distcc, um den Build zu beschleunigen, indem der C++-Teil des Swift-Builds verteilt wird. Standardmäßig deaktiviert.
- ``--sccache``: Verwendet sccache, um nachfolgende Builds des Compilers zu beschleunigen, indem mehr C++-Build-Artefakte zwischengespeichert werden. Standardmäßig deaktiviert.

Weitere Optionen können im Laufe der Zeit hinzugefügt werden. Bitte geben Sie ``--help`` an 
``build-toolchain``, um die vollständige Liste der Optionen anzuzeigen.

#### Installation in Xcode

Auf macOS, wenn Sie eine solche Toolchain in Xcode installieren möchten:

1. Entpacken und kopieren Sie die Toolchain in eines der Verzeichnisse `/Library/Developer/Toolchains/` oder 
   `~/Library/Developer/Toolchains/`. Z. B.:

```sh
  $ sudo tar -xzf swift-LOCAL-YYYY-MM-DD-a-osx.tar.gz -C /
  $ tar -xzf swift-LOCAL-YYYY-MM-DD-a-osx.tar.gz -C ~/
```

Das Skript erzeugt auch ein Archiv, das Debug-Symbole enthält, die 
über das Hauptarchiv installiert werden können, um Compiler-Abstürze zu symbolisieren.

```sh
  $ sudo tar -xzf swift-LOCAL-YYYY-MM-DD-a-osx-symbols.tar.gz -C /
  $ tar -xzf swift-LOCAL-YYYY-MM-DD-a-osx-symbols.tar.gz -C ~/
```

2. Geben Sie die lokale Toolchain für die Verwendung durch Xcode unter `Xcode->Toolchains` an.

### Build-Fehler

Versuchen Sie die Vorschläge in 
[Probleme beim Build beheben](/docs/HowToGuides/GettingStarted.md#troubleshooting-build-issues).

Stellen Sie sicher, dass Sie die 
[richtige Version](/docs/HowToGuides/GettingStarted.md#installing-dependencies) von Xcode verwenden.

Wenn Sie die Xcode-Version geändert haben, aber weiterhin Fehler auftreten, die mit der Xcode-Version zusammenhängen, versuchen Sie, `--clean` an `build-script` zu übergeben.

Wenn eine neue Version von Xcode veröffentlicht wird, können Sie Ihren Build aktualisieren, ohne das gesamte Projekt neu zu kompilieren, indem Sie `--reconfigure` an `build-script` übergeben.

## Mehr erfahren

Sehen Sie sich unbedingt den [Dokumentationsindex](/docs/README.md) an, um einen Überblick über die verfügbare Dokumentation zu erhalten. Insbesondere die Dokumente mit den Titeln 
[Debugging the Swift Compiler](docs/DebuggingTheCompiler.md) und 
[Continuous Integration for Swift](docs/ContinuousIntegration.md) sind sehr hilfreich, bevor Sie Ihre erste PR einreichen.
