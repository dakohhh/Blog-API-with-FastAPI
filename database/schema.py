
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    date_created = Column(TIMESTAMP, server_default=text("NOW()"))

    blogs_created = relationship("Blog", back_populates="user")



class Blog(Base):
    __tablename__ = "blogs"

    blog_id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    blog_title = Column(String(100), nullable=False)

    blog_body = Column(String(100), index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="blogs_created")

