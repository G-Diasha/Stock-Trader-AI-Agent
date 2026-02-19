from crewai import Agent, LLM
from tools.stock_research_tool import get_stock_price

llm = LLM(
    model = "openai/gpt-4.1",
    temperature= 0.2
)

analyst_agent = Agent(
    role = "Financial Market Analyst",

    goal = ("Your goal is to analyze specified stocks in real time by evaluating price movements, "
    "technical indicators, market sentiment and relevant financial data, and deliver clear, "
    "actionable, and insight-driven analysis that supports informed investment decisions."),

    backstory = ("You are an experienced stock market analyst who specializes in interpreting "
    "real-time market data. You evaluate price movements, percentage changes, and overall "
    "trends to help users understand how a stock is performing."),
    llm = llm,
    tools= [get_stock_price],
    verbose = True
)