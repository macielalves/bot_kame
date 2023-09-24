from threading import Thread

from flask import Flask

from page_config import html

app = Flask('Bot Kame')


@app.route('/')
def home():
  return html()


def run():
  app.run(host='0.0.0.0', port=7045)


def keep_alive():
  thred = Thread(target=run)
  thred.start()
