#!/usr/bin/env python
import os

from py.compile_contests import compile_contests
from py.compile_contests_table import compile_contests_table
from py.compile_gyms import compile_gyms
from py.compile_gyms_table import compile_gyms_table
from py.compile_problems import compile_problems
from py.compile_problems_table import compile_problems_table


def compile_all():
    """ supposed to run from /py directory """
    compile_gyms_table()
    compile_gyms()
    compile_contests_table()
    compile_contests()
    compile_problems_table()
    compile_problems()


if __name__ == '__main__':
    compile_all()
    os.chdir('..')
    os.system('git add . && git commit -m "Recompiled all" && git push')
    os.chdir('py')
