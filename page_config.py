def css():
  css = open('includes/styles.css', 'r', encoding='utf-8')
  return css.read().replace('\n', '').replace(' ', '')


body = open('includes/body.html', 'r', encoding='utf-8').read()

scripts = open('includes/scripts.js', 'r', encoding='utf-8').read()


def html():
  html = open('index.html', 'r', encoding='utf-8')
  return html.read().format(css(), body, scripts)
