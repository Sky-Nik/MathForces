#!/usr/bin/env python
import os
from contest_json2html import contest_json2html
from contest_json2html_table import contest_json2html_table
from problems2contest_tex import problems2contest_tex


def compile_contests():
  """ supposed to run from /py directory """
  os.chdir('../contests')
  for contest_id in map(lambda _: _[:-5], filter(lambda _: _[-5:] == '.json', os.listdir())):
    contest_json2html(contest_id)
    contest_json2html_table(contest_id)
    problems2contest_tex(contest_id)
  os.chdir('../py')


if __name__ == '__main__':
  compile_contests()
  # autoupdate on GitHub Pages:
  os.system('git add . && git commit -m "Recompiled all contests" && git push')
