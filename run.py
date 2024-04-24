from flask import Flask

from GameManager import GameManager


import sys
sys.path.append('./python_classes')

import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world !"

@app.route('/request_undo')
def index():
    return "Undo granted !"

@app.route('/resign')
def index():
    return "Thanks for the game !"

@app.route('/submit_move')
def index():
    return "Well done !"

if __name__ == "__main__":
    app.run()
