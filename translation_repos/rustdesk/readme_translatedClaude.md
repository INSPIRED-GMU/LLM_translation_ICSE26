<p align="center">
  <img src="res/logo-header.svg" alt="RustDesk - Ihr Remote-Desktop"><br>
  <a href="#public-servers">Server</a> •
  <a href="#raw-steps-to-build">Build</a> •
  <a href="#how-to-build-with-docker">Docker</a> •
  <a href="#file-structure">Struktur</a> •
  <a href="#snapshot">Snapshot</a><br>
  [<a href="docs/README-UA.md">Українська</a>] | [<a href="docs/README-CS.md">česky</a>] | [<a href="docs/README-ZH.md">中文</a>] | [<a href="docs/README-HU.md">Magyar</a>] | [<a href="docs/README-ES.md">Español</a>] | [<a href="docs/README-FA.md">فارسی</a>] | [<a href="docs/README-FR.md">Français</a>] | [<a href="docs/README-DE.md">Deutsch</a>] | [<a href="docs/README-PL.md">Polski</a>] | [<a href="docs/README-ID.md">Indonesian</a>] | [<a href="docs/README-FI.md">Suomi</a>] | [<a href="docs/README-ML.md">മലയാളം</a>] | [<a href="docs/README-JP.md">日本語</a>] | [<a href="docs/README-NL.md">Nederlands</a>] | [<a href="docs/README-IT.md">Italiano</a>] | [<a href="docs/README-RU.md">Русский</a>] | [<a href="docs/README-PTBR.md">Português (Brasil)</a>] | [<a href="docs/README-EO.md">Esperanto</a>] | [<a href="docs/README-KR.md">한국어</a>] | [<a href="docs/README-AR.md">العربي</a>] | [<a href="docs/README-VN.md">Tiếng Việt</a>] | [<a href="docs/README-DA.md">Dansk</a>] | [<a href="docs/README-GR.md">Ελληνικά</a>] | [<a href="docs/README-TR.md">Türkçe</a>]<br>
  <b>Wir brauchen Ihre Hilfe bei der Übersetzung dieser README, der <a href="https://github.com/rustdesk/rustdesk/tree/master/src/lang">RustDesk-Benutzeroberfläche</a> und der <a href="https://github.com/rustdesk/doc.rustdesk.com">RustDesk-Dokumentation</a> in Ihre Muttersprache</b>
</p>

