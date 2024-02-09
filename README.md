# Green program starter

```python
for i in range(39):
    print(i)
```

What is the goal of my project and what do I simply want to do with it?

First of all I have to start with describing
the problem that I want to fix with my program.
There a programs in the world, that don´t have 
to run 24/7 all the time, because they just 
calculate something one time a month.
The goal of my program now is to boot the program, 
if it really is in use.
Additionally my program will check, if the electricity 
that feeds the program is completely from green resources.

## Technologien, Bibliotheken und Sprachen, die ich benutzen möchte:

Ich möchte mein Programm gerne in Python schreiben.
Um die Daten der APIs auszulesen, brauche ich wahrscheinlich HTTP Befehle.

## APIs und was für Daten sie mir geben:

Ich werde wahrscheinlich eine API von dieser Webseite für
die Auslese meiner Daten verwenden: https://smard.api.bund.dev
Diese Webseite liefert mir Daten über die Stromzufuhr der verschiedenen
Bereiche, ihrer Kosten und auch prognostizierte Daten darüber, wie die
Stromverteilung sein wird.

Die Daten, die als zweites angegeben werden, sind die Stromerzeugung in Mega-
wattstunden.

Die Zahl davor gibt dem Timestamp an.

Wenn man den Link zur Erstellung der Timestamps mithilfe der ersten API so verändert: https://smard.de/app/chart_data/1223/DE/1223_DE_hour_1702854000000.json
dann kriegt man die aktuelleren Timestamps raus. Diese stehen dann auf einer gesonderten Webseite.

Den letzten Timestamp muss man dann nur noch hinten einfügen und man kriegt gute, aktuelle Werte raus.

Heute habe die Daten in eine Json Datei gespeichert, damit
ich sie dann später weiterverarbeiten kann.

Ich habe alle wichtigen Kommentare, die mein Vorgehen erklären, in die Python Datei direkt geschrieben.

Ich habe es jetzt geschafft, die wichtigen Werte aus Series in der Kommandozeile übersichtlich anzuzeigen. Diese Werte liegen ja in der Zukunft, also muss ich sie in Variablen speichere, die dann in einer Schleife
nach der korrekten Zeit abgerufen und benutzt/überprüft werden.

Und ich muss noch die nicht grünen Quellen abrufen, um zu überprüfen, wie hoch der Anteil an grünem Strom ist.

Ich muss jetzt den Fehler beheben, dass bei der zweiten Auslese für den MWh Wert nur ein Timestamp rauskommt. 
Aber das ist eigentlich sowieso unwichtig, denn wir haben herausgefunden, dass bei der Gesamt prognostizierten Erzeugung
noch alles andere wie Kohle und so dazukommt. Wir müssen also den Gesamtwert abrufen und dann mit dem Wind etc.
subtrahieren. Bis zum nächsten Mal, tschau.

Heute habe ich das Herausfiltern der Gesamt Werte in Module geballert. Um auch Werte herauszubekommen, die tagsüber liegen, muss man einfach weiter zurück
in den Listen gehen, um ältere Werte zu bekommen und nicht immer nur den letzten. Jetzt muss ich nur noch herausfinden, wie ich den richtigen Timestamp für den richtigen Wert herausbekomme. Ich weiß halt nicht, ob beide Listen bei jeder Anfrage gleich lang sind. Ich schätze mal, dass dem nicht so ist, also muss ich wohl einen Algorithmus programmieren, der das gut schafft. Mir fällt gerade auf, dass ich einfach nur in beiden Listen im Verhältnis gleich lang zurück gehen muss, um die passenden Werte zu finden. Ok, nice und tschau :)
Auf jeden Fall muss ich jetzt am Tag für jede Viertelstunde überprüfen, wie hoch die Erzeugung des grünem Strom
ist. Dann überprüfe ich, welcher Wert am höchsten ist und schalte die anderen Programme genau zu dieser Uhrzeit an. Irgendwann kann es dann sogar so weit
kommen, dass ich gucke, wann es sich langfristig am Besten lohnt, also wo der Verbrauch für mehrere Stunden am niedrigsten 
ist, falls Programme länger als 15 Minuten dauert. 

Wie ich es mir gerade denke: Ich überprüfe um ein Uhr morgens, wann der Anteil an grünem Strom am höchsten ist. Dazu errechne ich den Anteil an grünem Strom an der
Gesamterzeugung. Diese Uhrzeit speichere ich dann in eine Variable, die an ein zeitgesteuertes Modul übergeben wird und dieses Modul
führt die anderen Programme dann zu dieser bestimmten Uhrzeit aus.