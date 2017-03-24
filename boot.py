from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap
from flask_wtf import Form

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'

@app.route('/')
def index():
    return render_template('index.html', title="Index")


if __name__ == '__main__':
    app.run(debug=True, port=9527)
