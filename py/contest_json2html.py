#!/usr/bin/env python
import json
from problem_tex2html import problem_tex2html


def contest_json2html(contest_id):
  """ supposed to run from /contests directory """
  contest = json.loads(open(f'{contest_id}.json', 'r', encoding='utf-8').read())
  contest_html = f'''
<!DOCTYPE html>
<html>
<head>
  <title>Змагання №{contest['id']} | MathForces</title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="/MathForces/css/index.css">
  <link rel="stylesheet" type="text/css" href="/MathForces/css/contests.css">
  <script type="text/javascript" src="/MathForces/js/countdown.js"></script>
  <script type="text/javascript" src="/MathForces/js/convertDates.js"></script>
  <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML" async></script>
</head>
<body onload="convertDates();">
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
      <li class><a href="/MathForces/">ГОЛОВНА</a></li>
      <li class="current"><a href="/MathForces/contests/">ЗМАГАННЯ</a></li>
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
'''

  k = 0
  for problem_id in contest['p_ids']:
    k += 1
    problem = json.loads(open(f'../problemset/{problem_id}.json', 'r', encoding='utf-8').read())
    contest_html += f'''
      <div class="problem">
        <h1 class="problem_head">Задача №{k} <span style="font-size: smaller;">({problem['id']})</span>: {problem['name']}</h1>
        <p class="problem_body">{problem_tex2html(problem['id'], path="../problemset/")}</p>
        <div class="submit_problem">
          <button class="submit_problem_button" onlick="submit_problem("{problem['id']}");">Отослать!</button>
        </div>
      </div>'''

  contest_html += f'''
    </div>
  </div>
  <br style="height: 3em; clear: both;">
  <footer>MathForces &copy; 2019 <a href="/MathForces/team">наша команда</a></footer>
</body>
</html>'''

  open(f'{contest_id}.html', 'w', encoding='utf-8').write(contest_html)


def contest_json2html_table(contest_id):
  """ supposed to run from /contests directory """
  contest = json.loads(open(f'{contest_id}.json', 'r', encoding='utf-8').read())
  contest_html = f'''
<!DOCTYPE html>
<html>
<head>
  <title>Змагання №{contest['id']} | MathForces</title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="/MathForces/css/index.css">
  <link rel="stylesheet" type="text/css" href="/MathForces/css/contests.css">
  <script type="text/javascript" src="/MathForces/js/countdown.js"></script>
  <script type="text/javascript" src="/MathForces/js/convertDates.js"></script>
  <script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML" async></script>
</head>
<body onload="convertDates();">
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
      <li class><a href="/MathForces/">ГОЛОВНА</a></li>
      <li class="current"><a href="/MathForces/contests/">ЗМАГАННЯ</a></li>
      <li class><a href="/MathForces/gyms/">ТРЕНУВАННЯ</a></li>
      <li class><a href="/MathForces/problemset/">АРХІВ</a></li>
      <li class><a href="/MathForces/groups/">ГРУПИ</a></li>
      <li class><a href="/MathForces/blogs/">БЛОГИ</a></li>
      <li class><a href="/MathForces/team/">КОМАНДА</a></li>
    </ul>
  </nav>
  <br style="height: 3em; clear: both;">
  <div style="position: relative;">
    <div id="sidebar">
      <div class="roundbox sidebox">
        <div class="caption titled">
          → Зверніть увагу
        </div>
        <div style="padding: 0.5em; border-radius: 5px 5px 0 0;">
          <div class="before-contest">
            <span class="contest-state-phase">До змагання</span><br>
            <a href="/MathForces/contests/3">Онлайн олімпіада</a><br>
            <span class="countdown" id="before-contest-countdown"></span>
          </div>
        </div>
      </div>
    </div>
    <div id="pageContent" class="content-with-sidebar">
      <table>
        <thead>
          <th>№</th>
          <th>Назва</th>
          <th></th>
        </thead>
        <tbody>'''

  k = 0
  for problem_id in contest['p_ids']:
    problem = json.loads(open(f'../problemset/{problem_id}.json', 'r', encoding='utf-8').read())
    k += 1
    contest_html += f'''
          <tr style="background-color: {'white' if k & 1 else '#f2f2f2'};">
            <td><a href="../problemset/{problem['id']}">{k}</a> <span style="color: gray; font-size: smaller;">({problem['id']})</span></td>
            <td><a href="../problemset/{problem['id']}">{problem['name']}</a></td>
            <td><button class="submit_problem_button_inline_{'odd' if k & 1 else 'even'}" onlick="submit_problem("{problem['id']}");"></button></td>
          </tr>'''

  k += 1
  contest_html += f'''
          <tr style="background-color: {'white' if k & 1 else '#f2f2f2'};">
            <td></td>
            <td><a href="{contest_id}.html">Всі задачі</a></td>
            <td></td>
          </tr>'''

  contest_html += '''
        </tbody>
      </table
    </div>
  </div>
  <br style="height: 3em; clear: both;">
  <footer>MathForces &copy; 2019 <a href="/MathForces/team">наша команда</a></footer>
</body>
</html>'''
    
  open(f'{contest_id}_t.html', 'w', encoding='utf-8').write(contest_html)
