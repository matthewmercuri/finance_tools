class InvalidTicker(Exception):
    """
    Exception raised when a ticker is not valid (at least for the data source)

    Attributes:
        ticker -- ticker that is invalid
        message -- explanation as to why the error was raised
    """

    def __init__(self, ticker, message="Unable to fetch data for the given ticker"):
        self.ticker = ticker
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.ticker} -> {self.message}"
