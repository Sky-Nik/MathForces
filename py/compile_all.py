#!/usr/bin/env python
import os
from compile_gyms_table import compile_gyms_table
from compile_gyms import compile_gyms
from compile_contests_table import compile_contests_table
from compile_contests import compile_contests


def compile_all():
  compile_gyms_table()
  compile_gyms()
  compile_contests_table()
  compile_contests()


if __name__ == '__main__':
  compile_all()
  os.system('git add . && git commit -m "Recompiled all" && git push')
