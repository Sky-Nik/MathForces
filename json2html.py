#!/usr/bin/env python
import json


def p_tex2html(p_id, path=""):
    p_tex = open(f'{path}{p_id}.tex', 'r', encoding='utf-8').read()
    k, p_html = 0, ''
    for c in p_tex:
        if c == '$':
            k += 1
            if k & 1:
                p_html += '\\('
            else:
                p_html += '\\)'
        elif c == '\\':
            p_html += c
        else:
            p_html += c
    p_html = p_html.replace('---', '&mdash;')
    p_html = p_html.replace('\\dots', '&hellip;')  # please use \ldots in mathmode
    p_html = p_html.replace('\\guillemotleft', '&laquo;')
    p_html = p_html.replace('\\guillemotright', '&raquo;')
    p_html = p_html.replace('\\begin{equation}', '$$')
    p_html = p_html.replace('\\end{equation}', '$$')
    p_html = p_html.replace('\\medskip', '<br><br>')
    return p_html


def p_json2html(p_id):
    p = json.loads(open(f'{p_id}.json', 'r', encoding='utf-8').read())
    # assert p_id == p['id']
    open(f'{p_id}.html', 'w', encoding='utf-8').write(f'''
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Задача №{p['id']}: {p['name']} | MathForces</title>
  <!-- <link rel="stylesheet" type="text/css" href="/MathForces/problemset/index.css"> -->
  <link rel="stylesheet" type="text/css" href="index.css">
  <script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML" async></script>
  <!-- <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script> -->
</head>
<body onload="compile_filters();">
  <div class="header">
    <div class="logo">
      <a href="/MathForces/">
        <img src="/MathForces/img/logo-300x65.png">
      </a>
    </div>
    <div class="right">
      <div class="lang-chooser">
        <a href="/MathForces/index_en.html">
          <img src="/MathForces/img/gb.png" title="In English" alt="In English">
        </a>
        <!-- <a href="?locale=ru">
          <img src="ru.png" title="По-русски" alt="По-русски">
        </a> -->
        <a href="index.html">
          <img src="/MathForces/img/ua.png" title="Українською" alt="Українською">
        </a>
      </div>
      <div class="login">
        <a href="/MathForces/enter.html?back=%2f">Увійти</a>&ensp;|&ensp;<a href="/MathForces/register.html">Зареєструватися</a>
      </div>
    </div>
  </div>
  <div class="roundbox menu-box">
    <div class="menu-list-container">
      <ul class="menu-list main-menu-list">
        <li class>
          <a href="/MathForces/">ГОЛОВНА</a>
        </li>
        <li class>
          <a href="/MathForces/contests/">ЗМАГАННЯ</a>
        </li>
        <li class>
          <a href="/MathForces/problems/">ТРЕНУВАННЯ</a>
        </li>
        <li class="current">
          <a href="/MathForces/problemset/">АРХІВ</a>
        </li>
        <li class>
          <a href="/MathForces/groups/">ГРУПИ</a>
        </li>
        <li class>
          <a href="/MathForces/blogs/">БЛОГИ</a>
        </li>
      </ul>
    </div>
  </div>
  <br style="height: 3em; clear: both;">
  <div style="position: relative;">
    <div id="pageContent">
        <div class="ttypography">
            <div class="problem">
                <h1 class="problem_head">Задача №{p['id']}: {p['name']}</h1>
                <p class="problem_body">{p_tex2html(p_id)}</p>
                <div class="submit_problem">
                    <button class="submit_problem_button" onlick="submit_problem('{p_id}');">Отослать!</button>
                </div>
            </div>
        </div>
    </div>
</body>
</html>''')


def c_json2html(c_id):
    c = json.loads(open(f'{c_id}.json', 'r', encoding='utf-8').read())
    c_html = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Соревнование №{c_id}</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="../sty.css">
    <script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML" async>
    </script>
</head>
<body>'''

    k = 0
    for p_id in c['p_ids']:
        k += 1
        p = json.loads(open(f'../problemset/{p_id}.json', 'r', encoding='utf-8').read())
        c_html += f'''
    <div class="problem">
        <h1 class="problem_head">Задача №{k} <span style="font-size: smaller;">({p['id']})</span>: {p['name']}</h1>
        <p class="problem_body">{p_tex2html(p_id, path="../problemset/")}</p>
        <div class="submit_problem">
            <button class="submit_problem_button" onlick="submit_problem('{p_id}');">Отослать!</button>
        </div>
    </div>'''

    c_html += f'''
</body>
</html>'''

    open(f'{c_id}.html', 'w', encoding='utf-8').write(c_html)


def t_json2html(t_id):
    t = json.loads(open(f'{t_id}.json', 'r', encoding='utf-8').read())
    t_html = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Тренировка №{t_id}</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="../sty.css">
    <script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML" async>
    </script>
</head>
<body>'''

    k = 0
    for p_id in t['p_ids']:
        k += 1
        p = json.loads(open(f'../problemset/{p_id}.json', 'r', encoding='utf-8').read())
        t_html += f'''
    <div class="problem">
        <h1 class="problem_head">Задача №{k} <span style="font-size: smaller;">({p['id']})</span>: {p['name']}</h1>
        <p class="problem_body">{p_tex2html(p_id, path="../problemset/")}</p>
        <div class="submit_problem">
            <button class="submit_problem_button" onlick="submit_problem('{p_id}');">Отослать!</button>
        </div>
    </div>'''

    t_html += f'''
</body>
</html>'''

    open(f'{t_id}.html', 'w', encoding='utf-8').write(t_html)


