#!/usr/bin/env python
import json


def problems2contest_tex(contest_id):
  """ supposed to run from /contests directory """
  contest = json.loads(open(f'{contest_id}.json', 'r', encoding='utf-8').read())
  contest_tex = '\\input{contest.sty}\n\n\\begin{document}\n\n\\title{Змагання ' + f"№{contest['id']}: {contest['name']}" + '}\n\\maketitle\n\n'

  for problem_id in contest['p_ids']:
    problem = json.loads(open(f'../problemset/{problem_id}.json', 'r', encoding='utf-8').read())
    contest_tex += '\\begin{problem}' + f"[{problem['name']}]" + '\n\t' + open(f"../problemset/{problem['id']}.tex", 'r', encoding='utf-8').read()+ '\n\\end{problem}\n\n'

  contest_tex += '\\end{document}'
  open(f'{contest_id}.tex', 'w', encoding='utf-8').write(contest_tex)
