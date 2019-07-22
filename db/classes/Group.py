import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from db.classes.Base import Base


class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    createdOn = Column(DateTime, default=datetime.datetime.utcnow)
    createdBy = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f"<Group(name={self.name}, createdOn={self.createdOn}, createdBy={self.createdBy})>"
