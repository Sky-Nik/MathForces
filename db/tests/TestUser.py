#!/usr/bin/env python
import os
import unittest

from db.classes import *
from db.get_session import get_session
from db.register_user import register_user


class TestUser(unittest.TestCase):
    def test_users_plain(self):
        try:
            os.remove('mf.db')
            session = get_session()
            a0 = User(userType=0, handle="A0", password="Aj7TT5maXQcnh2Bz", email="a.0@gmail.com", country="ua")
            t1 = User(userType=1, handle="T1", password="EPtTrQLzNJ9d8LSY", email="t.1@gmail.com", country="ua")
            t2 = User(userType=1, handle="T2", password="mMngvY3WK6pt6CeN", email="t.2@gmail.com", country="ru")
            session.add_all([a0, t1, t2])
            session.commit()
            register_user("S1", "UxagTUZXK8tnPtas", "s.1@gmail.com", "ua")
            register_user("S2", "EUZV4temA3zUAKWT", "s.2@gmail.com", "gb")
            register_user("S3", "83usnb6LfH2cASy7", "s.3@gmail.com", "ru")
            register_user("S4", "RQVVgBn4B45zuqzb", "s.4@gmail.com", "ua")
            for user in session.query(User):
                print(user)
        except:
            self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
