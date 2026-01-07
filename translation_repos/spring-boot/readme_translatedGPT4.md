= Spring Boot 
image:https://github.com/spring-projects/spring-boot/actions/workflows/build-and-deploy-snapshot.yml/badge.svg?branch=main["Build Status", link="https://github.com/spring-projects/spring-boot/actions/workflows/build-and-deploy-snapshot.yml?query=branch%3Amain"] image:https://img.shields.io/badge/Revved%20up%20by-Develocity-06A0CE?logo=Gradle&labelColor=02303A["Revved up by Develocity", link="https://ge.spring.io/scans?&search.rootProjectNames=Spring%20Boot%20Build&search.rootProjectNames=spring-boot-build"]

:docs: https://docs.spring.io/spring-boot
:github: https://github.com/spring-projects/spring-boot

Spring Boot hilft Ihnen, Spring-basierte, produktionsreife Anwendungen und Services mit minimalem Aufwand zu erstellen. Es bietet eine meinungsstarke Sicht auf die Spring-Plattform, damit neue und bestehende Benutzer schnell zu den benötigten Teilen gelangen.

Sie können Spring Boot verwenden, um eigenständige Java-Anwendungen zu erstellen, die mit `java -jar` gestartet werden können, oder herkömmlichere WAR-Deployments nutzen. Wir bieten auch ein Befehlszeilentool, das Spring-Skripte ausführt.

Unsere Hauptziele sind:

* Bereitstellung eines radikal schnelleren und breiter zugänglichen Einstiegserlebnisses für die gesamte Spring-Entwicklung.
* Meinungsstark sein, aber schnell zur Seite treten, sobald Anforderungen von den Vorgaben abweichen.
* Bereitstellung einer Reihe von nicht-funktionalen Features, die für große Klassen von Projekten üblich sind (z. B. eingebettete Server, Sicherheit, Metriken, Gesundheitsprüfungen, externalisierte Konfiguration).
* Absolut keine Code-Generierung und keine Anforderungen an XML-Konfiguration.

== Installation und Einstieg

Die {docs}[Referenzdokumentation] enthält detaillierte {docs}/installing.html[Installationsanweisungen] sowie eine umfassende {docs}/tutorial/first-application/index.html["Erste Schritte"]-Anleitung.

Hier ein kurzer Einblick in eine vollständige Spring Boot-Anwendung in Java:

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

== Hilfe bekommen

Haben Sie Probleme mit Spring Boot? Wir möchten Ihnen helfen!

