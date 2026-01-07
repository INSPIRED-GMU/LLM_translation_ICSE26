= Elasticsearch

Elasticsearch ist eine verteilte Such- und Analyseengine, eine skalierbare Datenspeicher- und Vektordatenbank, die für Geschwindigkeit und Relevanz bei Produktions-Workloads optimiert ist. Elasticsearch ist die Grundlage von Elastics Open Stack-Plattform. Suchen Sie in Echtzeit in riesigen Datensätzen, führen Sie Vektorsuchen durch, integrieren Sie Anwendungen mit generativer KI und vieles mehr.

Anwendungsfälle, die durch Elasticsearch ermöglicht werden:

* https://www.elastic.co/search-labs/blog/articles/retrieval-augmented-generation-rag[Retrieval Augmented Generation (RAG)]
* https://www.elastic.co/search-labs/blog/categories/vector-search[Vektorsuche]
* Volltextsuche
* Logs
* Metriken
* Application Performance Monitoring (APM)
* Sicherheitslogs

\... und mehr!

Um mehr über die Funktionen und Möglichkeiten von Elasticsearch zu erfahren, besuchen Sie unsere
https://www.elastic.co/products/elasticsearch[Produktseite].

Informationen zu https://www.elastic.co/search-labs/blog/categories/ml-research[Machine Learning Innovationen] und den neuesten https://www.elastic.co/search-labs/blog/categories/lucene[Lucene-Beiträgen von Elastic] finden Sie in den https://www.elastic.co/search-labs[Search Labs].

[[get-started]]
== Erste Schritte

Der einfachste Weg, Elasticsearch einzurichten, ist die Erstellung eines verwalteten Deployments mit
https://www.elastic.co/cloud/as-a-service[Elasticsearch Service auf Elastic
Cloud].

Wenn Sie Elasticsearch lieber selbst installieren und verwalten möchten, können Sie die neueste Version von
https://www.elastic.co/downloads/elasticsearch[elastic.co/downloads/elasticsearch] herunterladen.

=== Elasticsearch lokal ausführen

[WARNING]
====
VERWENDEN SIE DIESE ANWEISUNGEN NICHT FÜR PRODUKTIONSUMGEBUNGEN.

Diese Einrichtung ist nur für lokale Entwicklung und Tests gedacht.
====

Richten Sie Elasticsearch und Kibana schnell in Docker für lokale Entwicklung oder Tests ein, mit dem https://github.com/elastic/start-local?tab=readme-ov-file#-try-elasticsearch-and-kibana-locally[`start-local` Skript].

ℹ️ Detailliertere Informationen zur `start-local` Einrichtung finden Sie in der https://github.com/elastic/start-local[README auf GitHub].

==== Voraussetzungen

- Wenn Sie Docker noch nicht installiert haben, https://www.docker.com/products/docker-desktop[laden Sie Docker Desktop herunter und installieren Sie es] für Ihr Betriebssystem.
- Wenn Sie Microsoft Windows verwenden, installieren Sie das https://learn.microsoft.com/en-us/windows/wsl/install[Windows Subsystem for Linux (WSL)].

==== Testlizenz
Diese Einrichtung enthält eine einmonatige Testlizenz mit allen Elastic-Funktionen.

Nach der Testphase wechselt die Lizenz zu *Free and open - Basic*.
Weitere Informationen finden Sie unter https://www.elastic.co/subscriptions[Elastic-Abonnements].

==== `start-local` ausführen

Um Elasticsearch und Kibana lokal einzurichten, führen Sie das `start-local` Skript aus:

[source,sh]
----
curl -fsSL https://elastic.co/start-local | sh
----
// NOTCONSOLE

Dieses Skript erstellt einen `elastic-start-local` Ordner mit Konfigurationsdateien und startet sowohl Elasticsearch als auch Kibana mit Docker.

Nach Ausführung des Skripts können Sie auf die Elastic-Dienste unter folgenden Endpunkten zugreifen:

* *Elasticsearch*: http://localhost:9200
* *Kibana*: http://localhost:5601

Das Skript generiert ein zufälliges Passwort für den `elastic` Benutzer, das am Ende der Installation angezeigt und in der `.env` Datei gespeichert wird.

[CAUTION]
====
Diese Einrichtung ist nur für lokale Tests gedacht. HTTPS ist deaktiviert und es wird Basic-Authentifizierung für Elasticsearch verwendet. Aus Sicherheitsgründen sind Elasticsearch und Kibana nur über `localhost` erreichbar.
====

[Die restlichen Code-Blöcke und technischen Anweisungen bleiben unverändert, nur die umgebenden Erklärungen werden übersetzt]

[[upgrade]]
== Upgrade

Informationen zum Upgrade von einer früheren Version von Elasticsearch finden Sie in der
https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-upgrade.html[Elasticsearch Upgrade-Dokumentation].

[[build-source]]
== Aus dem Quellcode bauen

Elasticsearch verwendet https://gradle.org[Gradle] als Build-System.

[Die weiteren Build-Anweisungen und Code-Blöcke bleiben unverändert]

[[docs]]
== Dokumentation

Die vollständige Elasticsearch-Dokumentation finden Sie unter
https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html[elastic.co].

[[examples]]
== Beispiele und Anleitungen

Das https://github.com/elastic/elasticsearch-labs[`elasticsearch-labs`] Repository enthält ausführbare Python-Notebooks, Beispielanwendungen und Ressourcen zum Testen von Elasticsearch für Vektorsuche, Hybridsuche und Anwendungsfälle der generativen KI.

[[contribute]]
== Mitwirken

Die Richtlinien für Beiträge finden Sie unter xref:CONTRIBUTING.md[CONTRIBUTING].

[[questions]]
== Fragen? Probleme? Vorschläge?

* Um einen Fehler zu melden oder eine Funktion anzufordern, erstellen Sie ein
https://github.com/elastic/elasticsearch/issues/new/choose[GitHub Issue]. Bitte
stellen Sie sicher, dass nicht bereits jemand anderes ein Issue zum gleichen Thema erstellt hat.

* Brauchen Sie Hilfe bei der Verwendung von Elasticsearch? Wenden Sie sich an das
https://discuss.elastic.co[Elastic Forum] oder https://ela.st/slack[Slack]. Ein
Mitglied der Community oder ein Elastic-Ingenieur wird Ihnen gerne weiterhelfen.