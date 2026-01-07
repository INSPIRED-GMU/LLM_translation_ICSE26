# Flask

Flask ist ein leichtgewichtiges [WSGI] Web-Anwendungs-Framework. Es wurde entwickelt,
um einen schnellen und einfachen Einstieg zu ermöglichen und gleichzeitig die Skalierung
zu komplexen Anwendungen zu unterstützen. Es begann als einfacher Wrapper um [Werkzeug]
und [Jinja] und ist zu einem der beliebtesten Python-Web-Anwendungs-Frameworks geworden.

Flask macht Vorschläge, erzwingt aber keine Abhängigkeiten oder
Projektstruktur. Es liegt am Entwickler, die gewünschten Tools und
Bibliotheken auszuwählen. Es gibt viele von der Community bereitgestellte
Erweiterungen, die das Hinzufügen neuer Funktionalität erleichtern.

[WSGI]: https://wsgi.readthedocs.io/
[Werkzeug]: https://werkzeug.palletsprojects.com/
[Jinja]: https://jinja.palletsprojects.com/

## Ein einfaches Beispiel

```python
# speichern Sie dies als app.py
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
```

```
$ flask run
  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

## Spenden

Die Pallets-Organisation entwickelt und unterstützt Flask und die von
ihm verwendeten Bibliotheken. Um die Community der Mitwirkenden und Benutzer
zu vergrößern und den Betreuern mehr Zeit für die Projekte zu ermöglichen,
[spenden Sie bitte heute].

[spenden Sie bitte heute]: https://palletsprojects.com/donate

## Mitwirken

In unserer [detaillierten Dokumentation zum Mitwirken][contrib] finden Sie viele
Möglichkeiten zur Mitarbeit, einschließlich dem Melden von Problemen, dem Anfordern
von Funktionen, dem Stellen oder Beantworten von Fragen und dem Erstellen von PRs.

[contrib]: https://palletsprojects.com/contributing/