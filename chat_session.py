class ChatSession:
    def __init__(self, client, model: str, session_id=None, system_prompt="You are a helpful assistant.", db=None):
        self.client = client
        self.model = model
        self.session_id = session_id
        self.db = db
        self.messages = self._load_messages_from_db() if self.db and self.session_id else [
            {"role": "system", "content": system_prompt}
        ]

    def _load_messages_from_db(self):
        return self.db.get_messages(session_id=self.session_id)

    def _store_message(self, role, content):
        if self.db and self.session_id:
            self.db.save_message(self.session_id, role, content)

    def add_user_message(self, content: str):
        self.messages.append({"role": "user", "content": content})
        self._store_message("user", content)

    def add_assistant_message(self, content: str):
        self.messages.append({"role": "assistant", "content": content})
        self._store_message("assistant", content)

    def run(self, stream_chat_func, temperature=0.7):
        return stream_chat_func(
            messages=self.messages,
            model=self.model,
            client=self.client,
            temperature=temperature
        )
