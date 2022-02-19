import yfinance as yf


def validate_ticker(ticker: str) -> bool:
    """
    Inputs a ticker and returns True if data can be fetched
    for it, else False
    """
    ticker_data = None
    try:
        ticker_data = yf.Ticker(ticker).info["symbol"]
    except Exception as e:
        print(e)

    if ticker_data is not None:
        return True
    else:
        return False


def ticker_metadata(ticker: str) -> dict:
    """
    Inputs a ticker and returns a dict of metadata about it
    """
    try:
        ticker_data = yf.Ticker(ticker)
        return ticker_data.info
    except Exception as e:
        print(e)
