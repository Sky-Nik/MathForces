#!/usr/bin/env python
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.classes import *

os.remove('mf.db')
engine = create_engine('sqlite:///mf.db', echo=True)
Base.metadata.create_all(engine)
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()
