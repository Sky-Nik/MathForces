#!/usr/bin/env python
import os
import json


def compile_contests_table():
    """ supposed to run from /py directory """
    os.chdir('../contests')
    compiled_contests_table = ""
    for file in filter(lambda _: os.path.splitext(_)[1] == '.json', os.listdir()):
        contest = json.loads(open(file, 'r', encoding='utf-8').read())
        assert contest['type'] == 'contest'
        compiled_contests_table += f'''              <tr contest-id="{contest['id']}">
                <td class="contest-number-column"><a href="/MathForces/contests/{contest['id']}_t.html">{contest['id']}</a></td>
                <td class="contest-name-column"><a href="/MathForces/contests/{contest['id']}_t.html">{contest['name']}</a></td>
                <td class="contest-start-time-column">{contest['start_time'].replace(', ', '<br>')}</td>
                <td class="contest-duration-column">{contest['duration'].zfill(5)}</td>
              </tr>
'''
    # update index:
    index_lines = open('index.html', 'r', encoding='utf-8').readlines()
    table_body_start = index_lines.index('            <tbody id="contests-table-body">\n')
    table_body_end = index_lines.index('            </tbody>\n')
    index_lines = index_lines[:table_body_start + 1] + [compiled_contests_table, ] + index_lines[table_body_end:]
    open('index.html', 'w', encoding='utf-8').writelines(index_lines)
    os.chdir('../py')


if __name__ == '__main__':
    compile_contests_table()
    # autoupdate on GitHub Pages:
    os.system('git add . && git commit -m "Recompiled contests table" && git push')
