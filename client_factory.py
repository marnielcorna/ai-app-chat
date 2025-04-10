from config.config import USE_OLLAMA, OPENAI_API_KEY, OLLAMA_BASE_URL
from openai import OpenAI


def get_client():
    if USE_OLLAMA:
        print("#### OLLAMA RUNNING ####")
        return OpenAI(
            base_url=OLLAMA_BASE_URL,
            api_key="ollama"  # Placeholder
        )
    else:
        print("### CHAT GPT RUNNING###")
        return OpenAI(api_key=OPENAI_API_KEY)
