from crewai import Task
from agents.analyst_agent import analyst_agent

get_stock_analysis = Task(
    description= ("Analyze the recent performance of the stock: {stock}. Use the live stockresearch tool to retrieve current price, percentage change, trading volume and other marketdata. Provide a summary of how the stock is performing today and highlight any key observations from the dataz�A clear bullet-pointed summary of:{stock}"
    "which will include current stock price, percentage change, trading volume, and other market" \
    "data. Provide a summary of how the stock is performing today and highlight any key observations" \
    "from the data")
    expected_output = ("A clear bullet-pointed summary of:\n"
"-Current stock price\n"
"-Daily price change and percentage\n"
"-volume and volatility\n"
"-any immediate trends or observations"),
agent = analyst_agent
)
