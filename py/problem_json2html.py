#!/usr/bin/env python
import json

from py.problem_tex2html import problem_tex2html


def problem_json2html(problem_id):
    """ supposed to run from /problemset directory """
    problem = json.loads(open(f'{problem_id}.json', 'r', encoding='utf-8').read())
    assert problem['type'] == 'problem'
    open(f"{problem['id']}.html", 'w', encoding='utf-8').write(f'''
<!DOCTYPE html>
<html>
<head>
  <title>Задача №{problem['id']}: {problem['name']} | MathForces</title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="/MathForces/css/index.css">
  <link rel="stylesheet" type="text/css" href="/MathForces/css/problemset.css">
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
      <li class><a href="/MathForces/contests/">ЗМАГАННЯ</a></li>
      <li class><a href="/MathForces/gyms/">ТРЕНУВАННЯ</a></li>
      <li class="current"><a href="/MathForces/problemset/">АРХІВ</a></li>
      <li class><a href="/MathForces/groups/">ГРУПИ</a></li>
      <li class><a href="/MathForces/blogs/">БЛОГИ</a></li>
      <li class><a href="/MathForces/team/">КОМАНДА</a></li>
    </ul>
  </nav>
  <br style="height: 3em; clear: both;">
  <div style="position: relative;">
    <div id="pageContent">
      <div class="ttypography">
        <div class="problem">
          <h1 class="problem_head">Задача №{problem['id']}: {problem['name']}</h1>
          <p class="problem_body">{problem_tex2html(problem['id'])}</p>
          <div class="submit_problem">
            <button class="submit_problem_button" onlick="submit_problem('{problem["id"]}');">Отослать!</button>
          </div>
        </div>
      </div>
    </div>
  <br style="height: 3em; clear: both;">
  <footer>MathForces &copy; 2019 <a href="/MathForces/team">наша команда</a></footer>
</body>
</html>''')
