# 🦜️🔗 LangChain

⚡ Entwickeln Sie kontextbewusste Reasoning-Anwendungen ⚡

[![Release Notes](https://img.shields.io/github/release/langchain-ai/langchain?style=flat-square)](https://github.com/langchain-ai/langchain/releases)
[![CI](https://github.com/langchain-ai/langchain/actions/workflows/check_diffs.yml/badge.svg)](https://github.com/langchain-ai/langchain/actions/workflows/check_diffs.yml)
[![PyPI - License](https://img.shields.io/pypi/l/langchain-core?style=flat-square)](https://opensource.org/licenses/MIT)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain-core?style=flat-square)](https://pypistats.org/packages/langchain-core)
[![GitHub star chart](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square)](https://star-history.com/#langchain-ai/langchain)
[![Open Issues](https://img.shields.io/github/issues-raw/langchain-ai/langchain?style=flat-square)](https://github.com/langchain-ai/langchain/issues)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode&style=flat-square)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/langchain-ai/langchain)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/langchain-ai/langchain)
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/langchainai.svg?style=social&label=Follow%20%40LangChainAI)](https://twitter.com/langchainai)

Suchen Sie nach der JS/TS-Bibliothek? Schauen Sie sich [LangChain.js](https://github.com/langchain-ai/langchainjs) an.

Um Ihre LangChain-Apps schneller in die Produktion zu bringen, werfen Sie einen Blick auf [LangSmith](https://smith.langchain.com).
[LangSmith](https://smith.langchain.com) ist eine einheitliche Entwicklerplattform zum Erstellen, Testen und Überwachen von LLM-Anwendungen.
Füllen Sie [dieses Formular](https://www.langchain.com/contact-sales) aus, um mit unserem Vertriebsteam zu sprechen.

## Schnellinstallation

Mit pip:

```bash
pip install langchain
```

Mit conda:

```bash
conda install langchain -c conda-forge
```

## 🤔 Was ist LangChain?

**LangChain** ist ein Framework zur Entwicklung von Anwendungen, die von großen Sprachmodellen (LLMs) angetrieben werden.

Für diese Anwendungen vereinfacht LangChain den gesamten Anwendungslebenszyklus:

- **Open-Source-Bibliotheken**: Entwickeln Sie Ihre Anwendungen mit LangChains Open-Source-[Komponenten](https://python.langchain.com/docs/concepts/) und [Drittanbieter-Integrationen](https://python.langchain.com/docs/integrations/providers/).
  Nutzen Sie [LangGraph](https://langchain-ai.github.io/langgraph/) um zustandsbehaftete Agenten mit erstklassigem Streaming und Human-in-the-Loop-Unterstützung zu erstellen.
- **Produktionalisierung**: Untersuchen, überwachen und evaluieren Sie Ihre Apps mit [LangSmith](https://docs.smith.langchain.com/), damit Sie sie ständig optimieren und mit Zuversicht einsetzen können.
- **Bereitstellung**: Verwandeln Sie Ihre LangGraph-Anwendungen in produktionsreife APIs und Assistenten mit der [LangGraph Platform](https://langchain-ai.github.io/langgraph/cloud/).

### Open-Source-Bibliotheken

- **`langchain-core`**: Basis-Abstraktionen.
- **Integrationspakete** (z.B. **`langchain-openai`**, **`langchain-anthropic`**, etc.): Wichtige Integrationen wurden in leichtgewichtige Pakete aufgeteilt, die vom LangChain-Team und den Integrationsentwicklern gemeinsam gepflegt werden.
- **`langchain`**: Chains, Agenten und Retrieval-Strategien, die die kognitive Architektur einer Anwendung bilden.
- **`langchain-community`**: Von der Community gepflegte Drittanbieter-Integrationen.
- **[LangGraph](https://langchain-ai.github.io/langgraph)**: Erstellen Sie robuste und zustandsbehaftete Multi-Aktor-Anwendungen mit LLMs, indem Sie Schritte als Kanten und Knoten in einem Graphen modellieren. Integriert sich nahtlos mit LangChain, kann aber auch ohne verwendet werden. Um mehr über LangGraph zu erfahren, schauen Sie sich unseren ersten LangChain Academy-Kurs *Introduction to LangGraph* [hier](https://academy.langchain.com/courses/intro-to-langgraph) an.

### Produktionalisierung:

- **[LangSmith](https://docs.smith.langchain.com/)**: Eine Entwicklerplattform, die es Ihnen ermöglicht, Chains auf beliebigen LLM-Frameworks zu debuggen, testen, evaluieren und überwachen und sich nahtlos in LangChain integriert.

### Bereitstellung:

- **[LangGraph Platform](https://langchain-ai.github.io/langgraph/cloud/)**: Verwandeln Sie Ihre LangGraph-Anwendungen in produktionsreife APIs und Assistenten.

![Diagramm, das die hierarchische Organisation des LangChain-Frameworks zeigt und die vernetzten Teile über mehrere Ebenen darstellt.](docs/static/svg/langchain_stack_112024.svg#gh-light-mode-only "LangChain Architekturübersicht")
![Diagramm, das die hierarchische Organisation des LangChain-Frameworks zeigt und die vernetzten Teile über mehrere Ebenen darstellt.](docs/static/svg/langchain_stack_112024_dark.svg#gh-dark-mode-only "LangChain Architekturübersicht")

## 🧱 Was können Sie mit LangChain entwickeln?

**❓ Fragen beantworten mit RAG**

- [Dokumentation](https://python.langchain.com/docs/tutorials/rag/)
- End-to-End-Beispiel: [Chat LangChain](https://chat.langchain.com) und [Repository](https://github.com/langchain-ai/chat-langchain)

**🧱 Strukturierte Ausgaben extrahieren**

- [Dokumentation](https://python.langchain.com/docs/tutorials/extraction/)
- End-to-End-Beispiel: [LangChain Extract](https://github.com/langchain-ai/langchain-extract/)

**🤖 Chatbots**

- [Dokumentation](https://python.langchain.com/docs/tutorials/chatbot/)
- End-to-End-Beispiel: [Web LangChain (Web-Researcher-Chatbot)](https://weblangchain.vercel.app) und [Repository](https://github.com/langchain-ai/weblangchain)

Und vieles mehr! Besuchen Sie den [Tutorials](https://python.langchain.com/docs/tutorials/)-Bereich der Dokumentation für weitere Beispiele.

## 🚀 Wie hilft LangChain?

Die wichtigsten Vorteile der LangChain-Bibliotheken sind:

1. **Komponenten**: Kombinierbare Bausteine, Werkzeuge und Integrationen für die Arbeit mit Sprachmodellen. Die Komponenten sind modular und einfach zu verwenden, unabhängig davon, ob Sie den Rest des LangChain-Frameworks nutzen oder nicht.
2. **Einfache Orchestrierung mit LangGraph**: [LangGraph](https://langchain-ai.github.io/langgraph/), aufgebaut auf `langchain-core`, bietet integrierte Unterstützung für [Nachrichten](https://python.langchain.com/docs/concepts/messages/), [Werkzeuge](https://python.langchain.com/docs/concepts/tools/) und andere LangChain-Abstraktionen. Dies macht es einfach, Komponenten zu produktionsreifen Anwendungen mit Persistenz, Streaming und anderen wichtigen Funktionen zu kombinieren. Schauen Sie sich die LangChain [Tutorials-Seite](https://python.langchain.com/docs/tutorials/#orchestration) für Beispiele an.

## Komponenten

Die Komponenten fallen in folgende **Module**:

**📃 Modell-I/O**

Dies umfasst [Prompt-Management](https://python.langchain.com/docs/concepts/prompt_templates/) und eine generische Schnittstelle für [Chat-Modelle](https://python.langchain.com/docs/concepts/chat_models/), einschließlich einer konsistenten Schnittstelle für [Tool-Calling](https://python.langchain.com/docs/concepts/tool_calling/) und [strukturierte Ausgaben](https://python.langchain.com/docs/concepts/structured_outputs/) über verschiedene Modellanbieter hinweg.

**📚 Retrieval**

Retrieval Augmented Generation umfasst das [Laden von Daten](https://python.langchain.com/docs/concepts/document_loaders/) aus verschiedenen Quellen, deren [Aufbereitung](https://python.langchain.com/docs/concepts/text_splitters/), und anschließendes [Suchen (bzw. Abrufen)](https://python.langchain.com/docs/concepts/retrievers/) für die Verwendung im Generierungsschritt.

**🤖 Agenten**

Agenten ermöglichen einem LLM Autonomie darüber, wie eine Aufgabe erfüllt wird. Agenten treffen Entscheidungen über die zu ergreifenden Aktionen, führen diese aus, beobachten das Ergebnis und wiederholen dies, bis die Aufgabe abgeschlossen ist. [LangGraph](https://langchain-ai.github.io/langgraph/) macht es einfach, LangChain-Komponenten zu verwenden, um sowohl [benutzerdefinierte](https://langchain-ai.github.io/langgraph/tutorials/) als auch [eingebaute](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/) LLM-Agenten zu erstellen.

## 📖 Dokumentation

Die vollständige Dokumentation finden Sie [hier](https://python.langchain.com), einschließlich:

- [Einführung](https://python.langchain.com/docs/introduction/): Überblick über das Framework und die Struktur der Dokumentation.
- [Tutorials](https://python.langchain.com/docs/tutorials/): Wenn Sie etwas Bestimmtes entwickeln möchten oder eher praktisch lernen, schauen Sie sich unsere Tutorials an. Dies ist der beste Einstiegspunkt.
- [How-to-Guides](https://python.langchain.com/docs/how_to/): Antworten auf "Wie mache ich...?"-Fragen. Diese Anleitungen sind zielorientiert und konkret; sie sollen Ihnen helfen, eine bestimmte Aufgabe zu erfüllen.
- [Konzeptioneller Leitfaden](https://python.langchain.com/docs/concepts/): Konzeptionelle Erklärungen der wichtigsten Teile des Frameworks.
- [API-Referenz](https://python.langchain.com/api_reference/): Ausführliche Dokumentation jeder Klasse und Methode.

## 🌐 Ökosystem

- [🦜🛠️ LangSmith](https://docs.smith.langchain.com/): Verfolgen und evaluieren Sie Ihre Sprachmodellanwendungen und intelligenten Agenten, um den Übergang von Prototyp zur Produktion zu erleichtern.
- [🦜🕸️ LangGraph](https://langchain-ai.github.io/langgraph/): Erstellen Sie zustandsbehaftete Multi-Aktor-Anwendungen mit LLMs. Integriert sich nahtlos mit LangChain, kann aber auch ohne verwendet werden.
- [🦜🕸️ LangGraph Platform](https://langchain-ai.github.io/langgraph/concepts/#langgraph-platform): Stellen Sie mit LangGraph erstellte LLM-Anwendungen in Produktion bereit.

## 💁 Mitwirken

Als Open-Source-Projekt in einem sich schnell entwickelnden Bereich sind wir sehr offen für Beiträge, sei es in Form neuer Funktionen, verbesserter Infrastruktur oder besserer Dokumentation.

Detaillierte Informationen zum Mitwirken finden Sie [hier](https://python.langchain.com/docs/contributing/).

## 🌟 Mitwirkende

[![langchain contributors](https://contrib.rocks/image?repo=langchain-ai/langchain&max=2000)](https://github.com/langchain-ai/langchain/graphs/contributors)