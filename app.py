from flask import Flask

from GameManager import GameManager



import sys
sys.path.append('./python_classes')

import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello world !"

@app.route('/request_undo')
def undo():
    return "Undo granted !"

@app.route('/resign')
def resign():
    return "Thanks for the game !"

@app.route('/submit_move')
def submit_move():
    return "Well done !"

@app.route('/create_game')
def create_game():
    return "f08-751"

if __name__ == "__main__":
    app.run()