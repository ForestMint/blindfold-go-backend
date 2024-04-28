


import sys
sys.path.append('./python_classes')

from PoolOfGames import PoolOfGames
my_pool_of_games=PoolOfGames()

from flask import Flask, request
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
    size = request.args.get('size')
    handicap = request.args.get('handicap')
    komi = request.args.get('komi')
    #return str(my_pool_of_games.create_game(size,handicap,komi))
    return {"game_id":my_pool_of_games.create_game(size,handicap,komi)}

if __name__ == "__main__":
    app.run()