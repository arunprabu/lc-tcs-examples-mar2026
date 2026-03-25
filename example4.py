# agent example with linkedin post writer agent
import os 
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

my_agent = create_agent(
  model="google_genai:gemini-2.5-flash",  #brain
  system_prompt="""You are a LinkedIn Post Writer. 
  You must create engaging and informative posts. 
  You should never work on anything else. 
  If users ask you to do something outside of this scope,
   politely decline.""", # roles and goals for the agent
)

response = my_agent.invoke(
  {
    "messages": [
      # {"role": "user", "content": """Write a LinkedIn post about the 
      # importance of AI in modern business."""}
      # checking if the agent sticks to its role and declines out of scope requests
      {"role": "user", "content": """Write an email to my manager about the 
      progress of the AI project."""}
    ]
  }
)

print(response["messages"][-1].text)