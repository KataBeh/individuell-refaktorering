from dataclasses import dataclass               # denna hjälper mig att skapa en enkel klass som ska hålla data
from pathlib import Path                        # och denna använder jag för sökvägar


@dataclass(frozen=True)                         # frozen = konfigurationen inte ska ändras efter att objektet skapats
class ReportConfig:
    input_path: Path = Path("data/orders.csv")
    output_dir: Path = Path("output")


# när jag kör config=ReportCofig så kommer jag automatiskt få config.input_path och config.output_dir