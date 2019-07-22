from sqlalchemy import Unicode
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine


def u_create_engine(string: str) -> Engine:
  return create_engine(string + '?charset=utf8mb4', encoding='utf-8')


def u_string(n: int) -> Unicode:
  return Unicode(n, collation='utf8_bin')
