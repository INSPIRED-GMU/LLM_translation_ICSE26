# Flask

Flask ist ein leichtgewichtiges [WSGI]-Webanwendungs-Framework. Es ist darauf ausgelegt, den Einstieg schnell und einfach zu gestalten, mit der Möglichkeit, zu komplexen Anwendungen zu skalieren. Ursprünglich begann es als einfacher Wrapper um [Werkzeug] und [Jinja] und hat sich zu einem der beliebtesten Python-Webframeworks entwickelt.

Flask gibt Empfehlungen, erzwingt jedoch keine Abhängigkeiten oder Projektstruktur. Es liegt beim Entwickler, die Werkzeuge und Bibliotheken auszuwählen, die er verwenden möchte. Die Community stellt viele Erweiterungen bereit, die das Hinzufügen neuer Funktionen erleichtern.

[WSGI]: https://wsgi.readthedocs.io/
[Werkzeug]: https://werkzeug.palletsprojects.com/
[Jinja]: https://jinja.palletsprojects.com/

## Ein Einfaches Beispiel

```python
# Speichern Sie dies als app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

```
$ flask run
  * Läuft auf http://127.0.0.1:5000/ (Drücken Sie STRG+C zum Beenden)
```

## Spenden

Die Pallets-Organisation entwickelt und unterstützt Flask und die Bibliotheken, die es verwendet. Um die Community von Mitwirkenden und Nutzern zu vergrößern und den Maintainern zu ermöglichen, mehr Zeit in die Projekte zu investieren, [bitte heute spenden].

[bitte heute spenden]: https://palletsprojects.com/donate

## Mitwirken

Siehe unsere [ausführliche Mitwirkungsdokumentation][contrib] für viele Möglichkeiten zur Beteiligung, darunter das Melden von Problemen, das Anfordern von Funktionen, das Stellen oder Beantworten von Fragen und das Erstellen von Pull Requests.

[contrib]: https://palletsprojects.com/contributing/

