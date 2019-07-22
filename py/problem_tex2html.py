#!/usr/bin/env python
def problem_tex2html(problem_id, path=""):
    """ can run from anywhere given a right path """
    problem_tex = open(f'{path}{problem_id}.tex', 'r', encoding='utf-8').read()
    k, problem_html = 0, ''
    for char in problem_tex:
        if char == '$':
            k += 1
            if k & 1:
                problem_html += '\\('
            else:
                problem_html += '\\)'
        elif char == '\\':
            problem_html += char
        else:
            problem_html += char
    problem_html = problem_html.replace('---', '&mdash;')
    problem_html = problem_html.replace('\\dots', '&hellip;')  # please use \ldots in math mode
    problem_html = problem_html.replace('\\guillemotleft', '&laquo;')
    problem_html = problem_html.replace('\\guillemotright', '&raquo;')
    problem_html = problem_html.replace('\\begin{equation}', '$$')
    problem_html = problem_html.replace('\\end{equation}', '$$')
    problem_html = problem_html.replace('\\smallskip', '<br>')
    problem_html = problem_html.replace('\\medskip', '<br><br>')
    problem_html = problem_html.replace('\\bigskip', '<br><br><br>')
    return problem_html
