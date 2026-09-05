import pandas as pd

from order_report.processing import prepare_orders


def test_prepare_orders_calculates_order_value():
    orders = pd.DataFrame(
        {
            "region": ["south"],
            "product_category": ["electronics"],
            "quantity": [2],
            "unit_price": [100],
            "discount": [0],
            "returned": ["false"],
        }
    )

    processed_orders = prepare_orders(orders)

    assert processed_orders.loc[0, "order_value"] == 200


def test_prepare_orders_calculates_discounted_value():
    orders = pd.DataFrame(
        {
            "region": ["south"],
            "product_category": ["electronics"],
            "quantity": [2],
            "unit_price": [100],
            "discount": [0.25],
            "returned": ["false"],
        }
    )

    processed_orders = prepare_orders(orders)

    assert processed_orders.loc[0, "discounted_value"] == 150


def test_prepare_orders_cleans_text_values():
    orders = pd.DataFrame(
        {
            "region": ["  south "],
            "product_category": [" electronics "],
            "quantity": [1],
            "unit_price": [100],
            "discount": [0],
            "returned": ["false"],
        }
    )

    processed_orders = prepare_orders(orders)

    assert processed_orders.loc[0, "region"] == "South"
    assert processed_orders.loc[0, "product_category"] == "Electronics"


def test_prepare_orders_converts_returned_to_boolean():
    orders = pd.DataFrame(
        {
            "region": ["South"],
            "product_category": ["Electronics"],
            "quantity": [1],
            "unit_price": [100],
            "discount": [0],
            "returned": ["yes"],
        }
    )

    processed_orders = prepare_orders(orders)

    assert bool(processed_orders.loc[0, "returned"]) is True