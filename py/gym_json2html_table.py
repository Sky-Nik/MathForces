#!/usr/bin/env python
import json


def gym_json2html_table(gym_id): 
  """ supposed to run from /gyms directory """
  gym = json.loads(open(f'{gym_id}.json', 'r', encoding='utf-8').read())
  gym_html = f'''
<!DOCTYPE html>
<html>
<head>
  <title>Тренування №{gym['id']} | MathForces</title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="/MathForces/css/index.css">
  <link rel="stylesheet" type="text/css" href="/MathForces/css/gyms.css">
  <script type="text/javascript" src="/MathForces/js/countdown.js"></script>
  <script type="text/javascript" src="/MathForces/js/convertDates.js"></script>
  <script type="text/javascript" src="/MathForces/js/dumsFilter.js"></script>
  <script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML" async></script>
</head>
<body onload="convertDates();compile_filters();">
  <header>
    <div class="logo"><a href="/MathForces/"><img src="/MathForces/img/logo-300x65.png"></a></div>
    <div class="right">
      <div class="lang-chooser">
        <a href="/index_en.html"><img src="/MathForces/img/gb.png" title="In English" alt="In English"></a>
        <!-- <a href="?locale=ru"><img src="ru.png" title="По-русски" alt="По-русски"></a> -->
        <a href="index.html"><img src="/MathForces/img/ua.png" title="Українською" alt="Українською"></a>
      </div>
      <div class="login">
        <a href="/MathForces/enter.html?back=%2f">Увійти</a>&ensp;|&ensp;<a href="/MathForces/register.html">Зареєструватися</a>
      </div>
    </div>
  </header>
  <nav class="roundbox">
    <ul class="menu-list main-menu-list">
      <li class="current"><a href="/MathForces/">ГОЛОВНА</a></li>
      <li class><a href="/MathForces/contests/">ЗМАГАННЯ</a></li>
      <li class><a href="/MathForces/gyms/">ТРЕНУВАННЯ</a></li>
      <li class><a href="/MathForces/problemset/">АРХІВ</a></li>
      <li class><a href="/MathForces/groups/">ГРУПИ</a></li>
      <li class><a href="/MathForces/blogs/">БЛОГИ</a></li>
      <li class><a href="/MathForces/team/">КОМАНДА</a></li>
    </ul>
  </nav>
  <br style="height: 3em; clear: both;">
  <div style="position: relative;">
    <div id="pageContent">
      <table>
        <thead>
          <th>№</th>
          <th>Название</th>
          <th></th>
        </thead>
        <tbody>'''

  k = 0
  for problem_id in gym['p_ids']:
    problem = json.loads(open(f'../problemset/{problem_id}.json', 'r', encoding='utf-8').read())
    k += 1
    gym_html += f'''
          <tr style="background-color: {'white' if k & 1 else '#f2f2f2'};">
            <td><a href="../problemset/{problem['id']}">{k}</a> <span style="color: gray; font-size: smaller;">({problem['id']})</span></td>
            <td><a href="../problemset/{problem['id']}">{problem['name']}</a></td>
            <td><button class="submit_problem_button_inline_{'odd' if k & 1 else 'even'}" onlick="submit_problem('{problem["id"]}');"></button></td>
          </tr>'''

  k += 1
  gym_html += f'''
          <tr style="background-color: {'white' if k & 1 else '#f2f2f2'};">
            <td></td>
            <td><a href="{gym_id}.html">Всі задачі</a></td>
            <td></td>
          </tr>'''

  gym_html += '''
        </tbody>
      </table
    </div>
  </div>
</body>
</html>'''
    
  open(f'{gym_id}_t.html', 'w', encoding='utf-8').write(gym_html)
