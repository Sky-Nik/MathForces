from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from db.classes import Base
from db.configure_logging import configure_logging


def get_session() -> Session:
    configure_logging()
    engine = create_engine('sqlite:///mf.db')  # , echo=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    return sessionmaker(bind=engine)()
