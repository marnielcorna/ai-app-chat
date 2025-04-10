from dotenv import load_dotenv
import os

load_dotenv()

USE_OLLAMA = os.getenv("USE_OLLAMA", "False").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OLLAMA_BASE_URL = "http://localhost:11434/v1"
