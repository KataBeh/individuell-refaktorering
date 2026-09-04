# Kodgranskning av order_report.py

## Utgångsläge
Scriptet går att köra och skapar en orderrapporter med sammanställningar över försäljning och returer.

## Granskningsfynd

### Fynd 1 - Hela programmet körs vid import

**Observation:** Hela arbetsflödet körs direkt på modulnivå. Filen börjar läsa data och skapa rapporter så fort modulen körs eller importeras.

**Konsekvens:** Import läser och skriver filer på direkten. Koden får oväntade sidoeffekter och blir svår att återanvända och testa.

**Förslag:** Lägg programstarten/flödet i en `main()`-funktion och skydda anropet med en main-guard.

### Fynd 2 - Flera ansvar är sammanblandade

**Observation:** Samma script blandar/hanterar filhantering, validering, datastädning, transformationslogik, rapportering, filsparning, beräkningar och felhantering.

**Konsekvens:** Delarna blir svåra att testa eller återanvända oberoende av varandra. Om programmet växer blir det också svårare att hitta var olika typer av ändringar ska göras.

**Förslag:** Separera ren transformationslogik från filhantering och orkestrering. Dela upp ansvaret i tydliga moduler, till exempel inläsning, validering, bearbetning och rapportering.


### Fynd 3 - Valideringen ger ett generellt fel

**Observation:** Valideringen kastar `Exception` med meddelandet `Något gick fel` och Om någon obligatorisk kolumn saknas kastas `Exception` med `Fel data`. 

**Konsekvens:** Felet är svårt att felsöka och svårt att kontrollera specifikt i ett automatiskt test. Det framgår inte vilka kolumner som saknas.

**Förslag:** Använd exempelvis `ValueError` och inkludera namnen på de saknade kolumnerna i felmeddelandet.


### Fynd 4 - Sökvägar och förutsättningar är hårdkodade

**Observation:** Sökvägarna till inputen och outputen ligger direkt i programflödet och scriptet som fasta strängar.

**Konsekvens:** Programmet blir svårare att köra med andra filer och svårare att testa med tillfälliga sökvägar. Koden förutsätter också att outputmappen redan finns innan resultatet sparas.

**Förslag:** Samla sökvägarna i en liten konfiguration, tex `dataclass` och låt sparfunktioner skapa målmappen (tex.outputmappen) vid behov.


### Fynd 5 - Statusmeddelanden använder print

**Observation:** `print()` används för att beskriva att programmet startar, hur många rader som lästs och vilka rapporter som sparats.

**Konsekvens:** Det går inte att styra loggnivå, format, destination på ett tydligt sätt. Det framgår inte vilken modul som skapade meddelandet.

**Förslag:** Använd modulloggers för körinformation (tex. `logging.getLogger(__name__)`) och konfigurera loggning centralt vid programmets startpunkt.


### Fynd 6 - Centrala regler saknar tydliga testgränser

**Observation:** Beräkningar för `order_value`, `discounted_value`, försäljning, returer och sammanställningar ligger direkt i det stora programflödet.

**Konsekvens:** För att testa en enskild regel behöver man i praktiken köra stora delar av scriptet. Det gör testerna mer beroende av filsystemet och svårare att felsöka.

**Förslag:** Extrahera rena funktioner som tar emot en DataFrame och returnerar en ny DataFrame eller ett tydligt resultat helt enkelt. Testa den dessutom med små DataFrames i minnet.


### Fynd 7 - Det finns duplicerad rapportlogik

**Observation:** Rapporten per produktkategori och rapporten per region gör nästan samma typ av groupby, summering, avrundning, beräkning av returgrad, sortering och återställning av index.

**Konsekvens:** Liknande kod behöver ändras på flera ställen om rapportlogiken förändras. Det ökar risken för att rapporterna börjar bete sig olika av misstag.

**Förslag:** Flytta den gemensamma logiken till en återanvändbar funktion där grupperingskolumnen skickas in som argument.


### Fynd 8 - Namnen beskriver dataflödet dåligt

**Observation:** Namn som `data`, `required`, `result1` och `result2` är ganska allmänna och beskriver inte tydligt vad objekten innehåller.

**Konsekvens:** Det blir svårare att följa dataflödet, särskilt om programmet senare får fler mellanresultat och rapporter.

**Förslag:** Använd mer beskrivande namn, till exempel orders, required_columns, sales_by_category och sales_by_region.


### Fynd 9 - Felhanteringen är för bred

**Observation:** Nästan hela programmet ligger inuti ett `try` och alla fel fångas med `except Exception`.

**Konsekvens:** Olika typer av fel behandlas på samma sätt och felet skrivs bara ut. Det kan göra det svårare att förstå om problemet exempelvis är en saknad fil, felaktig data eller ett programmeringsfel.

**Förslag:** Hantera endast fel som programmet rimligen kan hantera och låt andra fel vara tydliga. Använd specifika undantag där det är lämpligt.


## Sammanfattning
Scriptet skapar de rapporter som efterfrågas, men stora delar av programmet ligger i samma fil och flera olika ansvar är sammanblandade. Programmet har dessutom sidoeffekter vid import, begränsad validering, bred felhantering och duplicerad rapportlogik.

De centrala beräkningarna är därför svåra att testa isolerat och projektet blir svårare att vidareutveckla.

## Prioritering

### Hög prioritet
1. Fynd 1 - Hela programmet körs vid import
2. Fynd 2 - Flera ansvar är sammanblandade
3. Fynd 6 - Centrala regler saknar tydliga testgränser
4. Fynd 7 - Det finns duplicerad rapportlogik

### Medelprioritet
5. Fynd 3 - Valideringen ger ett generellt fel
6. Fynd 4 - Sökvägar och förutsättningar är hårdkodade
7. Fynd 5 - Statusmeddelanden använder print
8. Fynd 9 - Felhanteringen är för bred

### Låg prioritet
9. Fynd 8 - Namnen beskriver dataflödet dåligt