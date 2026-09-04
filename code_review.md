# Kodgranskning av order_report.py

## Utgångsläge
Scriptet går att köra och skapar en artistöversikt.

## Granskningsfynd

### Fynd 1 - Hela programmet körs vid import

**Observation:** Hela arbetsflödet körs på modulnivå.

**Konsekvens:** Import läser och skriver filer. Koden får oväntade sidoeffekter och blir svår att återanvända och testa.

**Förslag:** Lägg programstarten i en `main()`-funktion och skydda anropet med en main-guard

### Fynd 2 - Flera ansvar är sammanblandade

**Observation:** Scriptet blandar filhantering, validering, transformationslogik, rapportering och programflöde.

**Konsekvens:** Delarna kan inte testas eller återanvändas oberoende av varandra. Olika typer av förändringar behöver göras på samma plats.

**Förslag:** Separera ren transformationslogik från filhantering och orkestrering.


### Fynd 3 - Valideringen ger ett generellt fel

**Observation:** Valideringen kastar `Exception` med meddelandet `Fel data`.

**Konsekvens:** Felet är svårt att felsöka och svårt att kontrollera specifikt i ett automatiskt test. Det framgår inte vilka kolumner som saknas.

**Förslag:** Kasta `ValueError` och namnen på dom saknade kolumnerna.


### Fynd 4 - Sökvägar och förutsättningar är hårdkodade

**Observation:** Sökvägarna ligger direkt i programflödet och scriptet förutsätter att outputmappen redan finns.

**Konsekvens:** Det blir svårare att köra programmet med andra filer och att testa det med tillfälliga sökvägar. Output mappen är en dold förutsättning

**Förslag:** Samla sökvägarna i en liten konfiguration och låt sparfunktioner skapa målmappen vid behov.


### Fynd 5 - Statusmeddelanden använder print

**Observation:** `print()` används för att beskriva att programmet läser data och att körningen är klar.

**Konsekvens:** Det går inte att styra nivå, format, destination, och det framgår inte vilken modul som skapade meddelandet.

**Förslag:** Använd modulloggers för körinformation och konfigurera loggning centralt vid programmets startpunkt.


### Fynd 6 - Centrala regler saknar tydliga testgränser

**Observation:** Reglerna för fullföljd spelning och sammanfattningen per artist är bundna till hela filflödet.

**Konsekvens:** För att kontrollera reglerna måste vi köra hela scriptet och läsa resultatfilen. Testerna blir långsammare och det blir svårare att se var ett fel uppstår.

**Förslag:** Extrahera rena funktioner som tar emot en DataFrame och returnerar en ny DataFrame. Testa den med små DataFrames i minnet.


### Fynd 7 - Namnen beskriver dataflödet dåligt

**Observation:** Namnen `data` och `result` är allmänna och säger väldigt lite om objektens innehåll eller roll.

**Konsekvens:** Dataflödet blir svårare att följa, särskillt om programmet skulle växa och fler mellanresultat skulle tillkomma.

**Förslag:** Använd mer beskrivande namn, t.ex: `history`, `prepared` och `summary`


## Sammanfattning
Scriptet skapar rätt artistöversikt för exempeldatan, men programflödet har sidoeffekter vid import och blandar filhantering, transformation och sparning. De centrala reglerna är därför svåra att testa isolerat.

## Prioritering

### Hög prioritet
1. Fynd 1 - Hela programmet körs vid import
2. Fynd 2 - Flera ansvar är sammanblandade
3. Fynd 6 - Centrala regler saknar tydliga testgränser

### Medelprioritet
4. Fynd 3 - Valideringen ger ett generellt fel
5. Fynd 4 - Sökvägar och förutsättningar är hårdkodade
6. Fynd 5 - Statusmeddelanden använder print

### Låg prioritet
7. Fynd 7 - Namnen beskriver dataflödet dåligt