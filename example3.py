# weather agent example
import os
from langchain.agents import create_agent
from langchain_core.tools import tool
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

# let's create a tool that fetches weather information for a given city. 
@tool
def get_weather(city: str) -> str:
    """A simple tool that simulates fetching weather information for a given city."""
    print(f"Fetching weather information for {city}...")
    # lets connect to a weather API and fetch the weather information for the city.
    api_key = os.getenv("OPENWEATHER_API_KEY")  # get API key
    api_url = os.getenv("OPENWEATHER_API_URL")  # get API URL

    # TODO: Make an API call to fetch weather information for the city using the api_key and api_url
    return f"In {city} temperature is 25°C."

weather_agent = create_agent(
  model="google_genai:gemini-2.5-flash",  #brain
  tools=[get_weather],  # registering the tools
  system_prompt="""You are a weather assistant. 
  You must provide accurate weather information for the requested city. 
  You should not answer any other questions outside your scope.""", # roles and goals for
)

response = weather_agent.invoke(
  {
    "messages": [
      {"role": "user", "content": "Tell me about Weather in chennai"}
    ]
  }
) 

print(response)