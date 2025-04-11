import logging
from datetime import datetime

from db.models.chat_message_model import ChatMessageModel
from sqlalchemy.orm import Session

from db.models.chat_session_model import ChatSessionModel


class ChatDB:
    def __init__(self, db_session: Session, user_id=None):
        self.db_session = db_session
        self.user_id = user_id

    def get_messages(self, session_id=None, user_id=None, limit=50):
        query = self.db_session.query(ChatMessageModel).order_by(ChatMessageModel.created_at.desc())

        if session_id:
            query = query.filter(ChatMessageModel.session_id == session_id)
        elif user_id:
            query = query.filter(ChatMessageModel.user_id == user_id)
        else:
            return []

        messages = query.limit(limit).all()
        return [{"role": m.role, "content": m.content} for m in reversed(messages)]

    def save_message(self, session_id, role, content):

        try:
            message = ChatMessageModel(
                session_id=session_id,
                role=role,
                content=content,
                user_id=self.user_id
            )
            self.db_session.add(message)
            self.db_session.commit()
            self.update_session_timestamp(session_id)
        except Exception as e:
            logging.error(f"Failed to save message to DB: {e}")
            self.db_session.rollback()

    def create_session(self, session_id: str, model: str):
        try:
            new_session = ChatSessionModel(
                session_id=session_id,
                user_id=self.user_id,
                model_used=model
            )
            self.db_session.add(new_session)
            self.db_session.commit()
        except Exception as e:
            logging.error(f"Failed to create session: {e}")
            self.db_session.rollback()

    def update_session_timestamp(self, session_id: str):
        try:
            session = self.db_session.query(ChatSessionModel) \
                .filter_by(session_id=session_id) \
                .first()
            if session:
                session.updated_at = datetime.utcnow()
                self.db_session.commit()
        except Exception as e:
            logging.error(f"Failed to update session timestamp: {e}")
            self.db_session.rollback()

