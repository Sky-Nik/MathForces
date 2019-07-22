import datetime

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from db.classes.Base import Base


class BlogPost(Base):
    __tablename__ = 'blog_posts'

    authorId = Column(Integer, ForeignKey('users.id'))
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255))
    publishedOn = Column(DateTime, default=datetime.datetime.utcnow)

    author = relationship("User", back_populates="blogPosts")

    def __repr__(self):
        return f'<BlogPost(id={self.id}, authorId={self.authorId}, ' \
               f'title="{self.title}", publishedOn={self.publishedOn})>'
