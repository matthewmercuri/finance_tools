from finance_tools import portfolio
from finance_tools.portfolio import Portfolio

portfolio = Portfolio()
portfolio.add_position("td.to", 10)
print(portfolio.holdings)
