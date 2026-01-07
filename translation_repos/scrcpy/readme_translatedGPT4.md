**Dieses GitHub-Repository (<https://github.com/Genymobile/scrcpy>) ist die einzige offizielle Quelle für das Projekt. Lade keine Releases von zufälligen Websites herunter, selbst wenn deren Name `scrcpy` enthält.**

# scrcpy (v3.1)

<img src="app/data/icon.svg" width="128" height="128" alt="scrcpy" align="right" />

_ausgesprochen "**scr**een **c**o**py**"_

Diese Anwendung spiegelt Android-Geräte (Video und Audio), die über USB oder [über TCP/IP](doc/connection.md#tcpip-wireless) verbunden sind, und ermöglicht die Steuerung des Geräts mit der Tastatur und Maus des Computers. Root-Zugriff ist nicht erforderlich. Es funktioniert unter _Linux_, _Windows_ und _macOS_.

![Screenshot](assets/screenshot-debian-600.jpg)

Schwerpunkte:

 - **Leichtgewichtigkeit**: nativ, zeigt nur den Gerätescreen
 - **Leistung**: 30~120fps, abhängig vom Gerät
 - **Qualität**: 1920×1080 oder höher
 - **Niedrige Latenz**: [35~70ms][lowlatency]
 - **Schneller Start**: ~1 Sekunde bis zum ersten Bild
 - **Nicht-invasiv**: Es wird nichts auf dem Android-Gerät installiert
 - **Benutzerfreundlichkeit**: kein Konto, keine Werbung, keine Internetverbindung nötig
 - **Freiheit**: freie und Open-Source-Software

[lowlatency]: https://github.com/Genymobile/scrcpy/pull/646

## Voraussetzungen

Das Android-Gerät benötigt mindestens API 21 (Android 5.0).

[Audio-Weiterleitung](doc/audio.md) wird ab API 30 (Android 11+) unterstützt.

Stelle sicher, dass du das [USB-Debugging aktiviert][enable-adb] hast.

[enable-adb]: https://developer.android.com/studio/debug/dev-options#enable

Bei einigen Geräten (insbesondere Xiaomi) kann folgender Fehler auftreten:

```
java.lang.SecurityException: Injecting input events requires the caller (or the source of the instrumentation, if any) to have the INJECT_EVENTS permission.
```

In diesem Fall musst du eine zusätzliche Option aktivieren: [USB-Debugging (Sicherheitseinstellungen)][control]. Danach ist ein Neustart des Geräts erforderlich.

[control]: https://github.com/Genymobile/scrcpy/issues/70#issuecomment-373286323

USB-Debugging ist nicht erforderlich, um scrcpy im [OTG-Modus](doc/otg.md) zu verwenden.

## Anwendung herunterladen

 - [Linux](doc/linux.md)
 - [Windows](doc/windows.md)
 - [macOS](doc/macos.md)

## Nützliche Tipps

 - [Reduziere die Auflösung](doc/video.md#size) für bessere Leistung (`scrcpy -m1024`)
 - [_Rechtsklick_](doc/mouse.md#mouse-bindings) aktiviert `BACK`
 - [_Mittelklick_](doc/mouse.md#mouse-bindings) aktiviert `HOME`
 - <kbd>Alt</kbd>+<kbd>f</kbd> wechselt in den [Vollbildmodus](doc/window.md#fullscreen)

## Anwendungsbeispiele

 - Bildschirmaufnahme in H.265, Größe auf 1920 begrenzt:

    ```bash
    scrcpy --video-codec=h265 --max-size=1920 --max-fps=60 --no-audio --keyboard=uhid
    ```

 - VLC in einem neuen virtuellen Display starten:

    ```bash
    scrcpy --new-display=1920x1080 --start-app=org.videolan.vlc
    ```

 - Gerät steuern ohne Spiegelung im OTG-Modus:

    ```bash
    scrcpy --otg
    ```

## Lizenz

    Copyright (C) 2018 Genymobile
    Copyright (C) 2018-2025 Romain Vimont

    Lizenziert unter der Apache License, Version 2.0.
    Sie können eine Kopie der Lizenz unter folgendem Link einsehen:

        http://www.apache.org/licenses/LICENSE-2.0

    Soweit nicht durch geltendes Recht vorgeschrieben oder schriftlich vereinbart,
    wird die Software "wie besehen" bereitgestellt, ohne jegliche Garantien.

