# Eine Sammlung von `.gitignore`-Vorlagen

Dies ist GitHubs Sammlung von [`.gitignore`][man]-Dateivorlagen.
Wir verwenden diese Liste, um die `.gitignore`-Vorlagenauswahl zu füllen, die
in der GitHub.com-Oberfläche beim Erstellen neuer Repositories und Dateien verfügbar ist.

Für weitere Informationen darüber, wie `.gitignore`-Dateien funktionieren und wie sie verwendet werden,
sind die folgenden Ressourcen ein guter Ausgangspunkt:

- Das [Kapitel "Dateien ignorieren"][chapter] im [Pro Git][progit] Buch.
- Der [Artikel "Dateien ignorieren"][help] auf der GitHub Help-Seite.
- Die [gitignore(5)][man] Handbuchseite.

[man]: http://git-scm.com/docs/gitignore
[help]: https://help.github.com/articles/ignoring-files
[chapter]: https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring
[progit]: http://git-scm.com/book

## Ordnerstruktur

Wir unterstützen eine Sammlung von Vorlagen, die wie folgt organisiert sind:

- Der Hauptordner enthält häufig verwendete Vorlagen, die Menschen den Einstieg
  in beliebte Programmiersprachen und Technologien erleichtern. Diese definieren
  sinnvolle Regeln für den Einstieg und stellen sicher, dass Sie keine
  unwichtigen Dateien in Ihr Repository übertragen.
