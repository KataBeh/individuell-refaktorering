from pathlib import Path

import pytest

from order_report.loading import load_orders


def test_load_orders_missing_file():
    missing_file = Path("data/does_not_exist.csv")

    with pytest.raises(FileNotFoundError):
        load_orders(missing_file)