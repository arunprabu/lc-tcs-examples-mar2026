# first example

# uv add langchain "langchain[google-genai]"
from langchain.chat_models import init_chat_model
import os 

os.environ["GEMINI_API_KEY"] = "AIzaSyBuc0AMmj_q2OI4gihiU6zFR1j29oSEG8c"
model = init_chat_model("google_genai:gemini-3-pro-preview")

response = model.invoke("Why do parrots talk?")

print(response)
