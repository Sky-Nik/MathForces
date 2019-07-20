#!/usr/bin/env python
import os
from gym_json2html import gym_json2html
from gym_json2html_table import gym_json2html_table
from problems2gym_tex import problems2gym_tex


def compile_gyms():
  """ supposed to run from /py directory """
  os.chdir('../gyms')
  for gym_id in map(lambda _: _[:-5], filter(lambda _: _[-5:] == '.json', os.listdir())):
    gym_json2html(gym_id)
    gym_json2html_table(gym_id)
    problems2gym_tex(gym_id)
  os.chdir('../py')


if __name__ == '__main__':
  compile_gyms()
  # autoupdate on GitHub Pages:
  os.system('git add . && git commit -m "Recompiled all gyms" && git push')
