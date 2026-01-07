= Spring Boot image:https://github.com/spring-projects/spring-boot/actions/workflows/build-and-deploy-snapshot.yml/badge.svg?branch=main["Build Status", link="https://github.com/spring-projects/spring-boot/actions/workflows/build-and-deploy-snapshot.yml?query=branch%3Amain"] image:https://img.shields.io/badge/Revved%20up%20by-Develocity-06A0CE?logo=Gradle&labelColor=02303A["Revved up by Develocity", link="https://ge.spring.io/scans?&search.rootProjectNames=Spring%20Boot%20Build&search.rootProjectNames=spring-boot-build"]

:docs: https://docs.spring.io/spring-boot
:github: https://github.com/spring-projects/spring-boot

Spring Boot hilft Ihnen dabei, Spring-basierte Produktionsanwendungen und -dienste mit minimalem Aufwand zu erstellen.
Es bietet eine vorgegebene Sichtweise auf die Spring-Plattform, sodass neue und bestehende Benutzer schnell zu den benötigten Funktionen gelangen können.

Sie können Spring Boot verwenden, um eigenständige Java-Anwendungen zu erstellen, die mit `java -jar` gestartet werden können, oder traditionellere WAR-Deployments.
Wir bieten auch ein Kommandozeilen-Tool an, das Spring-Skripte ausführt.

Unsere primären Ziele sind:

* Eine radikal schnellere und besser zugängliche Einstiegserfahrung für die gesamte Spring-Entwicklung bieten.
* Meinungsstark sein, aber schnell aus dem Weg gehen, sobald die Anforderungen von den Standardeinstellungen abweichen.
* Eine Reihe von nicht-funktionalen Features bereitstellen, die für große Projektklassen üblich sind (zum Beispiel eingebettete Server, Sicherheit, Metriken, Gesundheitsprüfungen, externalisierte Konfiguration).
* Absolut keine Codegenerierung und keine Notwendigkeit für XML-Konfiguration.

== Installation und Erste Schritte

Die {docs}[Referenzdokumentation] enthält detaillierte {docs}/installing.html[Installationsanweisungen] sowie eine umfassende {docs}/tutorial/first-application/index.html[``Erste Schritte``] Anleitung.

Hier ist ein kurzer Einblick in eine vollständige Spring Boot Anwendung in Java:

[source,java]
----
import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.web.bind.annotation.*;

@RestController
@SpringBootApplication
public class Example {

	@RequestMapping("/")
	String home() {
		return "Hello World!";
	}

	public static void main(String[] args) {
		SpringApplication.run(Example.class, args);
	}

}
----

== Hilfe erhalten

Haben Sie Probleme mit Spring Boot? Wir möchten helfen!

