import pandas as pd

from order_report.reporting import (
    create_overview,
    create_sales_summary,
    create_returns_by_category,
)


def test_create_overview():
    processed_orders = pd.DataFrame(
        {
            "order_id": ["00001", "00002", "00003"],
            "discounted_value": [100.0, 200.0, 50.0],
            "returned": [False, True, False],
        }
    )

    overview = create_overview(processed_orders)

    assert overview.loc[0, "value"] == 350.0
    assert overview.loc[1, "value"] == 3
    assert overview.loc[2, "value"] == 1


def test_create_sales_summary_by_category():
    processed_orders = pd.DataFrame(
        {
            "order_id": ["00001", "00002", "00003"],
            "product_category": ["Electronics", "Electronics", "Clothing"],
            "discounted_value": [100.0, 200.0, 50.0],
            "returned": [False, True, False],
        }
    )

    summary = create_sales_summary(
        processed_orders,
        "product_category"
    )

    electronics = summary[
        summary["product_category"] == "Electronics"
    ].iloc[0]

    assert electronics["order_count"] == 2
    assert electronics["total_sales"] == 300.0
    assert electronics["returns"] == 1
    assert electronics["return_rate"] == 0.5


def test_create_returns_by_category():
    processed_orders = pd.DataFrame(
        {
            "order_id": ["00001", "00002", "00003", "00004"],
            "product_category": [
                "Electronics",
                "Electronics",
                "Clothing",
                "Clothing",
            ],
            "returned": [True, False, True, True],
        }
    )

    returns_summary = create_returns_by_category(processed_orders)

    clothing = returns_summary[
        returns_summary["product_category"] == "Clothing"
    ].iloc[0]

    assert clothing["order_count"] == 2
    assert clothing["returns"] == 2
    assert clothing["return_rate"] == 1.0