### INF601 - Advanced Programming in Python
### Samuel Ayers
### Mini Project 3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'