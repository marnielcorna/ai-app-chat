import argparse
from client_factory import get_client
from chat import stream_chat
from chat_session import ChatSession
from config import USE_OLLAMA


def parse_args():
    parser = argparse.ArgumentParser(description="Chat with GPT or Ollama.")
    parser.add_argument("prompt", nargs="*", help="Prompt to send to the model")
    parser.add_argument("--interactive", action="store_true", help="Enable interactive chat mode")
    return parser.parse_args()


def main():
    args = parse_args()
    model = "llama3" if USE_OLLAMA else "gpt-4"
    client = get_client()
    session = ChatSession(client, model)

    if args.interactive:
        print("Interactive mode (type 'exit' to quit):\n")
        while True:
            user_input = input("You: ")
            if user_input.lower() in {"exit", "quit"}:
                break
            session.add_user_message(user_input)
            response = session.run(stream_chat)
            session.add_assistant_message(response)
    else:
        if not args.prompt:
            print("### Usage: python main.py \"your prompt here\" or --interactive")
            return
        prompt = " ".join(args.prompt)
        session.add_user_message(prompt)
        response = session.run(stream_chat)
        session.add_assistant_message(response)


if __name__ == "__main__":
    main()
