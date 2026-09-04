import pandas as pd


REQUIRED_COLUMNS = {
    "order_id",
    "order_date",
    "customer_id",
    "region",
    "product_category",
    "quantity",
    "unit_price",
    "discount",
    "returned",
}


def validate_columns(orders: pd.DataFrame) -> None:
    missing_columns = REQUIRED_COLUMNS - set(orders.columns)

    if missing_columns:
        raise ValueError(
            f"Saknade obligatoriska kolumner: {sorted(missing_columns)}"
        )

def validate_not_empty(orders: pd.DataFrame) -> None:
    if orders.empty:
        raise ValueError("Orderdata är tom")