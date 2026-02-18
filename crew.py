from crewai import Crew
from agents.analyst_agent import analyst_agent
from agents.trader_agent import trader_agent
from tasks.analysis_task import get_stock_analysis
from tasks.trade_task import trade_action

stock_crew = Crew(
    agents = [analyst_agent, trader_agent],
    tasks = [get_stock_analysis, trade_action],
    verbose = True
)

