from crewai import Agent, LLM

llm = LLM(
    model = "openai/gpt-4.1",
    temperature= 0.2
)

trader_agent = Agent(
    role = "Strategic Stock Trader",
    goal = ("Decide whether to Buy, Sell or Hold a given stock based on live stock data"
    ",price movements and the available financial data analysis"),
    backstory = ("You are a strategic trader with years of experience in timing market entry and"
    "exit points. You rely on real-time stock data, daily price movements, and volume trends"
    "to make trending decisions that optimize returns and redue risks."),
    llm= llm,
    tools = [],
    verbose = True
)