import nest_asyncio
from dotenv import load_dotenv

nest_asyncio.apply()
import os
import requests
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from pydantic_ai import ModelSettings

load_dotenv()
open_weather_api = os.getenv('OPENWEATHER_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')

#Defining the output schema of the tool using pydantic BaseModel
class weatherForecast(BaseModel):
  city: str
  description: str
  temperature: float

#Creating the AI Agent using Groq's Llama 3.3 model
weather_agent = Agent(
    model = "groq:llama-3.3-70b-versatile",
    model_settings= ModelSettings(temperature=0.3),
    system_prompt = ("You are a helpful weather assistant" "Use the 'get_forecast_for_city' function to get the weather forecast for a given city" 
"Provide clear and friendly responses"))

#Registering a tool with the AI Agent to get real-time weather data from the Openweather Map API
@weather_agent.tool
def get_forecast_for_city(ctx: RunContext, city: str) -> weatherForecast:
  """This function helps to get the weather forecast from the OpenWeatherMap API"""
  url = "https://api.openweathermap.org/data/2.5/weather"
  units = "metric"
  params = {
      "q": city,
      "appid": open_weather_api,
      "units" : units}
  #sending request to weather API
  response = requests.get(url, params=params).json()
  #returning the formatted weather data
  return weatherForecast(
      city = response["name"],
      description= response["weather"][0]["description"],
      temperature = response["main"]["temp"]
  )
#Run continuous user-interaction loop
if __name__=="__main__":
  print("Weather forecast agent is ready! Type exit to quit the agent")
  print("_"*50)
  while True:
   question =input("Ask about the weather for any city.").strip()
   if question.lower() in {"exit", "quit", ""}:
    break
   try:
    agent_response = weather_agent.run_sync(question)
    print("Weather update: ", agent_response.output)
   except Exception as e:
    print("Error", str(e))
     