- [`Global`](./Global) enthält Vorlagen für verschiedene Editoren, Tools und
  Betriebssysteme, die in unterschiedlichen Situationen verwendet werden können. Es wird empfohlen,
  diese entweder [zu Ihrer globalen Vorlage hinzuzufügen](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files#configuring-ignored-files-for-all-repositories-on-your-computer)
  oder diese Regeln in Ihre projektspezifischen Vorlagen zu integrieren, wenn Sie sie dauerhaft nutzen möchten.
- [`community`](./community) enthält spezialisierte Vorlagen für andere beliebte
  Sprachen, Tools und Projekte, die derzeit nicht zu den Hauptvorlagen gehören.
  Diese sollten zu Ihren projektspezifischen Vorlagen hinzugefügt werden, wenn Sie
  sich entscheiden, das Framework oder Tool zu verwenden.

## Was macht eine gute Vorlage aus?

Eine Vorlage sollte eine Reihe von Regeln enthalten, die Git-Repositories bei der Arbeit mit einer
bestimmten Programmiersprache, einem Framework, Tool oder einer Umgebung unterstützen.

Wenn es nicht möglich ist, eine kleine Anzahl nützlicher Regeln für diese Situation zusammenzustellen,
dann ist die Vorlage keine gute Wahl für diese Sammlung.

Wenn eine Vorlage hauptsächlich eine Liste von Dateien ist, die von einer bestimmten Version
einer Software installiert wurden (z.B. ein PHP-Framework), kann sie im `community`-Verzeichnis
untergebracht werden. Siehe [Versionierte Vorlagen](#versionierte-vorlagen) für weitere Details.

Wenn Sie einen kleinen Regelsatz haben oder eine Technologie unterstützen möchten, die nicht
weit verbreitet ist, und dennoch glauben, dass dies für andere hilfreich sein wird, lesen Sie bitte den
Abschnitt über [Spezialisierte Vorlagen](#spezialisierte-vorlagen) für weitere Details.

Fügen Sie Details hinzu, wenn Sie einen Pull Request für eine wichtige und sichtbare Vorlage öffnen. Wir
akzeptieren sie möglicherweise nicht sofort, können sie aber zu einem späteren Zeitpunkt
basierend auf dem Interesse in den Hauptordner verschieben.

Bitte haben Sie auch Verständnis dafür, dass wir nicht jedes jemals existierende Tool auflisten können.
Unser Ziel ist es, eine Sammlung der _häufigsten und hilfreichsten_ Vorlagen zu pflegen,
nicht sicherzustellen, dass wir jedes mögliche Projekt abdecken. Wenn wir uns entscheiden,
Ihre Sprache, Ihr Tool oder Ihr Projekt nicht aufzunehmen, liegt das nicht daran, dass es nicht großartig ist.

## Beitragsrichtlinien

Wir würden uns freuen, wenn Sie uns helfen, dieses Projekt zu verbessern. Um die hohe
Qualität dieser Sammlung zu gewährleisten, bitten wir darum, dass Beiträge die folgenden Richtlinien einhalten.

- **Stellen Sie einen Link zur Homepage der Anwendung oder des Projekts bereit**. Wenn es nicht
  extrem populär ist, besteht die Möglichkeit, dass die Maintainer die Sprache, das Framework,
  den Editor, die App oder das Projekt, auf das sich Ihre Änderung bezieht, nicht kennen oder verwenden.

- **Stellen Sie Links zur Dokumentation** bereit, die Ihre Änderung unterstützen.
  Aktuelle, maßgebliche Dokumentation, die die zu ignorierenden Dateien erwähnt, ist am besten.
  Wenn keine Dokumentation zur Unterstützung Ihrer Änderung verfügbar ist, erklären Sie so gut wie möglich,
  wofür die zu ignorierenden Dateien gedacht sind.

- **Erklären Sie, warum Sie eine Änderung vornehmen**. Auch wenn es selbsterklärend erscheint,
  nehmen Sie sich ein oder zwei Sätze Zeit, um uns zu erklären, warum Ihre Änderung oder Ergänzung erfolgen sollte.
  Besonders hilfreich ist es zu erläutern, warum diese Änderung für _alle_ gilt,
  die mit der betreffenden Technologie arbeiten, und nicht nur für Sie oder Ihr Team.

- **Bitte beachten Sie den Umfang Ihrer Änderung**. Wenn Ihre Änderung spezifisch für eine
  bestimmte Sprache oder ein Framework ist, stellen Sie sicher, dass die Änderung in der
  Vorlage für diese Sprache oder dieses Framework vorgenommen wird und nicht in der Vorlage für einen
  Editor, ein Tool oder ein Betriebssystem.

- **Bitte modifizieren Sie _nur eine Vorlage_ pro Pull Request**. Dies hilft, Pull
  Requests und Feedback auf ein bestimmtes Projekt oder eine bestimmte Technologie zu fokussieren.

Im Allgemeinen gilt: Je mehr Sie uns helfen können, die Änderung zu verstehen, die Sie vornehmen,
desto wahrscheinlicher ist es, dass wir Ihren Beitrag schnell akzeptieren.

## Versionierte Vorlagen

Einige Vorlagen können sich zwischen Versionen stark ändern, und wenn Sie zu diesem
Repository beitragen möchten, müssen wir diesem spezifischen Ablauf folgen:

- die Vorlage im Hauptverzeichnis sollte die aktuell unterstützte Version sein
- die Vorlage im Hauptverzeichnis sollte keine Version im Dateinamen haben
  ("evergreen")
- frühere Versionen von Vorlagen sollten unter `community/` liegen
- frühere Versionen der Vorlage sollten die Version im Dateinamen einbetten,
  der Lesbarkeit halber

Dies hilft sicherzustellen, dass Benutzer die neueste Version erhalten (da sie das verwenden, was
im Hauptverzeichnis liegt), aber hilft Maintainern auch, ältere Versionen zu unterstützen, die noch in Verwendung sind.

## Spezialisierte Vorlagen

Wenn Sie eine Vorlage haben, die Sie beitragen möchten, die aber nicht ganz
zum Mainstream gehört, erwägen Sie bitte, diese zum `community`-Verzeichnis in einem
Ordner hinzuzufügen, der am besten dazu passt.

Die Regeln in Ihrer spezialisierten Vorlage sollten spezifisch für das Framework oder
Tool sein, und alle zusätzlichen Vorlagen sollten in einem Kommentar im
Header der Vorlage erwähnt werden.

Zum Beispiel könnte diese Vorlage unter `community/DotNet/InforCRM.gitignore` liegen:

```
# gitignore template for InforCRM (formerly SalesLogix)
# website: https://www.infor.com/product-summary/cx/infor-crm/
#
# Recommended: VisualStudio.gitignore

# Ignore model files that are auto-generated
ModelIndex.xml
ExportedFiles.xml

# Ignore deployment files
[Mm]odel/[Dd]eployment

# Force include portal SupportFiles
!Model/Portal/*/SupportFiles/[Bb]in/
!Model/Portal/PortalTemplates/*/SupportFiles/[Bb]in
```

## Workflow für Beiträge

So schlagen wir vor, dass Sie bei einer vorgeschlagenen Änderung an diesem Projekt vorgehen:

1. [Forken Sie dieses Projekt][fork] in Ihren Account.
2. [Erstellen Sie einen Branch][branch] für die beabsichtigte Änderung.
3. Nehmen Sie Ihre Änderungen in Ihrem Fork vor.
4. [Senden Sie einen Pull Request][pr] von dem Branch Ihres Forks zu unserem `main` Branch.

Die Verwendung der webbasierten Oberfläche für Änderungen ist auch in Ordnung und wird Ihnen
helfen, indem das Projekt automatisch geforkt wird und Sie aufgefordert werden, einen Pull Request zu senden.

[fork]: https://help.github.com/articles/fork-a-repo/
[branch]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[pr]: https://help.github.com/articles/using-pull-requests/

## Lizenz

[CC0-1.0](./LICENSE).