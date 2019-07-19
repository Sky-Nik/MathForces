#!/usr/bin/env python
import os
import json


if __name__ == '__main__':
  compiled_problems_table = ""
  for file in filter(lambda _: os.path.splitext(_)[1] == '.json', os.listdir()):
    problem = json.loads(open(file, 'r', encoding='utf-8').read())
    assert problem['type'] == 'problem'
    compiled_problems_table += f'''              <tr class="problem-item">
                <td class="problem-number"><a href="/MathForces/problemset/{problem['id']}">{problem['id']}</a></td>
                <td class="problem-name"><a href="/MathForces/problemset/{problem['id']}">{problem['name']}</a></td>
                <td class="problem-tags">{', '.join(problem['tags'])}</td>
                <td class="problem-difficulty">{problem['difficulty']}</td>
              </tr>
'''
  # update index:
  index_lines = open('index.html', 'r', encoding='utf-8').readlines()
  table_body_start = index_lines.index('            <tbody id="problems_table_body">\n')
  table_body_end = index_lines.index('            </tbody>\n')
  index_lines = index_lines[:table_body_start + 1] + [compiled_problems_table, ] + index_lines[table_body_end:]
  open('index.html', 'w', encoding='utf-8').writelines(index_lines)
  # autoupdate contets table on GitHub Pages:
  os.system('git add . && git commit -m "Recompiled problemset table" && git push')
