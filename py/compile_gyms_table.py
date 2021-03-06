#!/usr/bin/env python
import os
import json

LOCAL_CATEGORY_NAMES_UPPERCASE = {
    "a": "Алгебра",
    "c": "Комбінаторика",
    "g": "Геометрія",
    "n": "Теорія чисел",
    "o": "Олімпіади",
    "m": "Різнобій",
    "all": "Всі",
}

LOCAL_DIFFICULTY_NAMES_UPPERCASE = {
    "ve": "Дуже легко",
    "e": "Легко",
    "m": "Середнє",
    "h": "Складно",
    "vh": "Дуже складно",
    "imo": "IMO™",  # this ™ is a trademark symbol
    "all": "Всі",
}


def compile_gyms_table():
    """ supposed to run from /py directory """
    os.chdir('../gyms')
    compiled_gyms_table = ""
    for file in filter(lambda _: os.path.splitext(_)[1] == '.json', os.listdir()):
        gym = json.loads(open(file, 'r', encoding='utf-8').read())
        assert gym['type'] == 'gym'
        compiled_gyms_table += f'''          <tr _cat="{gym['_cat']}" _grade="{gym['_grade']}" _diff="{gym['_diff']}" сlass=\"gymitem\">
            <td class="gym-source">{gym['source']}</td>
            <td class="gym-category">{LOCAL_CATEGORY_NAMES_UPPERCASE[gym['_cat']]}</td>
            <td class="gym-topic">{gym['name']}: 
              <a href="/MathForces/gyms/{gym['pdf_link']}.pdf">[pdf]</a>,
              <a href="/MathForces/gyms/{gym['id']}_t">[web]</a>,
              <span style="color: gray; font-size: smaller;">{gym['_num_probs']}&nbsp;задач{'і' if 2 <= gym['_num_probs'] <= 4 else ''}</span></td>
            <td class="gym-date">{gym['_date']}</td>
            <td class="gym-grade">{gym['_grade']}</td>
            <td class="gym-difficulty">{LOCAL_DIFFICULTY_NAMES_UPPERCASE[gym['_diff']]}</td>
          </tr>
'''
    # update index:
    index_lines = open('index.html', 'r', encoding='utf-8').readlines()
    table_body_start = index_lines.index('        <tbody id="gyms_table_body">\n')
    table_body_end = index_lines.index('        </tbody>\n')
    index_lines = index_lines[:table_body_start + 1] + [compiled_gyms_table, ] + index_lines[table_body_end:]
    open('index.html', 'w', encoding='utf-8').writelines(index_lines)
    os.chdir('../py')


if __name__ == '__main__':
    compile_gyms_table()
    # autoupdate on GitHub Pages:
    os.system('git add . && git commit -m "Recompiled gyms table" && git push')
