#!/usr/bin/env python
import os

from py.problem_json2html import problem_json2html


def compile_problems():
    """ supposed to run from /py directory """
    os.chdir('../problemset')
    for problem_id in map(lambda _: _[:-5], filter(lambda _: _[-5:] == '.json', os.listdir('.'))):
        problem_json2html(problem_id)
    os.chdir('../py')


if __name__ == "__main__":
    compile_problems()
    # auto-update on GitHub Pages:
    os.system('git add . && git commit -m "Recompiled all problems" && git push')
