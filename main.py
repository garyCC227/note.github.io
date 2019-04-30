from server import app
from flask import render_template


@app.route('/')
def login():
    return render_template('Login.html')
