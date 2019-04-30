from flask import Flask, session
from flask_login import LoginManager

app = Flask(__name__)
static_folder = 'static'
app.config['SECRECT_KEP'] = 'Strong'
app.secret_key = 'any random string'
