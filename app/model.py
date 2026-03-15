from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

class Post(Base):
        __tablename__ = 'posts'
        
        id = Column(Integer, primary_key=True, nullable=False)
        title = Column((String(255)), nullable=False)
        content = Column(String(255), nullable=False)
        published = Column(Boolean, server_default='1', nullable=False)
        created = Column(DateTime(timezone=True), server_default= func.now(),
                         nullable=False)
        owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
        owner_details = relationship("User")
class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True, nullable=False)
        email = Column(String(255), nullable=False, unique=True)
        password = Column(String(255), nullable=False)
        created_at = Column(DateTime(timezone=True), default=func.now())


class Vote(Base):
        __tablename__ = "votes"

        post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
        user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
# while True:
#     try:
#         conn = _mysql_connector.connect(
#             host = "localhost",
#             user = "root",
#             database = "fastapi",
#             password = "1234"
#         )
#         cursor = conn.cursor()
#         print("Connection to MySQL database was successful!")
#         break
#     except Exception as e:
#         print("Error Connecting to MysSQL database:", e)
#         time.sleep(2)

# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
#          {"title": "title of post 2", "content": "content of post 2", "id": 2}]