<a href="https://flutter.dev/">
  <h1 align="center">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://storage.googleapis.com/cms-storage-bucket/6e19fee6b47b36ca613f.png">
      <img alt="Flutter" src="https://storage.googleapis.com/cms-storage-bucket/c823e53b3a1a7b0d36a9.png">
    </picture>
  </h1>
</a>

[![Flutter CI Status](https://flutter-dashboard.appspot.com/api/public/build-status-badge?repo=flutter)](https://flutter-dashboard.appspot.com/#/build?repo=flutter)
[![Discord badge][]][Discord instructions]
[![Twitter handle][]][Twitter badge]
[![codecov](https://codecov.io/gh/flutter/flutter/branch/master/graph/badge.svg?token=11yDrJU2M2)](https://codecov.io/gh/flutter/flutter)
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/5631/badge)](https://bestpractices.coreinfrastructure.org/projects/5631)
[![SLSA 1](https://slsa.dev/images/gh-badge-level1.svg)](https://slsa.dev)

Flutter ist Googles SDK zum Erstellen schöner, schneller Benutzeroberflächen für
Mobile, Web und Desktop aus einer einzigen Codebasis. Flutter arbeitet mit bestehendem
Code zusammen, wird von Entwicklern und Organisationen weltweit genutzt und ist kostenlos und
Open Source.

## Dokumentation

* [Flutter installieren](https://flutter.dev/get-started/)
* [Flutter-Dokumentation](https://docs.flutter.dev/)
* [Entwicklungs-Wiki](./docs/README.md)
* [Zu Flutter beitragen](https://github.com/flutter/flutter/blob/main/CONTRIBUTING.md)

Für Ankündigungen zu neuen Releases, folgen Sie der
[flutter-announce@googlegroups.com](https://groups.google.com/forum/#!forum/flutter-announce)
Mailingliste. Unsere Dokumentation verfolgt auch [Breaking
Changes](https://docs.flutter.dev/release/breaking-changes) über Releases hinweg.

## Nutzungsbedingungen

Das Flutter-Tool lädt gelegentlich Ressourcen von Google-Servern herunter. Durch
das Herunterladen oder die Nutzung des Flutter SDK stimmen Sie den Google-Nutzungsbedingungen zu:
https://policies.google.com/terms

Wenn zum Beispiel von GitHub installiert (im Gegensatz zu einem vorverpackten
Archiv), lädt das Flutter-Tool beim ersten Start das Dart SDK von Google-Servern
herunter, da es zur Ausführung des `flutter`-Tools selbst verwendet wird.
Dies geschieht auch bei Flutter-Upgrades (z.B. durch Ausführen des `flutter
upgrade` Befehls).

## Über Flutter

Wir glauben, dass Flutter Ihnen hilft, schöne, schnelle Apps zu erstellen, mit einem produktiven,
erweiterbaren und offenen Entwicklungsmodell, egal ob Sie iOS oder Android,
Web, Windows, macOS, Linux oder die Einbettung als UI-Toolkit für eine Plattform Ihrer
Wahl anstreben.

### Schöne Benutzererlebnisse

Wir möchten Designer in die Lage versetzen, ihre kreative Vision vollständig umzusetzen, ohne
durch Einschränkungen des zugrunde liegenden Frameworks eingeschränkt zu werden.
Flutters [Schichtenarchitektur] gibt Ihnen die Kontrolle über jeden Pixel auf dem
Bildschirm, und seine leistungsstarken Compositing-Fähigkeiten ermöglichen es Ihnen, Grafiken, Video, Text
und Steuerelemente ohne Einschränkungen zu überlagern und zu animieren. Flutter enthält einen vollständigen
[Satz von Widgets][widget catalog] für pixelgenaue Erlebnisse, egal ob Sie für iOS ([Cupertino])
oder andere Plattformen ([Material]) entwickeln, zusammen mit Unterstützung für die Anpassung oder
Erstellung völlig neuer visueller Komponenten.

<p align="center"><img src="https://github.com/flutter/website/blob/main/src/content/assets/images/docs/homepage/reflectly-hero-600px.png?raw=true" alt="Reflectly hero image"></p>

### Schnelle Ergebnisse

Flutter ist schnell. Es wird von hardware-beschleunigten 2D-Grafik-
Bibliotheken wie [Skia] (die Chrome und Android zugrunde liegen) und
[Impeller] angetrieben. Wir haben Flutter so entwickelt, dass es
störungsfreie, ruckelfreie Grafiken in der nativen Geschwindigkeit Ihres Geräts unterstützt.

Flutter-Code wird von der erstklassigen [Dart-Plattform] angetrieben, die die
Kompilierung zu 32-Bit- und 64-Bit-ARM-Maschinencode für iOS und Android,
JavaScript und WebAssembly für das Web sowie Intel x64 und ARM
für Desktop-Geräte ermöglicht.

<p align="center"><img src="https://github.com/flutter/website/blob/main/src/content/assets/images/docs/homepage/dart-diagram-small.png?raw=true" alt="Dart diagram"></p>

### Produktive Entwicklung

Flutter bietet [zustandserhaltende Hot Reload][Hot reload] Funktionalität, mit der Sie Änderungen an Ihrem Code
vornehmen und die Ergebnisse sofort sehen können, ohne Ihre App neu zu starten oder ihren Zustand zu verlieren.

[![Hot reload animation][]][Hot reload]

### Erweiterbares und offenes Modell

Flutter funktioniert mit jedem Entwicklungstool (oder auch ohne) und enthält auch
Editor-Plugins für [Visual Studio Code] und [IntelliJ / Android Studio].
Flutter bietet [zehntausende von Paketen][Flutter packages] zur Beschleunigung Ihrer
Entwicklung, unabhängig von Ihrer Zielplattform. Der Zugriff auf anderen nativen Code
ist einfach, mit Unterstützung sowohl für FFI ([auf Android][Android FFI], [auf iOS][iOS FFI],
[auf macOS][macOS FFI] und [auf Windows][Windows FFI]) als auch
[plattformspezifische APIs][platform channels].

Flutter ist ein vollständig Open-Source-Projekt, und wir begrüßen Beiträge.
Informationen zum Einstieg finden Sie in unserem
[Leitfaden für Mitwirkende](CONTRIBUTING.md).

[Alle Links und Referenzen bleiben unverändert]