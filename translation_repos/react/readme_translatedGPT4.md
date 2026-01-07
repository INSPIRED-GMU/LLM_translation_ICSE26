# [React](https://react.dev/) &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/facebook/react/blob/main/LICENSE) [![npm version](https://img.shields.io/npm/v/react.svg?style=flat)](https://www.npmjs.com/package/react) [![(Runtime) Build and Test](https://github.com/facebook/react/actions/workflows/runtime_build_and_test.yml/badge.svg)](https://github.com/facebook/react/actions/workflows/runtime_build_and_test.yml) [![(Compiler) TypeScript](https://github.com/facebook/react/actions/workflows/compiler_typescript.yml/badge.svg?branch=main)](https://github.com/facebook/react/actions/workflows/compiler_typescript.yml) [![PRs Welcome](https://img.shields.io/badge/PRs-willkommen-brightgreen.svg)](https://legacy.reactjs.org/docs/how-to-contribute.html#your-first-pull-request)

React ist eine JavaScript-Bibliothek zur Erstellung von Benutzeroberflächen.

* **Deklarativ:** React macht es einfach, interaktive UIs zu erstellen. Entwerfe einfache Ansichten für jeden Zustand deiner Anwendung, und React aktualisiert und rendert effizient nur die richtigen Komponenten, wenn sich deine Daten ändern.
* **Komponentenbasiert:** Baue gekapselte Komponenten, die ihren eigenen Zustand verwalten, und kombiniere sie zu komplexen UIs. Da die Logik der Komponenten in JavaScript und nicht in Templates geschrieben ist, kannst du einfach umfangreiche Daten durch deine App reichen.
* **Einmal lernen, überall schreiben:** React trifft keine Annahmen über den Rest deines Tech-Stacks, sodass du neue Funktionen in React entwickeln kannst, ohne vorhandenen Code neu schreiben zu müssen. React kann auch auf dem Server mit [Node](https://nodejs.org/en) gerendert werden und mobile Apps mit [React Native](https://reactnative.dev/) betreiben.

[Erfahre, wie du React in deinem Projekt verwendest](https://react.dev/learn).

## Installation

React wurde von Anfang an für die schrittweise Einführung entwickelt, und **du kannst so wenig oder so viel React verwenden, wie du möchtest**:

* Nutze den [Schnellstart](https://react.dev/learn), um React auszuprobieren.
* [Füge React zu einem bestehenden Projekt hinzu](https://react.dev/learn/add-react-to-an-existing-project).
* [Erstelle eine neue React-App](https://react.dev/learn/start-a-new-react-project), wenn du ein leistungsstarkes JavaScript-Toolset suchst.

## Dokumentation

Die vollständige React-Dokumentation findest du [auf der Website](https://react.dev/).

Die Dokumentation ist in verschiedene Abschnitte unterteilt:

* [Schnellstart](https://react.dev/learn)
* [Tutorial](https://react.dev/learn/tutorial-tic-tac-toe)
* [Thinking in React](https://react.dev/learn/thinking-in-react)
* [Installation](https://react.dev/learn/installation)
* [UI-Beschreibung](https://react.dev/learn/describing-the-ui)
* [Interaktivität hinzufügen](https://react.dev/learn/adding-interactivity)
* [Statusverwaltung](https://react.dev/learn/managing-state)
* [Erweiterte Anleitungen](https://react.dev/learn/escape-hatches)
* [API-Referenz](https://react.dev/reference/react)
* [Unterstützung erhalten](https://react.dev/community)
* [Beitragsrichtlinien](https://legacy.reactjs.org/docs/how-to-contribute.html)

## Beispiele

Hier ist ein erstes Beispiel:

```jsx
import { createRoot } from 'react-dom/client';

function HelloMessage({ name }) {
  return <div>Hello {name}</div>;
}

const root = createRoot(document.getElementById('container'));
root.render(<HelloMessage name="Taylor" />);
```

Dieses Beispiel rendert "Hallo Taylor" in einen Container auf der Seite.

## Beitrag leisten

Die Weiterentwicklung von React erfolgt offen auf GitHub. Lies den [Beitragsleitfaden](https://legacy.reactjs.org/docs/how-to-contribute.html), um mehr zu erfahren.

### [Verhaltenskodex](https://code.fb.com/codeofconduct)

Bitte lies den [vollständigen Verhaltenskodex](https://code.fb.com/codeofconduct), um zu verstehen, welche Handlungen akzeptabel sind.

### [Gute erste Issues](https://github.com/facebook/react/labels/good%20first%20issue)

Um den Einstieg zu erleichtern, gibt es eine Liste von [guten ersten Issues](https://github.com/facebook/react/labels/good%20first%20issue).

## Lizenz

React ist [MIT-lizenziert](./LICENSE).