* Prüfen Sie die {docs}/[Referenzdokumentation], besonders die {docs}/how-to/index.html[How-to's] -- sie bieten Lösungen für die häufigsten Fragen.
* Lernen Sie die Spring-Grundlagen -- Spring Boot baut auf vielen anderen Spring-Projekten auf; besuchen Sie die https://spring.io[spring.io] Website für umfangreiche Referenzdokumentation.
  Wenn Sie neu bei Spring sind, versuchen Sie einen der https://spring.io/guides[Leitfäden].
* Wenn Sie ein Upgrade durchführen, lesen Sie die {github}/wiki[Release Notes] für Upgrade-Anweisungen und "neue und bemerkenswerte" Funktionen.
* Stellen Sie eine Frage -- wir überwachen https://stackoverflow.com[stackoverflow.com] für Fragen, die mit https://stackoverflow.com/tags/spring-boot[`spring-boot`] getaggt sind.
* Melden Sie Bugs mit Spring Boot unter {github}/issues[github.com/spring-projects/spring-boot/issues].

== Probleme melden

Spring Boot verwendet GitHubs integriertes Issue-Tracking-System zur Erfassung von Bugs und Feature-Anfragen.
Wenn Sie ein Problem melden möchten, befolgen Sie bitte die nachstehenden Empfehlungen:

* Bevor Sie einen Bug melden, durchsuchen Sie bitte den {github}/issues[Issue Tracker], um zu sehen, ob jemand das Problem bereits gemeldet hat.
* Wenn das Problem noch nicht existiert, {github}/issues/new[erstellen Sie ein neues Issue].
* Bitte stellen Sie so viele Informationen wie möglich mit dem Problem-Bericht zur Verfügung.
Wir möchten die Spring Boot Version, das Betriebssystem und die JVM-Version wissen, die Sie verwenden.
* Wenn Sie Code oder einen Stack Trace einfügen müssen, verwenden Sie Markdown.
+++```+++ vor und nach Ihrem Text.
* Wenn möglich, versuchen Sie einen Testfall oder ein Projekt zu erstellen, das das Problem reproduziert, und hängen Sie es an das Issue an.

== Aus den Quellen bauen

Sie müssen nicht aus den Quellen bauen, um Spring Boot zu nutzen (Binaries in https://repo.spring.io[repo.spring.io]), aber wenn Sie die neuesten und besten Funktionen ausprobieren möchten, kann Spring Boot mit dem https://docs.gradle.org/current/userguide/gradle_wrapper.html[Gradle Wrapper] gebaut und in Ihrem lokalen Maven-Cache veröffentlicht werden.
Sie benötigen auch JDK 17.

[source,shell]
----
$ ./gradlew publishToMavenLocal
----

Dies wird alle JARs und Dokumentation erstellen und sie in Ihrem lokalen Maven-Cache veröffentlichen.
Es werden keine Tests ausgeführt.
Wenn Sie alles bauen möchten, verwenden Sie den `build` Task:

[source,shell]
----
$ ./gradlew build
----

== Module

Es gibt mehrere Module in Spring Boot. Hier ist ein kurzer Überblick:

=== spring-boot

Die Hauptbibliothek, die Funktionen bereitstellt, die die anderen Teile von Spring Boot unterstützen. Dazu gehören:

* Die `SpringApplication` Klasse, die statische Convenience-Methoden bereitstellt, die verwendet werden können, um eine eigenständige Spring-Anwendung zu schreiben.
  Ihre einzige Aufgabe ist es, einen angemessenen Spring `ApplicationContext` zu erstellen und zu aktualisieren.
* Eingebettete Webanwendungen mit einer Auswahl an Containern (Tomcat, Jetty oder Undertow).
* Erstklassige externalisierte Konfigurationsunterstützung.
* Praktische `ApplicationContext` Initialisierer, einschließlich Unterstützung für sinnvolle Logging-Standardeinstellungen.

=== spring-boot-autoconfigure

Spring Boot kann große Teile typischer Anwendungen basierend auf dem Inhalt ihres Classpaths konfigurieren.
Eine einzelne `@EnableAutoConfiguration` Annotation löst die Auto-Konfiguration des Spring-Kontexts aus.

Die Auto-Konfiguration versucht zu ermitteln, welche Beans ein Benutzer benötigen könnte. Wenn zum Beispiel `HSQLDB` im Classpath ist und der Benutzer keine Datenbankverbindungen konfiguriert hat, dann möchte er wahrscheinlich eine In-Memory-Datenbank definieren.
Die Auto-Konfiguration wird sich immer zurückziehen, sobald der Benutzer beginnt, seine eigenen Beans zu definieren.

=== spring-boot-starters

Starter sind eine Reihe praktischer Abhängigkeitsdeskriptoren, die Sie in Ihre Anwendung einbinden können.
Sie erhalten einen One-Stop-Shop für alle Spring- und verwandten Technologien, die Sie benötigen, ohne durch Beispielcode suchen und massenhaft Abhängigkeitsdeskriptoren kopieren und einfügen zu müssen.
Wenn Sie zum Beispiel mit Spring und JPA für den Datenbankzugriff beginnen möchten, fügen Sie die `spring-boot-starter-data-jpa` Abhängigkeit in Ihr Projekt ein, und Sie können loslegen.

=== spring-boot-actuator

Actuator-Endpunkte ermöglichen es Ihnen, Ihre Anwendung zu überwachen und mit ihr zu interagieren.
Spring Boot Actuator stellt die für Actuator-Endpunkte erforderliche Infrastruktur bereit.
Es enthält Annotations-Unterstützung für Actuator-Endpunkte.
Dieses Modul bietet viele Endpunkte, einschließlich des `HealthEndpoint`, `EnvironmentEndpoint`, `BeansEndpoint` und viele mehr.

=== spring-boot-actuator-autoconfigure

Dies bietet Auto-Konfiguration für Actuator-Endpunkte basierend auf dem Inhalt des Classpaths und einer Reihe von Eigenschaften.
Wenn zum Beispiel Micrometer im Classpath ist, wird es den `MetricsEndpoint` automatisch konfigurieren.
Es enthält Konfigurationen, um Endpunkte über HTTP oder JMX zugänglich zu machen.
Genau wie Spring Boot AutoConfigure wird sich dies zurückziehen, sobald der Benutzer beginnt, seine eigenen Beans zu definieren.

=== spring-boot-test

Dieses Modul enthält Kernelemente und Annotationen, die beim Testen Ihrer Anwendung hilfreich sein können.

=== spring-boot-test-autoconfigure

Wie andere Spring Boot Auto-Konfigurationsmodule bietet spring-boot-test-autoconfigure Auto-Konfiguration für Tests basierend auf dem Classpath.
Es enthält viele Annotationen, die automatisch einen Teil Ihrer Anwendung konfigurieren können, der getestet werden muss.

=== spring-boot-loader

Spring Boot Loader bietet die geheime Zutat, die es Ihnen ermöglicht, eine einzelne JAR-Datei zu erstellen, die mit `java -jar` gestartet werden kann.
Normalerweise müssen Sie `spring-boot-loader` nicht direkt verwenden, sondern stattdessen mit dem link:spring-boot-project/spring-boot-tools/spring-boot-gradle-plugin[Gradle] oder link:spring-boot-project/spring-boot-tools/spring-boot-maven-plugin[Maven] Plugin arbeiten.

=== spring-boot-devtools

Das spring-boot-devtools Modul bietet zusätzliche Entwicklungszeit-Features, wie automatische Neustarts, für eine reibungslosere Anwendungsentwicklung.
Entwickler-Tools werden automatisch deaktiviert, wenn eine vollständig gepackte Anwendung ausgeführt wird.

== Leitfäden

Die https://spring.io/[spring.io] Website enthält mehrere Leitfäden, die Schritt für Schritt zeigen, wie man Spring Boot verwendet:

* https://spring.io/guides/gs/spring-boot/[Eine Anwendung mit Spring Boot erstellen] ist ein einführender Leitfaden, der zeigt, wie Sie eine Anwendung erstellen, ausführen und einige Management-Services hinzufügen.
* https://spring.io/guides/gs/actuator-service/[Einen RESTful Web Service mit Spring Boot Actuator erstellen] ist ein Leitfaden zum Erstellen eines REST-Web-Services und zeigt auch, wie der Server konfiguriert werden kann.

== Lizenz

Spring Boot ist Open Source Software, die unter der https://www.apache.org/licenses/LICENSE-2.0.html[Apache 2.0 Lizenz] veröffentlicht wurde.