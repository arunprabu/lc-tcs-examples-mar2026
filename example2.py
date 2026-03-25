# agent example
import os 
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

my_agent = create_agent(
  model="google_genai:gemini-3.1-pro",  #brain
  system_prompt="You are a helpful assistant", # roles and goals for the agent
)

response = my_agent.invoke(
  {
    "messages": [
      {"role": "user", "content": "What is the capital of France?"}
    ]
  }
)

print(response["messages"][-1].text)