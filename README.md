# Order Report

Detta projekt är en refaktorerad version av ett Pythonprogram för orderrapportering.

Programmet läser orderdata från en CSV-fil, validerar och bearbetar datan och skapar rapporter över bland annat försäljning och returer.

Syftet med projektet är främst att förbättra kodens struktur, testbarhet, felhantering och återanvändbarhet.

## Funktionalitet

Programmet kan:

- läsa orderdata från CSV
- kontrollera att obligatoriska kolumner finns
- kontrollera att datan inte är tom
- hantera vissa felaktiga eller orimliga värden
- beräkna ordervärde
- beräkna rabatterat ordervärde
- sammanställa försäljning per produktkategori
- sammanställa försäljning per region
- sammanställa returer per produktkategori
- spara rapporterna som CSV-filer

## Installation

Projektet använder Python och bland annat Pandas, jupyter, numpy och pytest.

Installera projektets beroenden med:

```bash
pip install -r requirements.txt 
```
och/ eller 
```bash
pip install -e .
```

## Kör programmet 

Starta från projektets rotmap 

```bash
python -m order_report 
```

### Orderdatan läses från 
data/orders.csv

### De sparade rapporterna sparas i
output/

där programmet skapar följande filer:
- overview.csv
- sales_by_category.csv
- sales_by_region.csv
- returns_by_category.csv

## Kör tester 
Projektet använder pytest för automatiska tester. Dessa kan köras med `python -m pytest -v`

Testerna kontrollerar bla:
- obligatoriska kolumner
- tom data
- numeriska värden
- beräkning av ordervärde
- rabatterat ordervärde
- bearbetning av returvärden
- sammanställning av försäljning
- sammanställning av returer
- hantering av saknad datafil


## Projektstruktur

individuell-refaktorering/
│
├── data/
│   └── orders.csv
│
├── output/
│
├── src/
│   └── order_report/
│       ├── __init__.py
│       ├── __main__.py
│       ├── config.py
│       ├── loading.py
│       ├── logging_config.py
│       ├── processing.py
│       ├── reporting.py
│       └── validation.py
│
├── tests/
│   ├── test_loading.py
│   ├── test_processing.py
│   ├── test_reporting.py
│   └── test_validation.py
│
├── code_review.md
├── legacy_order_report.py
├── pyproject.toml
├── README.md
└── requirements.txt


## Kort om modulerna

- `__main__.py` styr i vilken ordning programmet körs.
- `config.py` innehåller programmets konfiguration och sökvägar.
- `loading.py` läser in orderdata.
- `validation.py` kontrollerar datan och fångar rimliga fel.
- `processing.py` städar och bearbetar orderdatan.
- `reporting.py` skapar och sparar rapporterna.
- `logging_config.py` konfigurerar programmets logging.
- `tests/` innehåller automatiska tester med pytest.
- `legacy_order_report.py` innehåller den ursprungliga versionen av programmet.


---------------------------------------------------------------------------------------


**Vilka var de viktigaste problemen i originalkoden?**

De största problemen var att nästan all kod låg i samma fil och att flera olika saker blandades ihop, till exempel filinläsning, validering, bearbetning och rapportering. Det användes också **print()** istället för **logging** och felhanteringen var ganska basic och generell. Det gjorde koden svårare att förstå, testa och bygga vidare på.

**Vilka förändringar tycker du förbättrade programmet mest?**

Jag tycker att det blev störst förbättring när jag delade upp koden i flera moduler med tydliga ansvar. Då blev det lättare att se var varje del hör hemma. Jag tycker också att testerna och logging gjorde stor skillnad eftersom programmet blev lättare att kontrollera och felsöka.

**Varför valde du den projektstruktur du använde?**

Jag valde strukturen för att separera olika delar av programmet. Till exempel ligger inläsning i loading.py, validering i validation.py, bearbetning i processing.py och rapporterna i reporting.py. Då blir det lättare att förstå projektet och man behöver inte leta i en jättestor fil, samtidigt som jag försökte följa och inspireras av lärarens arbetstråd i VS COD så mycket det gick.

**Var använde du OOP/dataclass och varför passade det där?**

Jag använde en dataclass i config.py för programmets sökvägar. Där passade det bra eftersom inputfil och outputmapp hör ihop som konfiguration. Det gjorde också att jag slapp ha sökvägar hårdkodade direkt i huvudprogrammet.

**Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?**

Testerna kontrollerar bland annat att obligatoriska kolumner finns, att datan inte är tom, att ordervärden och rabatter räknas rätt och att rapporterna sammanställs korrekt. De testar också fel som saknad fil och negativa värden. Om programmet ändras i framtiden kan testerna hjälpa till att upptäcka om något som fungerade innan plötsligt har gått sönder.

**Vad var svårast?**

Det är rätt så mycket som kändes svår. I början var det svårt att förstå vad som skulle ligga i main och i de andra modulerna. Hur ska koden ändras exakt utan att "råka" ändra slutresultaten. I vilken ordning ska modulerna byggas och hur ska orginalkoden delas upp på bästa sätt. 

**Vad hade du velat förbättra ytterligare om du haft mer tid?**

Lite svårt att säga, men kanske gjort några fler tester? Kanske förbättra felmeddelanden lite och man kan alltid försöka göra koder lite mer detaljerade in i sista fingerspetsen. 