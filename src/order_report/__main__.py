# kom ihåg att main gör inte själva jobbet, utan talar bara om i vilken ordning delarna ska köras

from order_report.logging_config import configure_logging
from order_report.config import ReportConfig
from order_report.loading import load_orders
from order_report.validation import validate_columns, validate_not_empty
from order_report.processing import prepare_orders
from order_report.reporting import (
    create_overview,
    create_sales_summary,
    create_returns_by_category,
    save_report,
)


def main() -> None:
    configure_logging()

    config = ReportConfig()
    orders = load_orders(config.input_path)

    validate_not_empty(orders)
    validate_columns(orders)

    processed_orders = prepare_orders(orders)

    overview = create_overview(processed_orders)

    sales_by_category = create_sales_summary(
        processed_orders,
        "product_category"
    )

    sales_by_region = create_sales_summary(
        processed_orders,
        "region"
    )

    returns_by_category = create_returns_by_category(
        processed_orders
    )


if __name__ == "__main__":
    main()