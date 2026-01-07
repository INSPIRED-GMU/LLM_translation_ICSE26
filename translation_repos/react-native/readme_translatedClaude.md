<h1 align="center">
  <a href="https://reactnative.dev/">
    React Native
  </a>
</h1>

<p align="center">
  <strong>Einmal lernen, überall schreiben:</strong><br>
  Mobile Apps mit React entwickeln.
</p>

<p align="center">
  <a href="https://github.com/facebook/react-native/blob/HEAD/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="React Native wird unter der MIT-Lizenz veröffentlicht." />
  </a>
  <a href="https://circleci.com/gh/facebook/react-native">
    <img src="https://circleci.com/gh/facebook/react-native.svg?style=shield" alt="Aktueller CircleCI Build-Status." />
  </a>
  <a href="https://www.npmjs.org/package/react-native">
    <img src="https://img.shields.io/npm/v/react-native?color=brightgreen&label=npm%20package" alt="Aktuelle npm-Paketversion." />
  </a>
  <a href="https://reactnative.dev/docs/contributing">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs willkommen!" />
  </a>
  <a href="https://twitter.com/intent/follow?screen_name=reactnative">
    <img src="https://img.shields.io/twitter/follow/reactnative.svg?label=Follow%20@reactnative" alt="Folge @reactnative" />
  </a>
</p>

<h3 align="center">
  <a href="https://reactnative.dev/docs/getting-started">Erste Schritte</a>
  <span> · </span>
  <a href="https://reactnative.dev/docs/tutorial">Grundlagen lernen</a>
  <span> · </span>
  <a href="https://reactnative.dev/showcase">Showcase</a>
  <span> · </span>
  <a href="https://reactnative.dev/docs/contributing">Mitwirken</a>
  <span> · </span>
  <a href="https://reactnative.dev/help">Community</a>
  <span> · </span>
  <a href="https://github.com/facebook/react-native/blob/HEAD/.github/SUPPORT.md">Support</a>
</h3>

React Native bringt [**React**s][r] deklaratives UI-Framework zu iOS und Android. Mit React Native verwenden Sie native UI-Steuerelemente und haben vollen Zugriff auf die native Plattform.

- **Deklarativ.** React macht es einfach, interaktive UIs zu erstellen. Deklarative Ansichten machen Ihren Code vorhersehbarer und leichter zu debuggen.
- **Komponentenbasiert.** Erstellen Sie gekapselte Komponenten, die ihren Zustand verwalten, und komponieren Sie sie zu komplexen UIs.
- **Entwicklergeschwindigkeit.** Sehen Sie lokale Änderungen in Sekunden. Änderungen am JavaScript-Code können ohne Neuaufbau der nativen App live neu geladen werden.
- **Portabilität.** Wiederverwenden Sie Code für iOS, Android und [andere Plattformen][p].

React Native wird von vielen Unternehmen und einzelnen Kernmitwirkenden entwickelt und unterstützt. Erfahren Sie mehr in unserem [Ökosystem-Überblick][e].

[r]: https://react.dev/
[p]: https://reactnative.dev/docs/out-of-tree-platforms
[e]: https://github.com/facebook/react-native/blob/HEAD/ECOSYSTEM.md

## Inhalt

