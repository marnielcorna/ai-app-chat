class ChatSession:
    def __init__(self, client, model: str, session_id=None, messages=None, db=None, user_id=None):
        self.user_id = user_id
        self.client = client
        self.model = model
        self.session_id = session_id
        self.db = db
        self.messages = messages or []

    @staticmethod
    def create(client, model: str, session_id=None, db=None, system_prompt=None, user_id=None):
        system_prompt = system_prompt or "You are a helpful assistant."

        if db:
            if user_id:
                messages = db.get_messages(user_id=user_id, limit=50)
            else:
                messages = [{"role": "system", "content": system_prompt}]
        else:
            messages = [{"role": "system", "content": system_prompt}]

        return ChatSession(client, model, session_id=session_id, messages=messages, db=db, user_id=user_id)

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

    def get_last_n_messages(self, n=10):
        print(f"[DEBUG] Fetching last {n} messages...")
        if self.db:
            if self.user_id:
                return self.db.get_messages(user_id=self.user_id, limit=n)
        return self.messages[-n:]



