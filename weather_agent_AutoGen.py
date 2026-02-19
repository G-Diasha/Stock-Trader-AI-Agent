from dotenv import load_dotenv
import os
import requests
import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()
open_weather_api = os.getenv('OPENWEATHER_API_KEY')
openai_api_key = os.getenv('OPENAI_API_KEY')

model_client = OpenAIChatCompletionClient(
    model = "gpt-4.1"
)
#defining weather retrieval tool
async def get_weather(city: str) -> str:
    """This tool helps to fetch weather data from the OpenWeatherMap API"""
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        units = "metric"
        params = {
            "q": city,
            "appid": open_weather_api,
            "units": units
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return f"Could not fetch weather data for {city}! Status code: {response.status_code}"
        data = response.json()
        if "weather" not in data:
            return f"Weather data not found for {city}!"
        desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        location = data["name"]
        return f"The weather in {location} is {desc} with a temperature of {temp}°C."
    except Exception as e:
        return f"Error: {str(e)}"
    
#Defining the Assistant agent with the tool
agent = AssistantAgent(
    name = "weather_agent",
    system_message = ("You are a helpful weather assistant. When the user asks about the weather for any city, provide the weather using the 'get_weather' tool."),
    model_client = model_client,
    tools =[get_weather],
    reflect_on_tool_use = True,
    model_client_stream= True)

async def main():
  await Console(agent.run_stream(task="What is the weather in Dhaka?")) #console is used to display response stream
  await model_client.close()

if __name__ == "__main__":
    asyncio.run(main())
