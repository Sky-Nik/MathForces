#!/usr/bin/env python
import json


def problems2gym_tex(gym_id):
    """ supposed to run from /gyms directory """
    gym = json.loads(open(f'{gym_id}.json', 'r', encoding='utf-8').read())
    gym_tex = '''
\\input{gym.sty}
\\begin{document}
\\title{Тренування ''' + f"№{gym['id']}: {gym['name']}" + '''}
\\maketitle
'''

    for problem_id in gym['p_ids']:
        problem = json.loads(open(f'../problemset/{problem_id}.json', 'r', encoding='utf-8').read())
        gym_tex += '\\begin{problem}' + f"[{problem['name']}]" + '\n\t' + \
                   open(f"../problemset/{problem['id']}.tex", 'r', encoding='utf-8').read() + '\n\\end{problem}\n\n'

    gym_tex += '\\end{document}'
    open(f'{gym_id}.tex', 'w', encoding='utf-8').write(gym_tex)
