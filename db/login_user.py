#!/usr/bin/env python
import logging
import sys

from sqlalchemy.orm.exc import NoResultFound

from db.classes import User
from db.get_session import get_session


def login_user(handle_, password_) -> int:
    """ returns exception code if any else 0"""
    user_session = get_session()
    try:
        user = user_session.query(User).filter(User.handle == handle_).one()
        if user.password == password_:
            return 0
        else:
            logging.error(f"Wrong password for provided user handle.")
            return 1
    except NoResultFound as nrf:
        logging.error(nrf)
        logging.error(f"No user with provided user handle exists.")
        return 2
    except Exception as e:  # idk if this is possible
        logging.critical(e)
        return 3


if __name__ == "__main__":
    """ call this script with
        python login_user.py "HANDLE" "PASSWORD" """
    logging.info(f'''User login returned {login_user(
        handle_=sys.argv[1],
        password_=sys.argv[2],
    )}''')