* Überprüfen Sie die {docs}/[Referenzdokumentation], insbesondere die {docs}/how-to/index.html[How-to's], die Lösungen für die häufigsten Fragen bieten.
* Lernen Sie die Grundlagen von Spring kennen – Spring Boot baut auf vielen anderen Spring-Projekten auf; besuchen Sie die https://spring.io[spring.io]-Website für eine Fülle von Referenzdokumentationen. Wenn Sie neu bei Spring sind, probieren Sie einen der https://spring.io/guides[Guides].
* Wenn Sie ein Upgrade durchführen, lesen Sie die {github}/wiki[Release Notes] für Anweisungen zum Upgrade und für "neue und bemerkenswerte" Features.
* Stellen Sie eine Frage – wir überwachen https://stackoverflow.com[stackoverflow.com] für Fragen, die mit https://stackoverflow.com/tags/spring-boot[`spring-boot`] getaggt sind.
* Melden Sie Fehler mit Spring Boot unter {github}/issues[github.com/spring-projects/spring-boot/issues].

== Probleme melden

Spring Boot verwendet das integrierte Issue-Tracking-System von GitHub, um Fehler und Feature-Anfragen zu protokollieren. Wenn Sie ein Problem melden möchten, beachten Sie bitte die folgenden Empfehlungen:

* Bevor Sie einen Fehler melden, durchsuchen Sie den {github}/issues[Issue-Tracker], um zu sehen, ob jemand das Problem bereits gemeldet hat.
* Wenn das Problem noch nicht existiert, {github}/issues/new[erstellen Sie ein neues Issue].
* Bitte geben Sie so viele Informationen wie möglich mit der Problemmeldung an. Wir möchten die verwendete Spring Boot-Version, das Betriebssystem und die JVM-Version wissen.
* Wenn Sie Code oder einen Stack-Trace einfügen müssen, verwenden Sie Markdown. +++```+++ vor und nach Ihrem Text.
* Wenn möglich, versuchen Sie, einen Testfall oder ein Projekt zu erstellen, das das Problem reproduziert, und fügen Sie es dem Issue bei.

== Aus dem Quellcode bauen

Sie müssen nicht aus dem Quellcode bauen, um Spring Boot zu verwenden (Binärdateien finden Sie unter https://repo.spring.io[repo.spring.io]), aber wenn Sie die neuesten und besten Features ausprobieren möchten, können Sie Spring Boot mit dem https://docs.gradle.org/current/userguide/gradle_wrapper.html[Gradle-Wrapper] erstellen und in Ihrem lokalen Maven-Cache veröffentlichen. Sie benötigen auch JDK 17.

[source,shell]
----
$ ./gradlew publishToMavenLocal
----

Dies erstellt alle JARs und die Dokumentation und veröffentlicht sie in Ihrem lokalen Maven-Cache. Es führt keine Tests aus. Wenn Sie alles bauen möchten, verwenden Sie die `build`-Aufgabe:

[source,shell]
----
$ ./gradlew build
----

== Module

Es gibt mehrere Module in Spring Boot. Hier ein kurzer Überblick:

=== spring-boot

Die Hauptbibliothek, die Features bereitstellt, die die anderen Teile von Spring Boot unterstützen. Dazu gehören:

* Die `SpringApplication`-Klasse, die statische Komfortmethoden bereitstellt, um eine eigenständige Spring-Anwendung zu schreiben. Ihre einzige Aufgabe ist es, einen geeigneten Spring-`ApplicationContext` zu erstellen und zu aktualisieren.
* Eingebettete Webanwendungen mit einer Auswahl an Containern (Tomcat, Jetty oder Undertow).
* Erstklassige Unterstützung für externalisierte Konfiguration.
* Komfort-`ApplicationContext`-Initialisierer, einschließlich Unterstützung für sinnvolle Standardwerte für Logging.

=== spring-boot-autoconfigure

Spring Boot kann große Teile typischer Anwendungen basierend auf dem Inhalt ihres Klassenpfads konfigurieren. Eine einzelne `@EnableAutoConfiguration`-Annotation löst die automatische Konfiguration des Spring-Kontexts aus.

=== spring-boot-starters

Starter sind eine Reihe bequemer Abhängigkeitsbeschreibungen, die Sie in Ihre Anwendung aufnehmen können. Sie erhalten alles, was Sie für die Arbeit mit Spring und verwandten Technologien benötigen, ohne durch Beispielcode suchen und zahlreiche Abhängigkeitsbeschreibungen kopieren zu müssen.

=== spring-boot-actuator

Actuator-Endpunkte ermöglichen es Ihnen, Ihre Anwendung zu überwachen und mit ihr zu interagieren. Spring Boot Actuator bietet die Infrastruktur, die für Actuator-Endpunkte erforderlich ist.

=== spring-boot-test

Dieses Modul enthält Kernpunkte und Annotationen, die beim Testen Ihrer Anwendung hilfreich sein können.

== Guides

Die https://spring.io/[spring.io]-Website enthält mehrere Anleitungen, die zeigen, wie Sie Spring Boot Schritt für Schritt verwenden:

* https://spring.io/guides/gs/spring-boot/[Building an Application with Spring Boot] ist eine Einführung, die zeigt, wie Sie eine Anwendung erstellen, ausführen und einige Verwaltungsdienste hinzufügen.
* https://spring.io/guides/gs/actuator-service/[Building a RESTful Web Service with Spring Boot Actuator] ist eine Anleitung zur Erstellung eines REST-Webdienstes und zeigt auch, wie der Server konfiguriert werden kann.

== Lizenz

Spring Boot ist Open-Source-Software, die unter der https://www.apache.org/licenses/LICENSE-2.0.html[Apache 2.0-Lizenz] veröffentlicht wurde.
