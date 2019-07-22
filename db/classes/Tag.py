from sqlalchemy import Column, Integer, String

from db.classes.Base import Base


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)

    def __repr__(self):
        return f'<Tag(id={self.id}, name="{self.name}")>'
