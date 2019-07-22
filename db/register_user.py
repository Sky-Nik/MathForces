#!/usr/bin/env python
import logging
import sys

from sqlalchemy.exc import IntegrityError

from db.classes import User
from db.get_session import get_session


def register_user(handle_, password_, email_, country_) -> int:
    """ returns exception code if any else 0"""
    user_session = get_session()
    try:
        # auto-registration is possible for students only
        user_session.add(User(
            userType=2,
            handle=handle_,
            password=password_,
            email=email_,
            country=country_
        ))
        user_session.commit()
        return 0
    except IntegrityError as ie:  # UNIQUE constraint failed
        logging.error(ie)
        if user_session.query(User.handle == handle_):
            logging.error('Provided handle is already taken.')
            return 1
        elif user_session.query(User.email == email_):
            logging.error('Provided email is already in use.')
            return 2
        else:  # idk if this is possible
            return 3
    except Exception as e:  # idk if this is possible
        logging.critical(e)
        return 4


if __name__ == "__main__":
    """ call this script with
        python register_user.py "HANDLE" "PASSWORD" "EMAIL" ["COUNTRY"] """
    logging.info(f'''User registration returned {register_user(
        handle_=sys.argv[1],
        password_=sys.argv[2],
        email_=sys.argv[3],
        country_=sys.argv[4]
    )}''')
