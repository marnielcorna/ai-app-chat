import sys
from client_factory import get_client
from chat import stream_chat
from config import USE_OLLAMA


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"your prompt here\"")
        return

    # Get prompt from command-line args
    prompt = " ".join(sys.argv[1:])

    # Dynamically choose model
    model = "llama3" if USE_OLLAMA else "gpt-4"
    client = get_client()

    # Debug print
    print(f"Prompt to {model}: {prompt}")

    # Stream response
    stream_chat(prompt=prompt, model=model, client=client)


if __name__ == "__main__":
    main()
