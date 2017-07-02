from app import app
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from flask import render_template, redirect, session, url_for, request, g
from flask_login import LoginManager
import os


auth = HTTPBasicAuth()

user = {
    "john": "hello"
}


'''@app.before_request
def before_request():
    g.user = current_user
'''


@app.route('/')
@app.route('/index')
def home():
    return render_template('login.html', title='Home', user=user)


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


if __name__ == "__main__":
    app.run()
