#!/usr/bin/env python
import os
import json


LOCAL_CATEGORY_NAMES_UPPERCASE = {
  "a":   "Алгебра",
  "c":   "Комбінаторика",
  "g":   "Геометрія",
  "n":   "Теорія чисел",
  "o":   "Олімпіади",
  "m":   "Різнобій",
  "all": "Всі",
}

LOCAL_DIFFICULTY_NAMES_UPPERCASE = {
  "ve":  "Дуже легко",
  "e":   "Легко",
  "m":   "Середнє",
  "h":   "Складно",
  "vh":  "Дуже складно",
  "imo": "IMO™",  # this ™ is a trademark symbol
  "all": "Всі",
}


if __name__ == '__main__':
  compiled_gyms_table = ""
  for file in filter(lambda _: os.path.splitext(_)[1] == '.json', os.listdir()):
    gym = json.loads(open(file, 'r', encoding='utf-8').read())
    assert gym['type'] == 'gym'
    compiled_gyms_table += f'''
              <tr сlass="gym_item" _cat="{gym['_cat']}" _grade="{gym['_grade']}" _diff="{gym['_diff']}" gym-id="{gym['id']}">
                <td class="gym-source">{gym['source']}</td>
                <td class="gym-category">{LOCAL_CATEGORY_NAMES_UPPERCASE[gym['_cat']]}</td>
                <td class="gym-topic">{gym['name']}: 
                  <a href="/MathForces/gyms/{gym['pdf_link']}.pdf">[pdf]</a>,
                  <a href="v/MathForces/gyms/{gym['id']}_t">[web]</a>,
                  <span style="color: gray; font-size: smaller;">{gym['_num_probs']}&nbsp;задач{'і' if 2 <= gym['_num_probs'] <= 4 else ''}</span></td>
                <td class="gym-date">{gym['_date']}</td>
                <td class="gym-grade">{gym['_grade']}</td>
                <td clas="gym-difficulty">{LOCAL_DIFFICULTY_NAMES_UPPERCASE[gym['_diff']]}</td>
              </tr>'''
  open('compiled_gyms_table.html', 'w', encoding='utf-8').write(compiled_gyms_table)
  # autoupdate contets table on GitHub Pages:
  os.system('git add . && git commit -m "Recompiled gyms table" && git push')
