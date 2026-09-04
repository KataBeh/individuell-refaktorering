from dataclasses import dataclass               # denna hjälper mig att skapa en enkel klass som ska hålla data
from pathlib import Path                        # och denna använder jag för sökvägar


@dataclass(frozen=True)
class ReportConfig:
    input_path: Path = Path("data/orders.csv")
    output_dir: Path = Path("output")