# db/models/user_model.py
from sqlalchemy import Column, String, DateTime
from db.models.base import Base
from datetime import datetime


class UserModel(Base):
    __tablename__ = "users"

    user_id = Column(String, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    role = Column(String, nullable=False, default="user")
    created_at = Column(DateTime, default=datetime.utcnow)
