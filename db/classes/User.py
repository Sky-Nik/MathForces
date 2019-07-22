import datetime

from sqlalchemy import Column, Integer, String, DateTime

from db.classes.Base import Base


class User(Base):
    __tablename__ = 'users'

    userType = Column(Integer, nullable=False)  # admin = 0, teacher = 1, student = 2
    handle = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    country = Column(String(255))  # nullable=True
    registredOn = Column(DateTime, default=datetime.datetime.utcnow)
    id = Column(Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        return f'<User(userType={self.userType}, handle="{self.handle}", password="{self.password}", ' \
               f'email="{self.email}", country="{self.country}", registredOn="{self.registredOn}", id={self.id})>'
