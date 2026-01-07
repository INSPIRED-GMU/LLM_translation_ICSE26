# Eine Sammlung von `.gitignore`-Vorlagen

Dies ist GitHubs Sammlung von [`.gitignore`][man]-Dateivorlagen.
Wir verwenden diese Liste, um die `.gitignore`-Vorlagen-Auswahl zu füllen, die in der GitHub.com-Oberfläche beim Erstellen neuer Repositories und Dateien verfügbar ist.

Weitere Informationen darüber, wie `.gitignore`-Dateien funktionieren und wie sie verwendet werden, finden Sie in den folgenden Ressourcen:

- Das Kapitel [Dateien ignorieren][chapter] im Buch [Pro Git][progit].
- Der Artikel [Dateien ignorieren][help] auf der GitHub-Hilfeseite.
- Die Handbuchseite [gitignore(5)][man].

[man]: http://git-scm.com/docs/gitignore
[help]: https://help.github.com/articles/ignoring-files
[chapter]: https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring
[progit]: http://git-scm.com/book

## Ordnerstruktur

Wir unterstützen eine Sammlung von Vorlagen, die folgendermaßen organisiert ist:

- Der Hauptordner enthält Vorlagen, die häufig verwendet werden, um den Einstieg mit beliebten Programmiersprachen und Technologien zu erleichtern. Diese definieren eine sinnvolle Menge an Regeln, um sicherzustellen, dass unwichtige Dateien nicht in Ihr Repository übernommen werden.
- [`Global`](./Global) enthält Vorlagen für verschiedene Editoren, Tools und Betriebssysteme, die in unterschiedlichen Situationen verwendet werden können. Es wird empfohlen, diese entweder zu Ihrer [globalen Vorlage hinzuzufügen](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files#configuring-ignored-files-for-all-repositories-on-your-computer) oder diese Regeln in Ihre projektspezifischen Vorlagen zu übernehmen, wenn Sie sie dauerhaft verwenden möchten.
- [`community`](./community) enthält spezialisierte Vorlagen für andere beliebte Sprachen, Tools und Projekte, die derzeit nicht zu den Standardvorlagen gehören. Diese sollten zu Ihren projektspezifischen Vorlagen hinzugefügt werden, wenn Sie sich entscheiden, das Framework oder Tool zu verwenden.

## Was macht eine gute Vorlage aus?

Eine Vorlage sollte eine Reihe von Regeln enthalten, um Git-Repositories mit einer bestimmten Programmiersprache, einem Framework, einem Tool oder einer Umgebung kompatibel zu machen.

Wenn es nicht möglich ist, eine kleine Menge nützlicher Regeln für diese Situation zusammenzustellen, ist die Vorlage nicht geeignet für diese Sammlung.

Wenn eine Vorlage hauptsächlich aus einer Liste von Dateien besteht, die von einer bestimmten Version einer Software (z. B. einem PHP-Framework) installiert werden, könnte sie unter dem Verzeichnis `community` leben. Siehe [Versionierte Vorlagen](#versionierte-vorlagen) für weitere Details.

Wenn Sie eine kleine Menge von Regeln haben oder eine Technologie unterstützen möchten, die nicht weit verbreitet ist, und dennoch glauben, dass dies anderen helfen wird, lesen Sie bitte den Abschnitt über [spezialisierte Vorlagen](#spezialisierte-vorlagen) für weitere Details.

Fügen Sie Details hinzu, wenn Sie eine Pull-Request öffnen, falls die Vorlage wichtig und sichtbar ist. Wir akzeptieren sie möglicherweise nicht sofort, aber wir können sie basierend auf dem Interesse später in das Hauptverzeichnis verschieben.

Bitte verstehen Sie auch, dass wir nicht jedes existierende Tool auflisten können. Unser Ziel ist es, eine Sammlung der _häufigsten und hilfreichsten_ Vorlagen zu kuratieren und nicht sicherzustellen, dass wir jedes mögliche Projekt abdecken. Wenn wir uns entscheiden, Ihre Sprache, Ihr Tool oder Ihr Projekt nicht einzuschließen, liegt das nicht daran, dass es nicht großartig ist.

## Richtlinien für Beiträge

Wir würden uns freuen, wenn Sie uns helfen, dieses Projekt zu verbessern. Um die Qualität dieser Sammlung hoch zu halten, bitten wir darum, dass Beiträge den folgenden Richtlinien entsprechen:

- **Bereitstellen eines Links zur Homepage der Anwendung oder des Projekts**. Es besteht die Möglichkeit, dass die Maintainer die Sprache, das Framework, den Editor, die App oder das Projekt, auf das sich Ihre Änderung bezieht, nicht kennen oder verwenden, es sei denn, es ist extrem populär.

- **Bereitstellen von Links zur Dokumentation**, die die von Ihnen vorgenommenen Änderungen unterstützen. Aktuelle, offizielle Dokumentationen, die die zu ignorierenden Dateien erwähnen, sind ideal. Wenn keine Dokumentation verfügbar ist, tun Sie Ihr Bestes, um zu erklären, wofür die zu ignorierenden Dateien verwendet werden.

- **Erklären Sie, warum Sie eine Änderung vornehmen**. Selbst wenn es offensichtlich erscheint, nehmen Sie sich bitte einen Moment Zeit, um zu erklären, warum Ihre Änderung oder Ergänzung vorgenommen werden sollte. Es ist besonders hilfreich zu artikulieren, warum diese Änderung für _alle_ gilt, die mit der entsprechenden Technologie arbeiten, und nicht nur für Sie oder Ihr Team.

- **Berücksichtigen Sie den Umfang Ihrer Änderung**. Wenn Ihre Änderung spezifisch für eine bestimmte Sprache oder ein bestimmtes Framework ist, stellen Sie sicher, dass die Änderung an der Vorlage für diese Sprache oder dieses Framework vorgenommen wird und nicht an der Vorlage für einen Editor, ein Tool oder ein Betriebssystem.

- **Bitte ändern Sie _nur eine Vorlage_ pro Pull-Request**. Dies hilft, Pull-Requests und Feedback auf ein bestimmtes Projekt oder eine bestimmte Technologie zu fokussieren.

Im Allgemeinen: Je mehr Sie uns helfen können, Ihre Änderung zu verstehen, desto wahrscheinlicher ist es, dass wir Ihren Beitrag schnell akzeptieren.

## Versionierte Vorlagen

Einige Vorlagen können sich zwischen Versionen stark ändern, und wenn Sie zu diesem Repository beitragen möchten, müssen wir diesem spezifischen Ablauf folgen:

- Die Vorlage im Hauptverzeichnis sollte die aktuell unterstützte Version sein.
- Die Vorlage im Hauptverzeichnis sollte keine Version im Dateinamen haben (z. B. "evergreen").
- Frühere Versionen von Vorlagen sollten unter `community/` gespeichert werden.
- Frühere Versionen der Vorlage sollten die Version im Dateinamen enthalten, um die Lesbarkeit zu gewährleisten.

Dies hilft sicherzustellen, dass Benutzer die neueste Version erhalten (weil sie die Vorlage im Hauptverzeichnis verwenden), aber auch älteren Versionen, die noch im Einsatz sind, Unterstützung bieten.

## Spezialisierte Vorlagen

Wenn Sie eine Vorlage haben, die Sie beitragen möchten, die aber nicht ganz Mainstream ist, ziehen Sie bitte in Betracht, sie im Verzeichnis `community` unter einem Ordner hinzuzufügen, der am besten dazu passt.

Die Regeln in Ihrer spezialisierten Vorlage sollten spezifisch für das Framework oder Tool sein, und alle zusätzlichen Vorlagen sollten in einem Kommentar im Header der Vorlage erwähnt werden.

Zum Beispiel könnte diese Vorlage unter `community/DotNet/InforCRM.gitignore` gespeichert sein:

```
# gitignore-Vorlage für InforCRM (ehemals SalesLogix)
# Website: https://www.infor.com/product-summary/cx/infor-crm/
#
# Empfohlen: VisualStudio.gitignore

# Ignoriere Modell-Dateien, die automatisch generiert werden
ModelIndex.xml
ExportedFiles.xml

# Ignoriere Bereitstellungsdateien
[Mm]odel/[Dd]eployment

# Erzwinge die Einbeziehung von Portal-SupportFiles
!Model/Portal/*/SupportFiles/[Bb]in/
!Model/Portal/PortalTemplates/*/SupportFiles/[Bb]in
```

## Arbeitsablauf für Beiträge

So schlagen wir vor, dass Sie vorgehen, um eine Änderung an diesem Projekt vorzuschlagen:

1. [Forken Sie dieses Projekt][fork] zu Ihrem Konto.
2. [Erstellen Sie einen Branch][branch] für die Änderung, die Sie vornehmen möchten.
3. Nehmen Sie Ihre Änderungen an Ihrem Fork vor.
4. [Senden Sie eine Pull-Request][pr] von Ihrem Branch im Fork zu unserem `main`-Branch.

Die Verwendung der webbasierten Oberfläche, um Änderungen vorzunehmen, ist ebenfalls in Ordnung und wird Ihnen helfen, das Projekt automatisch zu forken und eine Pull-Request vorzuschlagen.

[fork]: https://help.github.com/articles/fork-a-repo/
[branch]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[pr]: https://help.github.com/articles/using-pull-requests/

## Lizenz

[CC0-1.0](./LICENSE).
