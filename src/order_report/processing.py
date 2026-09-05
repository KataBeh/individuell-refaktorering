import pandas as pd


def prepare_orders(orders: pd.DataFrame) -> pd.DataFrame:
    processed_orders = orders.copy()

    processed_orders["region"] = (
        processed_orders["region"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    processed_orders["product_category"] = (
        processed_orders["product_category"]
        .fillna("Unknown")
        .astype(str)
        .str.strip()
        .str.title()
    )

    processed_orders["quantity"] = pd.to_numeric(
        processed_orders["quantity"],
        errors="coerce"
    ).fillna(1)

    processed_orders["unit_price"] = pd.to_numeric(
        processed_orders["unit_price"],
        errors="coerce"
    )

    processed_orders["unit_price"] = processed_orders["unit_price"].fillna(
        processed_orders["unit_price"].median()
    )

    processed_orders["discount"] = pd.to_numeric(
        processed_orders["discount"],
        errors="coerce"
    ).fillna(0)

    processed_orders["returned"] = (
        processed_orders["returned"]
        .fillna("false")
        .astype(str)
        .str.strip()
        .str.lower()
        .isin(["true", "yes", "1", "ja"])
    )

    processed_orders["order_value"] = (
        processed_orders["quantity"] * processed_orders["unit_price"]
    )

    processed_orders["discounted_value"] = (
        processed_orders["order_value"] * (1 - processed_orders["discount"])
    )

    return processed_orders