from order_report.logging_config import configure_logging
from order_report.config import ReportConfig
from order_report.loading import load_orders
from order_report.validation import validate_columns, validate_not_empty
from order_report.processing import prepare_orders


def main() -> None:
    configure_logging()

    config = ReportConfig()
    orders = load_orders(config.input_path)

    validate_not_empty(orders)
    validate_columns(orders)

    processed_orders = prepare_orders(orders)



if __name__ == "__main__":
    main()