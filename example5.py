# agent with 2 tools 
import os
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_core.tools import tool
from tavily import TavilyClient

load_dotenv()  # Load environment variables from .env file
client = TavilyClient(os.getenv("TAVILY_API_KEY"))

# let's create a tool that fetches weather information for a given city. 
@tool
def get_weather_tool(city: str) -> str:
    """A simple tool that simulates fetching weather information for a given city."""
    print(f"Fetching weather information for {city}...")
    # lets connect to a weather API and fetch the weather information for the city.
    api_key = os.getenv("OPENWEATHER_API_KEY")  # get API key
    api_url = os.getenv("OPENWEATHER_API_URL")  # get API URL

    # TODO: Make an API call to fetch weather information for the city using the api_key and api_url
    return f"In {city} temperature is 25°C."

# web search tool
@tool
def websearch_tool(query: str) -> str:
  """use this for general web search queries"""
  print(f"Performing web search for {query}...")
  response = client.search(
      query=query,
      search_depth="advanced"
  )
  return response

general_purpose_agent = create_agent(
  model="google_genai:gemini-3.1-pro-preview",  #brain
  tools=[get_weather_tool, websearch_tool],  # registering the tools
  system_prompt="""You are a helpful assistant. 
  You are given two tools - get_weather which fetches weather information for a given city, 
  and websearch which performs general web searches. 
  If the outputs from the tools are not sufficient to answer the user's query, 
  tell the user that you are not able to answer the query instead of making up an answer. 
  """
)

response = general_purpose_agent.invoke(
  {
    "messages": [
      {"role": "user", "content": "Tell me about latest AI news"}
    ]
  }
) 

print(response["messages"][-1].text)