from chat import stream_chat


class InteractiveChat:
    def __init__(self, session):
        self.session = session

    def run(self):
        print("Interactive mode (type 'exit' to quit):\n")
        while True:
            user_input = input("You: ")
            if user_input.lower() in {"exit", "quit"}:
                break
            self.session.add_user_message(user_input)
            response = self.session.run(stream_chat)
            print(f"Assistant: {response}")
            self.session.add_assistant_message(response)