- [Anforderungen](#-anforderungen)
- [Ihre erste React Native App erstellen](#-ihre-erste-react-native-app-erstellen)
- [Dokumentation](#-dokumentation)
- [Aktualisierung](#-aktualisierung)
- [Wie Sie beitragen können](#-wie-sie-beitragen-können)
- [Verhaltenskodex](#verhaltenskodex)
- [Lizenz](#-lizenz)

## 📋 Anforderungen

React Native Apps können iOS 15.1 und Android 7.0 (API 24) oder neuer als Ziel haben. Sie können Windows, macOS oder Linux als Entwicklungsbetriebssystem verwenden, wobei das Erstellen und Ausführen von iOS-Apps auf macOS beschränkt ist. Tools wie [Expo](https://expo.dev) können verwendet werden, um dies zu umgehen.

## 🎉 Ihre erste React Native App erstellen

Folgen Sie dem [Erste-Schritte-Leitfaden](https://reactnative.dev/docs/getting-started). Die empfohlene Art, React Native zu installieren, hängt von Ihrem Projekt ab. Hier finden Sie kurze Anleitungen für die häufigsten Szenarien:

- [React Native ausprobieren][hello-world]
- [Eine neue Anwendung erstellen][new-app]
- [React Native zu einer bestehenden Anwendung hinzufügen][existing]

[hello-world]: https://snack.expo.dev/@samples/hello-world
[new-app]: https://reactnative.dev/docs/getting-started
[existing]: https://reactnative.dev/docs/integration-with-existing-apps

## 📖 Dokumentation

Die vollständige Dokumentation für React Native finden Sie auf unserer [Website][docs].

Die React Native-Dokumentation behandelt Komponenten, APIs und Themen, die spezifisch für React Native sind. Weitere Dokumentation zur React-API, die zwischen React Native und React DOM geteilt wird, finden Sie in der [React-Dokumentation][r-docs].

Der Quellcode für die React Native-Dokumentation und Website wird in einem separaten Repository gehostet, [**@facebook/react-native-website**][repo-website].

[docs]: https://reactnative.dev/docs/getting-started
[r-docs]: https://react.dev/learn
[repo-website]: https://github.com/facebook/react-native-website

## 🚀 Aktualisierung

Die Aktualisierung auf neue Versionen von React Native kann Ihnen Zugriff auf mehr APIs, Ansichten, Entwicklertools und andere Vorteile geben. Siehe [Aktualisierungsleitfaden][u] für Anweisungen.

React Native Releases werden [in diesem Diskussions-Repo](https://github.com/reactwg/react-native-releases/discussions) besprochen.

[u]: https://reactnative.dev/docs/upgrading
[repo-releases]: https://github.com/react-native-community/react-native-releases

## 👏 Wie Sie beitragen können

Der Hauptzweck dieses Repositories ist die Weiterentwicklung des React Native-Kerns. Wir möchten das Mitwirken an diesem Projekt so einfach und transparent wie möglich gestalten und sind der Community dankbar für die Beiträge zu Fehlerbehebungen und Verbesserungen. Lesen Sie unten, wie Sie sich an der Verbesserung von React Native beteiligen können.

### [Verhaltenskodex][code]

Facebook hat einen Verhaltenskodex übernommen, den wir von Projektteilnehmern erwarten.
Bitte lesen Sie den [vollständigen Text][code], damit Sie verstehen, welche Handlungen toleriert werden und welche nicht.

[code]: https://code.fb.com/codeofconduct/

### [Mitwirkungsleitfaden][contribute]

Lesen Sie unseren [**Mitwirkungsleitfaden**][contribute], um mehr über unseren Entwicklungsprozess zu erfahren, wie Sie Fehlerbehebungen und Verbesserungen vorschlagen können und wie Sie Ihre Änderungen an React Native erstellen und testen können.

[contribute]: https://reactnative.dev/docs/contributing

### [Open Source Roadmap][roadmap]

Sie können mehr über unsere Vision für React Native in der [**Roadmap**][roadmap] erfahren.

[roadmap]: https://github.com/facebook/react-native/wiki/Roadmap

### Gute erste Issues

Wir haben eine Liste von [guten ersten Issues][gfi], die Bugs enthalten, die einen relativ begrenzten Umfang haben. Dies ist ein guter Ausgangspunkt, um Erfahrungen zu sammeln und sich mit unserem Beitragsprozess vertraut zu machen.

[gfi]: https://github.com/facebook/react-native/labels/good%20first%20issue

### Diskussionen

Größere Diskussionen und Vorschläge werden in [**@react-native-community/discussions-and-proposals**][repo-meta] diskutiert.

[repo-meta]: https://github.com/react-native-community/discussions-and-proposals

## 📄 Lizenz

React Native steht unter der MIT-Lizenz, wie in der [LICENSE][l]-Datei zu finden.

Die React Native-Dokumentation steht unter der Creative Commons-Lizenz, wie in der [LICENSE-docs][ld]-Datei zu finden.

[l]: https://github.com/facebook/react-native/blob/main/LICENSE
[ld]: https://github.com/facebook/react-native/blob/main/LICENSE-docs