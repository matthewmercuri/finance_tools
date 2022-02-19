from .data_sources import yfinance_clean


def validate_ticker(ticker: str, data_source: str) -> bool:
    """
    Inputs a ticker and returns True if data can be fetched
    for it, else False
    """
    if data_source == "yfinance":
        return yfinance_clean.validate_ticker(ticker)
    else:
        ValueError(f"{data_source} is not a valid data source.")


def ticker_metadata(ticker: str, data_source: str) -> dict:
    """
    Inputs a ticker and returns a dict of metadata about it
    """
    if data_source == "yfinance":
        return yfinance_clean.ticker_metadata(ticker)
    else:
        ValueError(f"{data_source} is not a valid data source.")