def c_json2html_t(c_id): 
    c = json.loads(open(f'{c_id}.json', 'r', encoding='utf-8').read())
    c_html = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Соревнование №{c_id}: {c['name']}</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="../sty.css">
    <script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML" async>
    </script>
</head>
<body>
    <table>
        <thead>
            <th>№</th>
            <th>Название</th>
            <th></th>
        </thead>
        <tbody>'''

    ps2c_tex(c['p_ids'], c_id)

    k = 0
    for p_id in c['p_ids']:
        p = json.loads(open(f'../problemset/{p_id}.json', 'r', encoding='utf-8').read())
        k += 1
        c_html += f'''
            <tr style="background-color: {'white' if k & 1 else '#f2f2f2'};">
                <td><a href="../problemset/{p['id']}.html">{k}</a> <span style="color: gray; font-size: smaller;">({p['id']})</span></td>
                <td><a href="../problemset/{p['id']}.html">{p['name']}</a></td>
                <td><button class="submit_problem_button_inline_{'odd' if k & 1 else 'even'}" onlick="submit_problem('{p_id}');"></button></td>
            </tr>'''

    k += 1
    c_html += f'''<tr style="background-color: {'white' if k & 1 else '#f2f2f2'};">
        <td></td>
        <td><a href="{c_id}.html">Все задачи</a></td>
        <td></td>
    </tr>'''

    c_html += '''
        </tbody>
    </table
</body>
</html>'''
    
    open(f'{c_id}_t.html', 'w', encoding='utf-8').write(c_html)


def t_json2html_t(t_id): 
    t = json.loads(open(f'{t_id}.json', 'r', encoding='utf-8').read())
    t_html = f'''
<!DOCTYPE html>
<html>
<head>
    <title>Тренировка №{t_id}: {t['name']}</title>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="../sty.css">
    <script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML" async>
    </script>
</head>
<body>
    <table>
        <thead>
            <th>№</th>
            <th>Название</th>
            <th></th>
        </thead>
        <tbody>'''

    ps2t_tex(t['p_ids'], t_id)

    k = 0
    for p_id in t['p_ids']:
        p = json.loads(open(f'../problemset/{p_id}.json', 'r', encoding='utf-8').read())
        k += 1
        t_html += f'''
            <tr style="background-color: {'white' if k & 1 else '#f2f2f2'};">
                <td><a href="../problemset/{p['id']}.html">{k}</a> <span style="color: gray; font-size: smaller;">({p['id']})</span></td>
                <td><a href="../problemset/{p['id']}.html">{p['name']}</a></td>
                <td><button class="submit_problem_button_inline_{'odd' if k & 1 else 'even'}" onlick="submit_problem('{p_id}');"></button></td>
            </tr>'''

    k += 1
    t_html += f'''<tr style="background-color: {'white' if k & 1 else '#f2f2f2'};">
        <td></td>
        <td><a href="{t_id}.html">Все задачи</a></td>
        <td></td>
    </tr>'''

    t_html += '''
        </tbody>
    </table
</body>
</html>'''
    
    open(f'{t_id}_t.html', 'w', encoding='utf-8').write(t_html)


def ps2c_tex(p_ids, c_id):
    c = json.loads(open(f'{c_id}.json', 'r', encoding='utf-8').read())
    c_tex = '\\input{c.sty}\n\n\\begin{document}\n\n\\title{Соревнование ' + f"№{c_id}: {c['name']}" + '}\n\\maketitle\n\n'

    for p_id in p_ids:
        p = json.loads(open(f'../problemset/{p_id}.json', 'r', encoding='utf-8').read())
        c_tex += '\\begin{problem}' + f"[{p['name']}]" + '\n\t' + open(f'../problemset/{p_id}.tex', 'r', encoding='utf-8').read()+ '\n\\end{problem}\n\n'

    c_tex += '\\end{document}'
    open(f'{c_id}.tex', 'w', encoding='utf-8').write(c_tex)


def ps2t_tex(p_ids, t_id):
    t = json.loads(open(f'{t_id}.json', 'r', encoding='utf-8').read())
    t_tex = '\\input{t.sty}\n\n\\begin{document}\n\n\\title{Тренировка ' + f"№{t_id}: {t['name']}" + '}\n\\maketitle\n\n'

    for p_id in p_ids:
        p = json.loads(open(f'../problemset/{p_id}.json', 'r', encoding='utf-8').read())
        t_tex += '\\begin{problem}' + f"[{p['name']}]" + '\n\t' + open(f'../problemset/{p_id}.tex', 'r', encoding='utf-8').read()+ '\n\\end{problem}\n\n'

    t_tex += '\\end{document}'
    open(f'{t_id}.tex', 'w', encoding='utf-8').write(t_tex)


def all_p_json2html():
    import os
    os.chdir('problemset')
    for p_id in map(lambda _: _[:-5], filter(lambda _: _[-5:] == '.json', os.listdir())):
        p_json2html(p_id)
    os.chdir('..')


def all_c_json2html():
    import os
    os.chdir('contests')
    for c_id in map(lambda _: _[:-5], filter(lambda _: _[-5:] == '.json', os.listdir())):
        c_json2html(c_id)
        c_json2html_t(c_id)
    os.chdir('..')


def all_t_json2html():
    import os
    os.chdir('gyms')
    for t_id in map(lambda _: _[:-5], filter(lambda _: _[-5:] == '.json', os.listdir())):
        t_json2html(t_id)
        t_json2html_t(t_id)
    os.chdir('..')


if __name__ == "__main__":
    all_p_json2html()
    all_c_json2html()
    all_t_json2html()
