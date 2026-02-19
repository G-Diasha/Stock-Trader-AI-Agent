import yfinance as yf
from crewai.tools import tool

@tool("Live Stock Research")
def get_stock_price(ticker_symbol:str)-> str:
    """
    This tool retrieves useful information about stock from the Yahoo Finance.
    There can be any stock eg MSFT, AAPL, TSLA. The pararmeters are the stock symbols, and
    the output will be the current price, daily change and other useful info about the stock.
    """
    stock = yf.Ticker(ticker_symbol)
    info = stock.info
    
    current_price = info.get("regulararketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    currency = info.get("currency", "USD")

    if current_price is None:
        return f"Could not fetch price for {ticker_symbol}."
    
    return (
        f"Stock: {ticker_symbol.upper()}\n"
        f"Price:{current_price} {currency}\n"
        f"Change: {change} ({round(change_percent, 2)}%)"
    )
