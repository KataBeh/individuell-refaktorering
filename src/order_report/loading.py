import logging

import pandas as pd


logger = logging.getLogger(__name__)


def load_orders(file_path: str) -> pd.DataFrame:
    logger.info("Läser in orderdata från %s", file_path)

    orders = pd.read_csv(file_path)

    logger.info("Läste in %s rader", len(orders))

    return orders