#!/usr/bin/env python
import os.path
import json


def tex2html(from_filename: str, to_filename: str) -> None:
    reader = open(f'{from_filename}.tex', 'r', encoding='utf-8')
    contents = reader.read()
    k, response = 0, ''
    for char in contents:
        if char == '$':
            k += 1
            if k & 1:
                response += '\\('
            else:
                response += '\\)'
        elif char == '\\':
            response += char
        else:
            response += char
    response = response.replace('---', '&mdash;')
    response = response.replace('--', '&ndash;')
    writer = open(f'{to_filename}.html', 'w', encoding='utf-8')
    writer.write(response)


def json2html(from_filename: str, to_filename: str) -> None:
    reader = open(f'{from_filename}.json', 'r', encoding='utf-8')
    contents = json.loads(reader.read())
    if contents['type'] == 'problem':
        p = contents
        writer = open(f'{to_filename}.html', 'w', encoding='utf-8')
        writer.write(DEFAULT_HTML_HEAD_PRE_TITLE)
        writer.write(f"\t<title>Задача №{p['id']}: {p['name']}</title>")
        writer.write(DEFAULT_HTML_HEAD_POST_TITLE)
        writer.write(DEFAULT_HTML_BODY_PRE_PROBLEM)
        writer.write(f"\t\t<h1 class=\"problem_head\">Задача №{p['id']}: {p['name']}</h1>\n")
        tex2html(from_filename, f'{to_filename}_s')
        tex2html_response_reader = open(f'{to_filename}_s.html', 'r', encoding='utf-8')
        writer.write(f"\t\t<p class=\"problem_body\">\n\t\t\t{tex2html_response_reader.read()}\n\t\t</p>\n")
        writer.write(f"\t\t<div class=\"submit_problem\">\n\t\t\t<button class=\"submit_problem_button\" onlick=\"submit_problem({p['id']});\">Отослать!</button>\n\t\t</div>")
        writer.write(DEFAULT_HTML_BODY_POST_PROBLEM)


def convert(from_path: str, to_path: str) -> None:
    from_filename, from_extension = os.path.splitext(from_path)
    to_filename, to_extension = os.path.splitext(to_path)
    assert from_filename == to_filename
    assert from_extension != to_extension
    converters[from_extension][to_extension](from_filename, to_filename)


converters = {
    '.json': {
        '.html': json2html,
        # '.tex': json2tex,
    },
    # '.html': {
    #     '.json': html2json,
    #     '.tex': html2tex,
    # },
    # '.tex':  {
    #     '.html': tex2html,
    #     '.json': tex2json,
    # },
}


DEFAULT_HTML_HEAD_PRE_TITLE = '''
<!DOCTYPE html>
<html>
<head>
'''

DEFAULT_HTML_HEAD_POST_TITLE = '''
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="../sty.css">
    <script type="text/javascript" async
    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML" async>
    </script>
</head>
'''

DEFAULT_HTML_BODY_PRE_PROBLEM = '''
<body>
    <div class="problem">
'''

DEFAULT_HTML_BODY_POST_PROBLEM = '''
    </div>
</body>
</html>
'''


if __name__ == '__main__':
    convert('p/1.json', 'p/1.html')
