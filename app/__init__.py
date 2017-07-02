from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)


from app import views
