from flask import Flask, render_template

from devices import devices

app = Flask(__name__)


@app.route('/')
def devices():
  return render_template('main.html', devices=devices)


if __name__ == '__main__':
  app.run()
