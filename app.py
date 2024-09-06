


import sys
sys.path.append('./python_classes')


from sente import sgf

from PoolOfGameManagers import PoolOfGameManagers
my_pool_of_game_managers=PoolOfGameManagers()

from flask import Flask, request
app = Flask(__name__)

import requests

import json

import string

import logging
logging.basicConfig(filename='./logging/logging.log',level=logging.DEBUG,filemode='a')
logging.info("Running Urban Planning")

import configparser
config = configparser.ConfigParser()
config.read('config.ini')
ply_picking_engine_ip = config['PLY_PICKING_ENGINE']['IP']
ply_picking_engine_port = config['PLY_PICKING_ENGINE']['port']

@app.route('/request_undo')
def undo():
    game_manager_uuid = request.args.get('game_manager_uuid')
    my_pool_of_game_managers.get_game_manager(game_manager_uuid)['game_manager'].undo()
    return "Undo granted !"

@app.route('/resign')
def resign():
    game_manager_uuid = request.args.get('game_manager_uuid')
    my_pool_of_game_managers.get_game_manager(game_manager_uuid)['game_manager'].resign()
    return "Thanks for the game !"

@app.route('/pass')
def pass_turn():
    game_manager_uuid = request.args.get('game_manager_uuid')
    my_pool_of_game_managers.get_game_manager(game_manager_uuid)['game_manager'].pss()
    return "You passed."

@app.route('/play_move')
def play_move():
    game_manager_uuid = request.args.get('game_manager_uuid')
    move = request.args.get('move')

    my_pool_of_game_managers.get_game_manager(game_manager_uuid)['game_manager'].play_move(move)

    return "Well done !"

@app.route('/is_game_over')
def is_game_over():
    game_manager_uuid = request.args.get('game_manager_uuid')

    

    return {"result":my_pool_of_game_managers.get_game_manager(game_manager_uuid)['game_manager'].is_game_over()}

@app.route('/request_ply_from_engine')
def request_ply_from_engine():
    game_manager_uuid = request.args.get('game_manager_uuid')
    game = my_pool_of_game_managers.get_game_manager(game_manager_uuid)['game_manager'].game
    #r = requests.get("https://"+ply_picking_engine_ip+ply_picking_engine_port+"/request_ply", params={"game":game})
    parameters={"game":game}
    #parameters={}
    r = requests.get(url="http://127.0.0.1:5001/request_ply", params=parameters)
    

    my_pool_of_game_managers.get_game_manager(game_manager_uuid)['game_manager'].game.play(r.json()['result'])
    print(my_pool_of_game_managers.get_game_manager(game_manager_uuid)['game_manager'].game)
    sgf.dump(my_pool_of_game_managers.get_game_manager(game_manager_uuid)['game_manager'].game, "./games/my_game.sgf")
    
    return r.json()
    return {"ply":"Q16"}

@app.route('/create_game')
def create_game():
    size = request.args.get('size')
    handicap = request.args.get('handicap')
    komi = request.args.get('komi')
    #return str(my_pool_of_games.create_game(size,handicap,komi))
    return my_pool_of_game_managers.add_new_game_manager(size,handicap,komi)

@app.route('/is_move')
def is_move():
    
    game_manager_uuid = request.args.get('game_manager_uuid')
    
    candidate_speech = request.args.get('candidate_speech')

    
    return my_pool_of_game_managers.get_game_manager(game_manager_uuid)['game_manager'].is_move(candidate_speech)
    
    

if __name__ == "__main__":
    app.run(debug=True)