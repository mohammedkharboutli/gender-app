# README
## Installation von Python3.13
Um Python unkompliziert zu installieren, kann der `Microsoft Store` verwendet werden. Dort einfach in der Suche nach `Python3.13` suchen, herunterladen und den Installationsprozess bestätigen.

## Installation von UV (Python Paket- und Projektmanager)
Mit dem Tool UV kann sehr unkompliziert ein Python Projekt verwaltet werden. Es nimmt einem die Arbeit des ordnungsgemäßen Dependency Management ab und ist dabei unfassbar schnell.

Zur Installation von UV muss der Installation Guide Schritt für Schritt durchlaufen werden. Diesen kann man [HIER](https://docs.astral.sh/uv/getting-started/installation/) finden.

(Wichtig: UV für das richtige Betriebssystem installieren. Windows unterscheidet sich von MacOS oder Linux!
## Starten der Applikation
Um nun alle erforderlichen Pakete/Dependencies zu installieren, kann einfach über den folgenden Command erledigt werden:
```terminal 
uv sync
```
Um nun die Applikation als Desktop App zu starten, wird folgender Befehl genutzt:
```terminal
uv run flet run -r main.py
```
Für die Ansicht im Web wird dieser Befehl eingesetzt:
```terminal
uv run flet run -r --web --port 8007 main.py
```
Zur Ansicht der WebApp muss nun im Browser die Adresse [http://localhost:8007/](http://localhost:8007/) aufgerufen werden. 

(Über die Flag `-r` wird der automatische Reload sichergestellt, dies ist sehr nützlich, wenn man seine Codeänderung live sehen möchte, ohne jedes Mal die Applikation neu zu starten.)

## Struktur der Applikation
Derzeit sieht die Struktur (View) der Applikation wie folgt aus:
```
+---------------------+---------------------+
|      Eingabe        |       Resultat      |  <-- Titel der beiden Spalten
+---------------------+---------------------+
|  Input TextField    |  Output TextField   |  <-- Selbstexpandierende Textfelder
|                     |                     |
|                     |                     |
|                     |                     |
+---------------------+---------------------+
|                     |                     |  <-- Platzhalter (zusätzlicher Raum)
+---------------------+---------------------+
| [ S ]  [ R ]                        [ D ] |  <-- Buttons und Dropdown
+-------------------------------------------+

```

## Planung
Es ist geplant, dass die App einen InputText (eingegeben vom User) erhält und diesen nach Vorgaben im Kontext von [gegenderte Sprache](https://de.wikipedia.org/wiki/Geschlechtergerechte_Sprache) auswertetet. Hierzu ist die Überlegung diese Vorgaben in Form von softwareseitigen Modulen im Model vorzunehmen und direkt über ein Dropdown zu verarbeiten.

