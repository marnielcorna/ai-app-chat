# chat_session.py

class ChatSession:
    def __init__(self, client, model: str, system_prompt="You are a helpful assistant."):
        self.client = client
        self.model = model
        self.messages = [{"role": "system", "content": system_prompt}]

    def add_user_message(self, content: str):
        self.messages.append({"role": "user", "content": content})

    def add_assistant_message(self, content: str):
        self.messages.append({"role": "assistant", "content": content})

    def run(self, stream_chat_func, temperature=0.7):
        return stream_chat_func(
            messages=self.messages,
            model=self.model,
            client=self.client,
            temperature=temperature
        )