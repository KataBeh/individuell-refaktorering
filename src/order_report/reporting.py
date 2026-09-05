import pandas as pd
import logging
from pathlib import Path

import pandas as pd


logger = logging.getLogger(__name__)

# overview funktion
def create_overview(processed_orders: pd.DataFrame) -> pd.DataFrame:        # min kod är nästan som orginalet men ligger i en funktion istället
    total_sales = round(
        processed_orders["discounted_value"].sum(),
        2
    )

    number_of_orders = processed_orders["order_id"].nunique()
    number_of_returns = int(processed_orders["returned"].sum())

    overview = pd.DataFrame(
        {
            "metric": [
                "total_sales",
                "order_count",
                "return_count",
            ],
            "value": [
                total_sales,
                number_of_orders,
                number_of_returns,
            ],
        }
    )

    return overview




# försäljning per kategori och region, det här löser min fynd 7, med duplicerade koder GROUPBY
def create_sales_summary(
    processed_orders: pd.DataFrame,
    group_by: str
) -> pd.DataFrame:

    summary = (
        processed_orders.groupby(
            group_by,
            as_index=False
        )
        .agg(
            order_count=("order_id", "nunique"),
            total_sales=("discounted_value", "sum"),
            returns=("returned", "sum"),
        )
    )

    summary["total_sales"] = summary["total_sales"].round(2)

    summary["return_rate"] = (
        summary["returns"]
        / summary["order_count"]
    ).round(3)

    summary = (
        summary
        .sort_values(
            "total_sales",
            ascending=False
        )
        .reset_index(drop=True)
    )

    return summary




# returer per kategori
def create_returns_by_category(
    processed_orders: pd.DataFrame
) -> pd.DataFrame:

    returns_by_category = (
        processed_orders.groupby(
            "product_category",
            as_index=False
        )
        .agg(
            order_count=("order_id", "nunique"),
            returns=("returned", "sum"),
        )
    )

    returns_by_category["return_rate"] = (
        returns_by_category["returns"]
        / returns_by_category["order_count"]
    ).round(3)

    returns_by_category = (
        returns_by_category
        .sort_values(
            "return_rate",
            ascending=False
        )
        .reset_index(drop=True)
    )

    return returns_by_category




def save_report(
    report: pd.DataFrame,
    output_dir: Path,               # skapar mappen om den inte redan finns
    filename: str
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / filename

    report.to_csv(
        output_path,
        index=False
    )

    logger.info("Sparade rapport till %s", output_path)