from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template('first.html', name=name)
