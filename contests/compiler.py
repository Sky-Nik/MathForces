#!/usr/bin/env python
import os
import json

if __name__ == '__main__':
  compiled_contests_table = ""
  for file in filter(lambda _: os.path.splitext(_)[1] == '.json', os.listdir()):
    contest = json.loads(open(file, 'r', encoding='utf-8').read())
    assert contest['type'] == 'contest'
    compiled_contests_table += f'''
              <tr contest-id="{contest['id']}">
                <td class="contest-number-column"><a href="/MathForces/contests/{contest['id']}_t.html">{contest['id']}</a></td>
                <td class="contest-name-column"><a href="/MathForces/contests/{contest['id']}_t.html">{contest['name']}</a></td>
                <td class="contest-start-time-column">{contest['start_time'].replace(', ', '<br>')}</td>
                <td class="contest-duration-column">{contest['duration'].zfill(5)}</td>
              </tr>'''
  open('compiled_contests_table.html', 'w', encoding='utf-8').write(compiled_contests_table)
