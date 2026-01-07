**Dieses GitHub-Repository (<https://github.com/Genymobile/scrcpy>) ist die einzige offizielle
Quelle für das Projekt. Laden Sie keine Releases von zufälligen Websites herunter, auch wenn
deren Name `scrcpy` enthält.**

# scrcpy (v3.1)

<img src="app/data/icon.svg" width="128" height="128" alt="scrcpy" align="right" />

_ausgesprochen "**scr**een **c**o**py**"_

Diese Anwendung spiegelt Android-Geräte (Video und Audio), die über USB oder
[über TCP/IP](doc/connection.md#tcpip-wireless) verbunden sind, und ermöglicht die Steuerung des
Geräts mit Tastatur und Maus des Computers. Es erfordert keinen _root_-Zugriff und funktioniert unter
_Linux_, _Windows_ und _macOS_.

![screenshot](assets/screenshot-debian-600.jpg)

Der Fokus liegt auf:

 - **Leichtigkeit**: nativ, zeigt nur den Gerätebildschirm an
 - **Leistung**: 30~120fps, abhängig vom Gerät
 - **Qualität**: 1920×1080 oder höher
 - **Geringe Latenz**: [35~70ms][lowlatency]
 - **Kurze Startzeit**: ~1 Sekunde bis zum ersten Bild
 - **Nicht-Aufdringlichkeit**: nichts wird auf dem Android-Gerät installiert
 - **Benutzervorteile**: kein Konto, keine Werbung, kein Internet erforderlich
 - **Freiheit**: freie und quelloffene Software

[lowlatency]: https://github.com/Genymobile/scrcpy/pull/646

Zu den Funktionen gehören:
 - [Audioweiterleitung](doc/audio.md) (Android 11+)
 - [Aufnahme](doc/recording.md)
 - [Virtuelles Display](doc/virtual_display.md)
 - Spiegelung bei [ausgeschaltetem Android-Gerätebildschirm](doc/device.md#turn-screen-off)
 - [Kopieren und Einfügen](doc/control.md#copy-paste) in beide Richtungen
 - [Konfigurierbare Qualität](doc/video.md)
 - [Kamera-Spiegelung](doc/camera.md) (Android 12+)
 - [Spiegelung als Webcam (V4L2)](doc/v4l2.md) (nur Linux)
 - Physische [Tastatur][hid-keyboard]- und [Maus][hid-mouse]-Simulation (HID)
 - [Gamepad](doc/gamepad.md)-Unterstützung
 - [OTG-Modus](doc/otg.md)
 - und mehr...

[hid-keyboard]: doc/keyboard.md#physical-keyboard-simulation
[hid-mouse]: doc/mouse.md#physical-mouse-simulation

## Voraussetzungen

Das Android-Gerät benötigt mindestens API 21 (Android 5.0).

[Audioweiterleitung](doc/audio.md) wird für API >= 30 (Android 11+) unterstützt.

Stellen Sie sicher, dass Sie [USB-Debugging aktiviert haben][enable-adb] auf Ihrem/n Gerät(en).

[enable-adb]: https://developer.android.com/studio/debug/dev-options#enable

Bei einigen Geräten (besonders Xiaomi) könnte folgender Fehler auftreten:

```
java.lang.SecurityException: Injecting input events requires the caller (or the source of the instrumentation, if any) to have the INJECT_EVENTS permission.
```

In diesem Fall müssen Sie [eine zusätzliche Option][control] `USB-Debugging
(Sicherheitseinstellungen)` aktivieren (dies ist ein anderer Punkt als `USB-Debugging`), um
es mit Tastatur und Maus steuern zu können. Ein Neustart des Geräts ist nach dem Setzen dieser
Option erforderlich.

[control]: https://github.com/Genymobile/scrcpy/issues/70#issuecomment-373286323

Beachten Sie, dass USB-Debugging für den Betrieb von scrcpy im [OTG-Modus](doc/otg.md) nicht erforderlich ist.


## App herunterladen

 - [Linux](doc/linux.md)
 - [Windows](doc/windows.md) (lesen Sie [wie man es ausführt](doc/windows.md#run))
 - [macOS](doc/macos.md)


## Wichtige Tipps

 - [Reduzierung der Auflösung](doc/video.md#size) kann die Leistung stark verbessern
   (`scrcpy -m1024`)
 - [_Rechtsklick_](doc/mouse.md#mouse-bindings) löst `ZURÜCK` aus
 - [_Mittelklick_](doc/mouse.md#mouse-bindings) löst `HOME` aus
 - <kbd>Alt</kbd>+<kbd>f</kbd> schaltet [Vollbild](doc/window.md#fullscreen) um
 - Es gibt viele weitere [Tastenkombinationen](doc/shortcuts.md)


## Anwendungsbeispiele

Es gibt viele Optionen, die auf separaten Seiten [dokumentiert](#benutzerdokumentation) sind.
Hier sind nur einige häufige Beispiele.

 - Bildschirm in H.265 aufnehmen (bessere Qualität), Größe auf 1920 begrenzen,
   Bildrate auf 60fps begrenzen, Audio deaktivieren und Gerät durch Simulation einer
   physischen Tastatur steuern:

    ```bash
    scrcpy --video-codec=h265 --max-size=1920 --max-fps=60 --no-audio --keyboard=uhid
    scrcpy --video-codec=h265 -m1920 --max-fps=60 --no-audio -K  # Kurzversion
    ```

 - VLC in einem neuen virtuellen Display starten (getrennt vom Gerätebildschirm):

    ```bash
    scrcpy --new-display=1920x1080 --start-app=org.videolan.vlc
    ```

 - Gerätekamera in H.265 mit 1920x1080 (und Mikrofon) in eine MP4-Datei
   aufnehmen:

    ```bash
    scrcpy --video-source=camera --video-codec=h265 --camera-size=1920x1080 --record=file.mp4
    ```

 - Front-Kamera des Geräts aufnehmen und als Webcam am Computer bereitstellen (unter
   Linux):

    ```bash
    scrcpy --video-source=camera --camera-size=1920x1080 --camera-facing=front --v4l2-sink=/dev/video2 --no-playback
    ```

 - Gerät ohne Spiegelung durch Simulation einer physischen Tastatur und
   Maus steuern (USB-Debugging nicht erforderlich):

    ```bash
    scrcpy --otg
    ```

 - Gerät mit am Computer angeschlossenen Gamepad-Controllern steuern:

    ```bash
    scrcpy --gamepad=uhid
    scrcpy -G  # Kurzversion
    ```

## Benutzerdokumentation

Die Anwendung bietet viele Funktionen und Konfigurationsoptionen. Diese sind
in den folgenden Seiten dokumentiert:

 - [Verbindung](doc/connection.md)
 - [Video](doc/video.md)
 - [Audio](doc/audio.md)
 - [Steuerung](doc/control.md)
 - [Tastatur](doc/keyboard.md)
 - [Maus](doc/mouse.md)
 - [Gamepad](doc/gamepad.md)
 - [Gerät](doc/device.md)
 - [Fenster](doc/window.md)
 - [Aufnahme](doc/recording.md)
 - [Virtuelles Display](doc/virtual_display.md)
 - [Tunnel](doc/tunnels.md)
 - [OTG](doc/otg.md)
 - [Kamera](doc/camera.md)
 - [Video4Linux](doc/v4l2.md)
 - [Tastenkombinationen](doc/shortcuts.md)


## Ressourcen

 - [FAQ](FAQ.md)
 - [Übersetzungen][wiki] (nicht unbedingt aktuell)
 - [Build-Anleitung](doc/build.md)
 - [Entwickler](doc/develop.md)

[wiki]: https://github.com/Genymobile/scrcpy/wiki


## Artikel

- [Einführung in scrcpy][article-intro]
- [Scrcpy funktioniert jetzt drahtlos][article-tcpip]
- [Scrcpy 2.0, mit Audio][article-scrcpy2]

[article-intro]: https://blog.rom1v.com/2018/03/introducing-scrcpy/
[article-tcpip]: https://www.genymotion.com/blog/open-source-project-scrcpy-now-works-wirelessly/
[article-scrcpy2]: https://blog.rom1v.com/2023/03/scrcpy-2-0-with-audio/

## Kontakt

Sie können ein [Issue] für Fehlerberichte, Funktionswünsche oder allgemeine Fragen öffnen.

Bei Fehlerberichten lesen Sie bitte zuerst die [FAQ](FAQ.md), möglicherweise finden Sie
sofort eine Lösung für Ihr Problem.

[issue]: https://github.com/Genymobile/scrcpy/issues

Sie können auch nutzen:

 - Reddit: [`r/scrcpy`](https://www.reddit.com/r/scrcpy)
 - BlueSky: [`@scrcpy.bsky.social`](https://bsky.app/profile/scrcpy.bsky.social)
 - Twitter: [`@scrcpy_app`](https://twitter.com/scrcpy_app)


## Spenden

Ich bin [@rom1v](https://github.com/rom1v), der Autor und Maintainer von _scrcpy_.

Wenn Sie diese Anwendung schätzen, können Sie [meine Open-Source-Arbeit unterstützen][donate]:
 - [GitHub Sponsors](https://github.com/sponsors/rom1v)
 - [Liberapay](https://liberapay.com/rom1v/)
 - [PayPal](https://paypal.me/rom2v)

[donate]: https://blog.rom1v.com/about/#support-my-open-source-work

## Lizenz

    Copyright (C) 2018 Genymobile
    Copyright (C) 2018-2025 Romain Vimont

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.