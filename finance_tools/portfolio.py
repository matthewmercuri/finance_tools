from .data import *
from .errors import InvalidTicker


class Portfolio:
    """
    Allows user to build a portfolio object that can be passed
    to different modules to perform static analysis.

    N.B. This is not designed to handle for a dynamic portfolio with
    changing holdings.
    """

    QUANTITY_TYPES = ["shares", "weights"]
    BASE_CURRENCIES = ["usd", "cad"]
    DATA_SOURCES = ["yfinance"]

    def __init__(
        self,
        data_source: str = "yfinance",
        quantity_type: str = "shares",
        base_currency: str = "usd",
    ):
        data_source = data_source.strip().lower()
        quantity_type = quantity_type.strip().lower()
        base_currency = base_currency.strip().lower()

        if data_source not in self.DATA_SOURCES:
            raise ValueError(
                f"{data_source} is not a valid data source. Please pass one of {self.DATA_SOURCES}"
            )
        if quantity_type not in self.QUANTITY_TYPES:
            raise ValueError(
                f'{quantity_type} is not a valid quantity type for a portfolio. Please pass "shares" or "weights"'
            )
        if base_currency not in self.BASE_CURRENCIES:
            raise ValueError(
                f"{base_currency} is not a supported base currency for a portfolio. Please pass one of {self.BASE_CURRENCIES}"
            )

        self.data_source = data_source
        self.quantity_type = quantity_type
        self.base_currency = base_currency

        self.holdings = {}

    def get_holdings_list(self) -> list:
        return [*self.holdings]

    def add_position(
        self, ticker: str, quantity: float, skip_data_call: bool = False
    ) -> None:
        """
        Given a ticker and a quantity (amount of shares or weight), this
        method will add it as a holding to the Portfolio.holdings attribute.
        If skip_data_call is passed as True, there will be no metadata added
        nor will ticker validation be performed (could lead to errors later).
        """
        ticker = ticker.strip().upper()
        self.holdings[ticker] = {}

        if skip_data_call is not True:
            if validate_ticker(ticker, self.data_source) is False:
                raise InvalidTicker(ticker)

            metadata = ticker_metadata(ticker, self.data_source)
            self.holdings[ticker]["metadata"] = metadata

        self.holdings[ticker]["quantity"] = quantity
