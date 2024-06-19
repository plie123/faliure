from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Server is running!"

def run():
  app.run(host='127.0.0.1',port=64908)

def server_on():
    t = Thread(target=run)
    t.start()