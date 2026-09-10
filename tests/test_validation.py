import pandas as pd
import pytest

from order_report.validation import validate_columns, validate_not_empty, validate_numeric_values


def test_validate_columns_with_all_required_columns():
    orders = pd.DataFrame(
        columns=[
            "order_id",
            "order_date",
            "customer_id",
            "region",
            "product_category",
            "quantity",
            "unit_price",
            "discount",
            "returned",
        ]
    )

    validate_columns(orders)


def test_validate_columns_missing_column():
    orders = pd.DataFrame(
        columns=[
            "order_id",
            "order_date",
            "customer_id",
            "region",
            "product_category",
            "quantity",
            "unit_price",
            "returned",
        ]
    )

    with pytest.raises(ValueError, match="discount"):
        validate_columns(orders)                         # här förväntar jag mig att koden ska kasta ett ValueError



# små tester för felhantering:
def test_validate_not_empty_with_data():
    orders = pd.DataFrame(
        {
            "order_id": ["00001"]
        }
    )

    validate_not_empty(orders)


def test_validate_not_empty_with_empty_dataframe():
    orders = pd.DataFrame()

    with pytest.raises(ValueError):
        validate_not_empty(orders)


def test_validate_numeric_values_with_negative_quantity():
    orders = pd.DataFrame(
        {
            "quantity": [-1],
            "unit_price": [100],
        }
    )

    with pytest.raises(ValueError, match="quantity"):
        validate_numeric_values(orders)