Chatten Sie mit uns: [Discord](https://discord.gg/nDceKgxnkV) | [Twitter](https://twitter.com/rustdesk) | [Reddit](https://www.reddit.com/r/rustdesk)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/I2I04VU09)

Eine weitere Remote-Desktop-Software, geschrieben in Rust. Funktioniert direkt nach der Installation, keine Konfiguration erforderlich. Sie haben die volle Kontrolle über Ihre Daten und müssen sich keine Sorgen um die Sicherheit machen. Sie können unseren Rendezvous/Relay-Server nutzen, [Ihren eigenen aufsetzen](https://rustdesk.com/server) oder [Ihren eigenen Rendezvous/Relay-Server entwickeln](https://github.com/rustdesk/rustdesk-server-demo).

![image](https://user-images.githubusercontent.com/71636191/171661982-430285f0-2e12-4b1d-9957-4a58e375304d.png)

RustDesk begrüßt Beiträge von jedem. Siehe [CONTRIBUTING.md](docs/CONTRIBUTING.md) für Hilfe beim Einstieg.

[**FAQ**](https://github.com/rustdesk/rustdesk/wiki/FAQ)

[**BINÄRDATEIEN HERUNTERLADEN**](https://github.com/rustdesk/rustdesk/releases)

[**NIGHTLY BUILD**](https://github.com/rustdesk/rustdesk/releases/tag/nightly)

[<img src="https://f-droid.org/badge/get-it-on.png"
    alt="Holen Sie es sich auf F-Droid"
    height="80">](https://f-droid.org/en/packages/com.carriez.flutter_hbb)
[<img src="https://flathub.org/api/badge?svg&locale=en"
    alt="Holen Sie es sich auf Flathub"
    height="80">](https://flathub.org/apps/com.rustdesk.RustDesk)

## Abhängigkeiten

Desktop-Versionen verwenden Flutter oder Sciter (veraltet) für die GUI. Dieses Tutorial ist nur für Sciter, da es einfacher und anfängerfreundlicher ist. Schauen Sie sich unsere [CI](https://github.com/rustdesk/rustdesk/blob/master/.github/workflows/flutter-build.yml) für das Erstellen der Flutter-Version an.

Bitte laden Sie die Sciter-Dynamische-Bibliothek selbst herunter.

[Windows](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.win/x64/sciter.dll) |
[Linux](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so) |
[macOS](https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.osx/libsciter.dylib)

## Grundlegende Schritte zum Erstellen

- Bereiten Sie Ihre Rust-Entwicklungsumgebung und C++-Build-Umgebung vor

- Installieren Sie [vcpkg](https://github.com/microsoft/vcpkg) und setzen Sie die `VCPKG_ROOT`-Umgebungsvariable korrekt

  - Windows: vcpkg install libvpx:x64-windows-static libyuv:x64-windows-static opus:x64-windows-static aom:x64-windows-static
  - Linux/macOS: vcpkg install libvpx libyuv opus aom

- Führen Sie `cargo run` aus

## So erstellen Sie unter Linux

### Ubuntu 18 (Debian 10)

```sh
sudo apt install -y zip g++ gcc git curl wget nasm yasm libgtk-3-dev clang libxcb-randr0-dev libxdo-dev \
        libxfixes-dev libxcb-shape0-dev libxcb-xfixes0-dev libasound2-dev libpulse-dev cmake make \
        libclang-dev ninja-build libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libpam0g-dev
```

### openSUSE Tumbleweed

```sh
sudo zypper install gcc-c++ git curl wget nasm yasm gcc gtk3-devel clang libxcb-devel libXfixes-devel cmake alsa-lib-devel gstreamer-devel gstreamer-plugins-base-devel xdotool-devel pam-devel
```

### Fedora 28 (CentOS 8)

```sh
sudo yum -y install gcc-c++ git curl wget nasm yasm gcc gtk3-devel clang libxcb-devel libxdo-devel libXfixes-devel pulseaudio-libs-devel cmake alsa-lib-devel gstreamer1-devel gstreamer1-plugins-base-devel pam-devel
```

### Arch (Manjaro)

```sh
sudo pacman -Syu --needed unzip git cmake gcc curl wget yasm nasm zip make pkg-config clang gtk3 xdotool libxcb libxfixes alsa-lib pipewire
```

### vcpkg installieren

```sh
git clone https://github.com/microsoft/vcpkg
cd vcpkg
git checkout 2023.04.15
cd ..
vcpkg/bootstrap-vcpkg.sh
export VCPKG_ROOT=$HOME/vcpkg
vcpkg/vcpkg install libvpx libyuv opus aom
```

### libvpx korrigieren (Für Fedora)

```sh
cd vcpkg/buildtrees/libvpx/src
cd *
./configure
sed -i 's/CFLAGS+=-I/CFLAGS+=-fPIC -I/g' Makefile
sed -i 's/CXXFLAGS+=-I/CXXFLAGS+=-fPIC -I/g' Makefile
make
cp libvpx.a $HOME/vcpkg/installed/x64-linux/lib/
cd
```

### Build

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
git clone https://github.com/rustdesk/rustdesk
cd rustdesk
mkdir -p target/debug
wget https://raw.githubusercontent.com/c-smile/sciter-sdk/master/bin.lnx/x64/libsciter-gtk.so
mv libsciter-gtk.so target/debug
VCPKG_ROOT=$HOME/vcpkg cargo run
```

## Mit Docker erstellen

Klonen Sie zuerst das Repository und erstellen Sie den Docker-Container:

```sh
git clone https://github.com/rustdesk/rustdesk
cd rustdesk
docker build -t "rustdesk-builder" .
```

Dann führen Sie jedes Mal, wenn Sie die Anwendung erstellen müssen, den folgenden Befehl aus:

```sh
docker run --rm -it -v $PWD:/home/user/rustdesk -v rustdesk-git-cache:/home/user/.cargo/git -v rustdesk-registry-cache:/home/user/.cargo/registry -e PUID="$(id -u)" -e PGID="$(id -g)" rustdesk-builder
```

Beachten Sie, dass der erste Build länger dauern kann, bis die Abhängigkeiten zwischengespeichert sind. Nachfolgende Builds werden schneller sein. Wenn Sie verschiedene Argumente für den Build-Befehl angeben müssen, können Sie dies am Ende des Befehls in der Position `<OPTIONAL-ARGS>` tun. Wenn Sie beispielsweise eine optimierte Release-Version erstellen möchten, würden Sie dem obigen Befehl `--release` hinzufügen. Die resultierende ausführbare Datei wird im target-Ordner auf Ihrem System verfügbar sein und kann ausgeführt werden mit:

```sh
target/debug/rustdesk
```

Oder, wenn Sie eine Release-Version ausführen:

```sh
target/release/rustdesk
```

Bitte stellen Sie sicher, dass Sie diese Befehle aus dem Root-Verzeichnis des RustDesk-Repositories ausführen, da die Anwendung sonst möglicherweise die erforderlichen Ressourcen nicht finden kann. Beachten Sie auch, dass andere cargo-Unterbefehle wie `install` oder `run` derzeit über diese Methode nicht unterstützt werden, da sie das Programm im Container anstatt auf dem Host installieren oder ausführen würden.

## Dateistruktur

- **[libs/hbb_common](https://github.com/rustdesk/rustdesk/tree/master/libs/hbb_common)**: Video-Codec, Konfiguration, TCP/UDP-Wrapper, Protobuf, FS-Funktionen für Dateiübertragung und andere Hilfsfunktionen
- **[libs/scrap](https://github.com/rustdesk/rustdesk/tree/master/libs/scrap)**: Bildschirmaufnahme
- **[libs/enigo](https://github.com/rustdesk/rustdesk/tree/master/libs/enigo)**: Plattformspezifische Tastatur-/Maussteuerung
- **[libs/clipboard](https://github.com/rustdesk/rustdesk/tree/master/libs/clipboard)**: Implementierung von Kopieren und Einfügen für Windows, Linux, macOS
- **[src/ui](https://github.com/rustdesk/rustdesk/tree/master/src/ui)**: Veraltete Sciter-UI (nicht mehr unterstützt)
- **[src/server](https://github.com/rustdesk/rustdesk/tree/master/src/server)**: Audio-/Zwischenablage-/Eingabe-/Video-Dienste und Netzwerkverbindungen
- **[src/client.rs](https://github.com/rustdesk/rustdesk/tree/master/src/client.rs)**: Peer-Verbindung starten
- **[src/rendezvous_mediator.rs](https://github.com/rustdesk/rustdesk/tree/master/src/rendezvous_mediator.rs)**: Kommunikation mit [rustdesk-server](https://github.com/rustdesk/rustdesk-server), Warten auf direkte Verbindung (TCP-Hole-Punching) oder Relay-Verbindung
- **[src/platform](https://github.com/rustdesk/rustdesk/tree/master/src/platform)**: Plattformspezifischer Code
- **[flutter](https://github.com/rustdesk/rustdesk/tree/master/flutter)**: Flutter-Code für Desktop und Mobile
- **[flutter/web/js](https://github.com/rustdesk/rustdesk/tree/master/flutter/web/js)**: JavaScript für Flutter-Web-Client

## Screenshots

![Verbindungsmanager](https://github.com/rustdesk/rustdesk/assets/28412477/db82d4e7-c4bc-4823-8e6f-6af7eadf7651)

![Verbunden mit einem Windows-PC](https://github.com/rustdesk/rustdesk/assets/28412477/9baa91e9-3362-4d06-aa1a-7518edcbd7ea)

![Dateiübertragung](https://github.com/rustdesk/rustdesk/assets/28412477/39511ad3-aa9a-4f8c-8947-1cce286a46ad)

![TCP-Tunneling](https://github.com/rustdesk/rustdesk/assets/28412477/78e8708f-e87e-4570-8373-1360033ea6c5)