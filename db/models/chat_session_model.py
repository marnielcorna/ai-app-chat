from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.sql import func
from db.models.base import Base


class ChatSessionModel(Base):
    __tablename__ = "chat_session"

    session_id = Column(String, primary_key=True)
    user_id = Column(String, nullable=True)
    model_used = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    title = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
