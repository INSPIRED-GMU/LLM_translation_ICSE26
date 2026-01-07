# [React](https://react.dev/) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebook/react/blob/main/LICENSE) [![npm version](https://img.shields.io/npm/v/react.svg?style=flat)](https://www.npmjs.com/package/react) [![(Runtime) Build and Test](https://github.com/facebook/react/actions/workflows/runtime_build_and_test.yml/badge.svg)](https://github.com/facebook/react/actions/workflows/runtime_build_and_test.yml) [![(Compiler) TypeScript](https://github.com/facebook/react/actions/workflows/compiler_typescript.yml/badge.svg?branch=main)](https://github.com/facebook/react/actions/workflows/compiler_typescript.yml) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://legacy.reactjs.org/docs/how-to-contribute.html#your-first-pull-request)

React ist eine JavaScript-Bibliothek zum Erstellen von Benutzeroberflächen.

* **Deklarativ:** React macht es einfach, interaktive Benutzeroberflächen zu erstellen. Entwerfen Sie einfache Ansichten für jeden Zustand Ihrer Anwendung, und React wird effizient nur die richtigen Komponenten aktualisieren und rendern, wenn sich Ihre Daten ändern. Deklarative Ansichten machen Ihren Code besser vorhersehbar, einfacher zu verstehen und leichter zu debuggen.
* **Komponentenbasiert:** Bauen Sie gekapselte Komponenten, die ihren eigenen Zustand verwalten, und setzen Sie sie dann zu komplexen Benutzeroberflächen zusammen. Da die Komponentenlogik in JavaScript statt in Templates geschrieben wird, können Sie einfach komplexe Daten durch Ihre App leiten und den Zustand außerhalb des DOMs halten.
* **Einmal lernen, überall einsetzen:** Wir machen keine Annahmen über den Rest Ihres Technologie-Stacks, sodass Sie neue Funktionen in React entwickeln können, ohne bestehenden Code neu zu schreiben. React kann auch serverseitig mit [Node](https://nodejs.org/en) rendern und mobile Apps mit [React Native](https://reactnative.dev/) antreiben.

[Lernen Sie, wie Sie React in Ihrem Projekt verwenden können](https://react.dev/learn).

## Installation

React wurde von Anfang an für eine schrittweise Einführung entwickelt, und **Sie können so wenig oder so viel React verwenden, wie Sie benötigen**:

* Nutzen Sie den [Schnellstart](https://react.dev/learn), um React kennenzulernen.
* [React zu einem bestehenden Projekt hinzufügen](https://react.dev/learn/add-react-to-an-existing-project), um so wenig oder so viel React zu verwenden, wie Sie benötigen.
* [Eine neue React-App erstellen](https://react.dev/learn/start-a-new-react-project), wenn Sie nach einer leistungsstarken JavaScript-Toolchain suchen.

## Dokumentation

Die React-Dokumentation finden Sie [auf der Website](https://react.dev/).

Schauen Sie sich die Seite [Erste Schritte](https://react.dev/learn) für einen schnellen Überblick an.

Die Dokumentation ist in mehrere Abschnitte unterteilt:

* [Schnellstart](https://react.dev/learn)
* [Tutorial](https://react.dev/learn/tutorial-tic-tac-toe)
* [In React denken](https://react.dev/learn/thinking-in-react)
* [Installation](https://react.dev/learn/installation)
* [Die Benutzeroberfläche beschreiben](https://react.dev/learn/describing-the-ui)
* [Interaktivität hinzufügen](https://react.dev/learn/adding-interactivity)
* [Zustand verwalten](https://react.dev/learn/managing-state)
* [Fortgeschrittene Anleitungen](https://react.dev/learn/escape-hatches)
* [API-Referenz](https://react.dev/reference/react)
* [Wo Sie Unterstützung finden](https://react.dev/community)
* [Leitfaden zum Mitwirken](https://legacy.reactjs.org/docs/how-to-contribute.html)

Sie können sie verbessern, indem Sie Pull Requests an [dieses Repository](https://github.com/reactjs/react.dev) senden.

## Beispiele

Wir haben mehrere Beispiele [auf der Website](https://react.dev/). Hier ist das erste, um Ihnen den Einstieg zu erleichtern:

```jsx
import { createRoot } from 'react-dom/client';

function HelloMessage({ name }) {
  return <div>Hello {name}</div>;
}

const root = createRoot(document.getElementById('container'));
root.render(<HelloMessage name="Taylor" />);
```

Dieses Beispiel wird "Hello Taylor" in einen Container auf der Seite rendern.

Sie werden bemerken, dass wir eine HTML-ähnliche Syntax verwendet haben; [wir nennen es JSX](https://react.dev/learn#writing-markup-with-jsx). JSX ist nicht erforderlich, um React zu verwenden, aber es macht den Code besser lesbar, und das Schreiben fühlt sich an wie HTML-Programmierung.

## Mitwirken

Der Hauptzweck dieses Repositories ist die Weiterentwicklung des React-Kerns, um ihn schneller und einfacher in der Verwendung zu machen. Die Entwicklung von React geschieht offen auf GitHub, und wir sind der Community dankbar für Fehlerbehebungen und Verbesserungen. Lesen Sie unten, wie Sie zur Verbesserung von React beitragen können.

### [Verhaltenskodex](https://code.fb.com/codeofconduct)

Meta hat einen Verhaltenskodex eingeführt, den wir von Projektteilnehmern erwarten einzuhalten. Bitte lesen Sie [den vollständigen Text](https://code.fb.com/codeofconduct), damit Sie verstehen, welche Handlungen toleriert werden und welche nicht.

### [Leitfaden zum Mitwirken](https://legacy.reactjs.org/docs/how-to-contribute.html)

Lesen Sie unseren [Leitfaden zum Mitwirken](https://legacy.reactjs.org/docs/how-to-contribute.html), um mehr über unseren Entwicklungsprozess zu erfahren, wie Sie Fehlerbehebungen und Verbesserungen vorschlagen können und wie Sie Ihre Änderungen an React erstellen und testen können.

### [Gute erste Issues](https://github.com/facebook/react/labels/good%20first%20issue)

Um Ihnen den Einstieg zu erleichtern und Sie mit unserem Beitragsprozess vertraut zu machen, haben wir eine Liste von [guten ersten Issues](https://github.com/facebook/react/labels/good%20first%20issue), die Fehler mit relativ begrenztem Umfang enthalten. Dies ist ein guter Ausgangspunkt.

### Lizenz

React steht unter der [MIT-Lizenz](./LICENSE).