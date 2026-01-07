= Elasticsearch

Elasticsearch ist eine verteilte Such- und Analyse-Engine, ein skalierbarer Datenspeicher und eine Vektordatenbank, die für Geschwindigkeit und Relevanz bei produktionsreifen Workloads optimiert ist. Elasticsearch bildet die Grundlage der offenen Stack-Plattform von Elastic. Suche nahezu in Echtzeit in riesigen Datensätzen, führe Vektorsuchen durch, integriere generative KI-Anwendungen und vieles mehr.

Durch Elasticsearch ermöglichte Anwendungsfälle umfassen:

* https://www.elastic.co/search-labs/blog/articles/retrieval-augmented-generation-rag[Retrieval Augmented Generation (RAG)]
* https://www.elastic.co/search-labs/blog/categories/vector-search[Vektorsuche]
* Volltextsuche
* Logs
* Metriken
* Application Performance Monitoring (APM)
* Sicherheitsprotokolle

... und mehr!

Um mehr über die Funktionen und Möglichkeiten von Elasticsearch zu erfahren, besuche unsere https://www.elastic.co/products/elasticsearch[Produktseite].

Weitere Informationen zu https://www.elastic.co/search-labs/blog/categories/ml-research[Machine Learning-Innovationen] und den neuesten https://www.elastic.co/search-labs/blog/categories/lucene[Lucene-Beiträgen von Elastic] findest du in den https://www.elastic.co/search-labs[Search Labs].

== Erste Schritte

Der einfachste Weg, Elasticsearch einzurichten, ist die Erstellung einer verwalteten Bereitstellung mit dem https://www.elastic.co/cloud/as-a-service[Elasticsearch Service auf Elastic Cloud].

Wenn du Elasticsearch lieber selbst installieren und verwalten möchtest, kannst du die neueste Version von https://www.elastic.co/downloads/elasticsearch[elastic.co/downloads/elasticsearch] herunterladen.

=== Elasticsearch lokal ausführen

[WARNUNG]
====
VERWENDE DIESE ANLEITUNG NICHT FÜR PRODUKTIVBEREITSTELLUNGEN.

Dieses Setup ist nur für lokale Entwicklung und Tests gedacht.
====

Richte Elasticsearch und Kibana schnell in Docker für die lokale Entwicklung oder Tests mit dem https://github.com/elastic/start-local?tab=readme-ov-file#-try-elasticsearch-and-kibana-locally[`start-local`-Skript] ein.

ℹ️ Für detailliertere Informationen zum `start-local`-Setup siehe das https://github.com/elastic/start-local[README auf GitHub].

==== Voraussetzungen

- Falls Docker nicht installiert ist, https://www.docker.com/products/docker-desktop[lade Docker Desktop herunter und installiere es] für dein Betriebssystem.
- Für Microsoft Windows, installiere das https://learn.microsoft.com/en-us/windows/wsl/install[Windows Subsystem für Linux (WSL)].

==== Testlizenz

Dieses Setup enthält eine einmonatige Testlizenz, die alle Elastic-Funktionen umfasst.

Nach der Testphase wechselt die Lizenz zu *Kostenlos und offen - Basis*.
Weitere Informationen findest du unter https://www.elastic.co/subscriptions[Elastic-Abonnements].

==== `start-local` ausführen

Um Elasticsearch und Kibana lokal einzurichten, führe das `start-local`-Skript aus:

[source,sh]
----
curl -fsSL https://elastic.co/start-local | sh
----

Dieses Skript erstellt einen `elastic-start-local`-Ordner mit Konfigurationsdateien und startet sowohl Elasticsearch als auch Kibana in Docker.

Nach der Ausführung des Skripts kannst du Elastic-Dienste über folgende Endpunkte aufrufen:

* *Elasticsearch*: http://localhost:9200
* *Kibana*: http://localhost:5601

==== API-Zugriff

Ein API-Schlüssel für Elasticsearch wird generiert und in der `.env`-Datei als `ES_LOCAL_API_KEY` gespeichert.
Verwende diesen Schlüssel, um mit einem https://www.elastic.co/guide/en/elasticsearch/client/index.html[Programmiersprachen-Client] oder der https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html[REST-API] eine Verbindung zu Elasticsearch herzustellen.

[source,sh]
----
source .env
curl $ES_LOCAL_URL -H "Authorization: ApiKey ${ES_LOCAL_API_KEY}"
----

=== Anfragen an Elasticsearch senden

Du sendest Daten und andere Anfragen an Elasticsearch über REST-APIs.
Interagiere mit Elasticsearch mit jedem Client, der HTTP-Anfragen sendet, z.B. mit https://curl.se[curl].

==== Mit curl

Beispielbefehl zum Erstellen eines neuen Elasticsearch-Index mit Basic Auth:

[source,sh]
----
curl -u elastic:$ELASTIC_PASSWORD \
  -X PUT \
  http://localhost:9200/my-new-index \
  -H 'Content-Type: application/json'
----

==== Mit einem Sprachclient

Beispiel mit Python:

[source,python]
----
import os
from elasticsearch import Elasticsearch

username = 'elastic'
password = os.getenv('ELASTIC_PASSWORD')

client = Elasticsearch(
    "http://localhost:9200",
    basic_auth=(username, password)
)

print(client.info())
----

==== Daten hinzufügen

Einzelnes Dokument hinzufügen:

----
POST /customer/_doc/1
{
  "firstname": "Jennifer",
  "lastname": "Walters"
}
----

==== Suchen

Suche nach Dokumenten mit dem Vornamen _Jennifer_:

----
GET /customer/_search
{
  "query": {
    "match": { "firstname": "Jennifer" }
  }
}
----

== Upgrade

Für ein Upgrade siehe die https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html[Upgrade-Dokumentation].

== Von der Quelle bauen

Elasticsearch nutzt https://gradle.org[Gradle] als Build-System:

[source,sh]
----
./gradlew localDistro
----

== Dokumentation

Die vollständige Dokumentation findest du unter https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html[elastic.co].

== Mitwirken

Für Beitragsrichtlinien siehe xref:CONTRIBUTING.md[CONTRIBUTING].

== Fragen? Probleme? Vorschläge?

* Melde Fehler oder wünsche Funktionen über https://github.com/elastic/elasticsearch/issues/new/choose[GitHub Issues].
* Hol dir Hilfe im https://discuss.elastic.co[Elastic-Forum] oder bei https://ela.st/slack[Slack].

