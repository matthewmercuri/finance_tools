from finance_tools import portfolio
from finance_tools.portfolio import Portfolio

portfolio = Portfolio()
portfolio.add_position("td.to", 10, skip_data_call=True)
portfolio.add_position("msft", 10, skip_data_call=True)
print(portfolio.get_holdings_list())
