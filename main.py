import argparse
import uuid
from client_factory import get_client
from chat_session import ChatSession
from utils.interactive_chat import InteractiveChat
from config.config import USE_OLLAMA, SYSTEM_PROMPT

from db.models.base import Base
from db.connection import Database
from db.chat_db import ChatDB


def parse_args():
    parser = argparse.ArgumentParser(description="Chat with GPT or Ollama.")
    parser.add_argument("--session", help="Optional session ID to continue a chat", default=None)
    parser.add_argument("--user", help="User ID", required=True)
    return parser.parse_args()


def main():
    args = parse_args()

    # Setup client and model
    model = "llama3" if USE_OLLAMA else "gpt-4"
    client = get_client()

    # Initialize database
    db = Database()

    # Makes sure that the app doesn't crash later due to missing tables.
    Base.metadata.create_all(db.engine)
    db_session = db.get_session()
    chat_db = ChatDB(db_session, user_id=args.user)

    # Create or reuse session
    session_id = args.session or str(uuid.uuid4())
    print(f"Session ID: {session_id}")
    chat_db.create_session(session_id, model)

    # Initialize chat session
    session = ChatSession.create(client, model, session_id, db=chat_db, system_prompt=SYSTEM_PROMPT, user_id=args.user)

    interactive_chat = InteractiveChat(session)
    interactive_chat.run()


if __name__ == "__main__":
    main()
