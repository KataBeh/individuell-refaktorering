import logging
from pathlib import Path
import pandas as pd


logger = logging.getLogger(__name__)


def load_orders(file_path: Path) -> pd.DataFrame:                # gör som läraren: en tydlig funktion med ett enda ansvar
    logger.info("Läser in orderdata från %s", file_path)
    if not file_path.exists():
        raise FileNotFoundError(
            f"Orderfilen kan ej hittas: {file_path}"
        )
    
    orders = pd.read_csv(file_path)

    logger.info("Läste in %s rader", len(orders))               # jag byter print() mot logging

    return orders