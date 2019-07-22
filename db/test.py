#!/usr/bin/env python
import os

from db.get_session import get_session

if __name__ == "__main__":
    session = get_session()
    os.remove('mf.db')
