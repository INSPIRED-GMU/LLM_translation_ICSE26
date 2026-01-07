<p align="center">
  <img src="res/logo-header.svg" alt="RustDesk - Dein Remote-Desktop"><br>
  <a href="#public-servers">Server</a> •
  <a href="#raw-steps-to-build">Build</a> •
  <a href="#how-to-build-with-docker">Docker</a> •
  <a href="#file-structure">Struktur</a> •
  <a href="#snapshot">Snapshot</a><br>
</p>

## Abhängigkeiten

Die Desktop-Versionen verwenden Flutter oder Sciter (veraltet) für die GUI. Dieses Tutorial bezieht sich nur auf Sciter, da es einfacher und benutzerfreundlicher ist. Schau dir unser [CI](https://github.com/rustdesk/rustdesk/blob/master/.github/workflows/flutter-build.yml) für den Flutter-Build an.

Bitte lade die Sciter-Dynamikbibliothek selbst herunter.

[Windows](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.win/x64/sciter.dll) |
[Linux](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so) |
[macOS](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.osx/libsciter.dylib)

## Schritte zum Bauen

- Bereite deine Rust-Entwicklungsumgebung und C++-Build-Umgebung vor.

- Installiere [vcpkg](https://github.com/microsoft/vcpkg) und setze die Umgebungsvariable `VCPKG_ROOT` korrekt.

  - Windows: `vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static`
  - Linux/macOS: `vcpkg install libvpx libyuv opus aom`

- Führe `cargo run` aus.

## [Build](https://rustdesk.com/docs/en/dev/build/)

## Wie man unter Linux baut

### Ubuntu 18 (Debian 10)

```sh
sudo apt install -y zip g++ gcc git curl wget nasm yasm libgtk-3-dev clang libxcb-randr0-dev libxdo-dev \
        libxfixes-dev libxcb-shape0-dev libxcb-xfixes0-dev libasound2-dev libpulse-dev cmake make \
        libclang-dev ninja-build libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libpam0g-dev
```

## Dateistruktur

- **[libs/hbb_common](https://github.com/rustdesk/rustdesk/tree/master/libs/hbb_common)**: Video-Codec, Konfiguration, TCP/UDP-Wrapper, Protobuf, FS-Funktionen für Dateitransfer und weitere Hilfsfunktionen.
- **[libs/scrap](https://github.com/rustdesk/rustdesk/tree/master/libs/scrap)**: Bildschirmaufnahme.
- **[libs/enigo](https://github.com/rustdesk/rustdesk/tree/master/libs/enigo)**: Plattformübergreifende Tastatur-/Maussteuerung.
- **[libs/clipboard](https://github.com/rustdesk/rustdesk/tree/master/libs/clipboard)**: Datei-Kopier- und Einfüge-Implementierung für Windows, Linux und macOS.
- **[src/ui](https://github.com/rustdesk/rustdesk/tree/master/src/ui)**: Veraltete Sciter-UI (deprecated).
- **[src/server](https://github.com/rustdesk/rustdesk/tree/master/src/server)**: Audio-/Clipboard-/Input-/Video-Services und Netzwerkverbindungen.

## Screenshots

![Verbindungsmanager](https://github.com/rustdesk/rustdesk/assets/28412477/db82d4e7-c4bc-4823-8e6f-6af7eadf7651)

![Mit einem Windows-PC verbunden](https://github.com/rustdesk/rustdesk/assets/28412477/9baa91e9-3362-4d06-aa1a-7518edcbd7ea)

![Dateiübertragung](https://github.com/rustdesk/rustdesk/assets/28412477/39511ad3-aa9a-4f8c-8947-1cce286a46ad)

![TCP-Tunneling](https://github.com/rustdesk/rustdesk/assets/28412477/78e8708f-e87e-4570-8373-1360033ea6c5)

## Lizenz

[MIT](https://opensource.org/licenses/MIT)

---

RustDesk heißt Beiträge von allen willkommen. Siehe [CONTRIBUTING.md](docs/CONTRIBUTING.md) für den Einstieg.

