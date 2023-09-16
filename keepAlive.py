from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
  return 'alive: true'


def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  thred = Thread(target=run)
  thred.start()