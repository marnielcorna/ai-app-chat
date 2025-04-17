from chat import stream_chat


class ChatOutPut:
    def __init__(self, session):
        self.session = session

    def get_user_input(self):
        return input("You: ")

    def process_input(self, user_input):
        self.session.add_user_message(user_input)
        response = self.session.run(stream_chat)
        self.session.add_assistant_message(response)
        print(f"Assistant: {response}")

    def run(self):
        print("Interactive mode (type 'exit' to quit, 'history' to show last messages):\n")
        while True:
            user_input = self.get_user_input()
            if user_input.lower() in {"exit", "quit"}:
                break
            elif user_input.lower() == "history":
                self.show_history()
            else:
                self.process_input(user_input)

    def show_history(self, n=10):
        messages = self.session.get_last_n_messages(n=n)
        print(f"\n--- Last {n} Messages ---")
        for msg in messages:
            role = msg["role"].capitalize()
            print(f"{role}: {msg['content']}")
        print("--- End ---\n")

