```markdown
<h1 align="center">
  <a href="https://reactnative.dev/">
    React Native
  </a>
</h1>

<p align="center">
  <strong>Einmal lernen, überall schreiben:</strong><br>
  Erstellen Sie mobile Apps mit React.
</p>

<p align="center">
  <a href="https://github.com/facebook/react-native/blob/HEAD/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="React Native ist unter der MIT-Lizenz veröffentlicht." />
  </a>
  <a href="https://circleci.com/gh/facebook/react-native">
    <img src="https://circleci.com/gh/facebook/react-native.svg?style=shield" alt="Aktueller CircleCI-Build-Status." />
  </a>
  <a href="https://www.npmjs.org/package/react-native">
    <img src="https://img.shields.io/npm/v/react-native?color=brightgreen&label=npm%20package" alt="Aktuelle npm-Paketversion." />
  </a>
  <a href="https://reactnative.dev/docs/contributing">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs willkommen!" />
  </a>
  <a href="https://twitter.com/intent/follow?screen_name=reactnative">
    <img src="https://img.shields.io/twitter/follow/reactnative.svg?label=Follow%20@reactnative" alt="Follow @reactnative" />
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

React Native bringt [**React**'s][r] deklaratives UI-Framework zu iOS und Android. Mit React Native verwenden Sie native UI-Elemente und haben vollen Zugriff auf die native Plattform.

- **Deklarativ.** React macht es einfach, interaktive UIs zu erstellen. Deklarative Ansichten machen Ihren Code vorhersehbarer und leichter zu debuggen.
- **Komponentenbasiert.** Erstellen Sie gekapselte Komponenten, die ihren Zustand verwalten, und kombinieren Sie diese, um komplexe UIs zu erstellen.
- **Entwicklergeschwindigkeit.** Sehen Sie Änderungen lokal innerhalb von Sekunden. Änderungen am JavaScript-Code können live neu geladen werden, ohne die native App neu zu bauen.
- **Portabilität.** Verwenden Sie denselben Code für iOS, Android und [andere Plattformen][p].

React Native wird von vielen Unternehmen und individuellen Hauptbeiträgern entwickelt und unterstützt. Erfahren Sie mehr in unserer [Übersicht zum Ökosystem][e].

[r]: https://react.dev/
[p]: https://reactnative.dev/docs/out-of-tree-platforms
[e]: https://github.com/facebook/react-native/blob/HEAD/ECOSYSTEM.md

## Inhaltsverzeichnis

- [Anforderungen](#-anforderungen)
- [Erstellung Ihrer ersten React Native App](#-erstellung-ihrer-ersten-react-native-app)
- [Dokumentation](#-dokumentation)
- [Aktualisierung](#-aktualisierung)
- [Wie man beiträgt](#-wie-man-beiträgt)
- [Verhaltenskodex](#verhaltenskodex)
- [Lizenz](#-lizenz)

## 📋 Anforderungen

React Native-Apps können iOS 15.1 und Android 7.0 (API 24) oder neuer anvisieren. Sie können Windows, macOS oder Linux als Entwicklungsbetriebssystem verwenden, obwohl das Erstellen und Ausführen von iOS-Apps auf macOS beschränkt ist. Tools wie [Expo](https://expo.dev) können genutzt werden, um dies zu umgehen.

## 🎉 Erstellung Ihrer ersten React Native App

Folgen Sie dem [Guide für den Einstieg](https://reactnative.dev/docs/getting-started). Die empfohlene Installationsmethode hängt von Ihrem Projekt ab. Hier finden Sie kurze Anleitungen für die häufigsten Szenarien:

- [React Native ausprobieren][hello-world]
- [Erstellung einer neuen Anwendung][new-app]
- [Hinzufügen von React Native zu einer bestehenden Anwendung][existing]

[hello-world]: https://snack.expo.dev/@samples/hello-world
[new-app]: https://reactnative.dev/docs/getting-started
[existing]: https://reactnative.dev/docs/integration-with-existing-apps

## 📖 Dokumentation

Die vollständige Dokumentation zu React Native finden Sie auf unserer [Website][docs].

Die React Native-Dokumentation behandelt Komponenten, APIs und Themen, die spezifisch für React Native sind. Für weitere Dokumentationen zur React-API, die zwischen React Native und React DOM geteilt wird, sehen Sie in der [React-Dokumentation][r-docs] nach.

Der Quellcode für die React Native-Dokumentation und -Website ist in einem separaten Repository untergebracht, [**@facebook/react-native-website**][repo-website].

[docs]: https://reactnative.dev/docs/getting-started
[r-docs]: https://react.dev/learn
[repo-website]: https://github.com/facebook/react-native-website

## 🚀 Aktualisierung

Aktualisierungen auf neue Versionen von React Native können Ihnen Zugang zu mehr APIs, Ansichten, Entwicklertools und weiteren Vorteilen bieten. Anweisungen finden Sie im [Aktualisierungsleitfaden][u].

React Native-Versionen werden [in diesem Diskussionsrepo](https://github.com/reactwg/react-native-releases/discussions) besprochen.

[u]: https://reactnative.dev/docs/upgrading
[repo-releases]: https://github.com/react-native-community/react-native-releases

## 👏 Wie man beiträgt

Der Hauptzweck dieses Repositories ist die kontinuierliche Weiterentwicklung des React Native-Kerns. Wir möchten das Beitragen zu diesem Projekt so einfach und transparent wie möglich machen und sind der Community dankbar für Fehlerbehebungen und Verbesserungen. Lesen Sie unten, wie Sie zur Verbesserung von React Native beitragen können.

### [Verhaltenskodex][code]

Facebook hat einen Verhaltenskodex angenommen, den wir von den Projektteilnehmern erwarten.
Bitte lesen Sie den [vollständigen Text][code], um zu verstehen, welche Aktionen toleriert werden und welche nicht.

[code]: https://code.fb.com/codeofconduct/

### [Beitragsrichtlinien][contribute]

Lesen Sie unseren [**Beitragsleitfaden**][contribute], um mehr über unseren Entwicklungsprozess, das Vorschlagen von Fehlerbehebungen und Verbesserungen sowie das Erstellen und Testen Ihrer Änderungen zu erfahren.

[contribute]: https://reactnative.dev/docs/contributing

### [Open Source Roadmap][roadmap]

Erfahren Sie mehr über unsere Vision für React Native in der [**Roadmap**][roadmap].

[roadmap]: https://github.com/facebook/react-native/wiki/Roadmap

### Gute erste Probleme

Wir haben eine Liste von [guten ersten Problemen][gfi], die Fehler mit relativ begrenztem Umfang enthalten. Dies ist ein großartiger Ausgangspunkt, um Erfahrung zu sammeln und sich mit unserem Beitragssystem vertraut zu machen.

[gfi]: https://github.com/facebook/react-native/labels/good%20first%20issue

### Diskussionen

Größere Diskussionen und Vorschläge werden in [**@react-native-community/discussions-and-proposals**][repo-meta] behandelt.

[repo-meta]: https://github.com/react-native-community/discussions-and-proposals

## 📄 Lizenz

React Native ist MIT-lizenziert, wie in der [LICENSE][l]-Datei zu finden.

Die React Native-Dokumentation ist unter der Creative Commons-Lizenz lizenziert, wie in der [LICENSE-docs][ld]-Datei beschrieben.

[l]: https://github.com/facebook/react-native/blob/main/LICENSE
[ld]: https://github.com/facebook/react-native/blob/main/LICENSE-docs
```