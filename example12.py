# getting inputs from user
import os
from langchain.agents import create_agent
from langchain_core.tools import tool   
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
from tavily import TavilyClient


load_dotenv()
client = TavilyClient(os.getenv("TAVILY_API_KEY"))


# ── 1. Define structured output schema ──────────────────────────────────────
class NewsArticle(BaseModel):
    """A single news article."""
    title: str = Field(description="Title of the article")
    source: str = Field(description="Publisher or source name")
    summary: str = Field(description="Brief summary of the article")
    url: str = Field(description="URL of the article, empty string if unavailable")


class AINewsResponse(BaseModel):
    """Structured response for AI news queries."""
    topic: str = Field(description="The specific topic of AI news covered")
    articles: List[NewsArticle] = Field(description="List of relevant articles found")
    overall_summary: str = Field(description="High-level summary of current AI news")


# ── 2. Decorate tools with @tool ─────────────────────────────────────────────
@tool
def get_weather_tool(city: str) -> str:
    """A simple tool that fetches weather information for a given city."""
    print(f"Fetching weather information for {city}...")
    api_key = os.getenv("OPENWEATHER_API_KEY")
    api_url = os.getenv("OPENWEATHER_API_URL")
    return f"In {city} temperature is 25°C."


@tool
def websearch_tool(query: str) -> str:
    """Use this for general web search queries."""
    print(f"Performing web search for {query}...")
    response = client.search(
        query=query,
        search_depth="advanced"
    )
    return response


# ── 3. Get topic input from user ──────────────────────────────────────────────
def main():
    topic = input("\nEnter a topic to search news about: ").strip()

    if not topic:
        print("No topic provided. Exiting.")
        return

    print(f"\n🔍 Searching for news on: '{topic}'...\n")

    # ── 4. Pass response_format to create_agent ──────────────────────────────
    general_purpose_agent = create_agent(
        model="google_genai:gemini-3.1-pro-preview",
        tools=[get_weather_tool, websearch_tool],
        response_format=AINewsResponse,
        system_prompt="""You are a helpful assistant.
        You are given two tools - get_weather_tool which fetches weather information for a given city,
        and websearch_tool which performs general web searches.
        If the tool outputs are not sufficient to answer the query,
        say you are unable to answer instead of making up a response.
        """
    )

    response = general_purpose_agent.invoke(
        {
            "messages": [
                {"role": "user", "content": f"Tell me about latest news on: {topic}"}
            ]
        }
    )

    # ── 5. Access structured output ───────────────────────────────────────────
    news: AINewsResponse = response["structured_response"]

    print(f"Topic: {news.topic}")
    print(f"\nOverall Summary:\n{news.overall_summary}")
    print(f"\nArticles ({len(news.articles)}):")
    for article in news.articles:
        print(f"\n  [{article.source}] {article.title}")
        print(f"  {article.summary}")
        if article.url:
            print(f"  🔗 {article.url}")


if __name__ == "__main__":
    main()