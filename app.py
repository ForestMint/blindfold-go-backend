


import sys
sys.path.append('./python_classes')

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
    return "Thanks for the game !"

@app.route('/play_move')
def play_move():
    game_manager_uuid = request.args.get('game_manager_uuid')
    move = request.args.get('move')

    my_pool_of_game_managers.get_game_manager(game_manager_uuid)['game_manager'].play_move(move)

    return "Well done !"

'''
@app.route('/submit_move')
def submit_move():
    return "Well done !"
'''

@app.route('/request_ply_from_engine')
def request_ply_from_engine():
    game_uuid = request.args.get('game_uuid')
    game = my_pool_of_game_managers.get_game(game_uuid)
    r = requests.get("https://"+ply_picking_engine_ip+ply_picking_engine_port)

    return r.json()["ply"]
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
    

    '''
    logging.info(candidate_speech)

    try:

        list_of_abscissae=list(string.ascii_uppercase)
        list_of_abscissae.remove("I")
        abscissa=list_of_abscissae.index(candidate_speech.upper()[:1])+1
        ordinate=int(candidate_speech[1:])
        
        print('This is error output')
        print('This is error output', file=sys.stderr)
        print('This is standard output', file=sys.stdout)

        logging.info('coordinates :'+str({"abscissa":abscissa, "ordinate":ordinate}))
        #print({"abscissa":abscissa, "ordinate":ordinate})
        my_pool_of_game_managers.get_game_manager(game_id).game.play(abscissa,ordinate)
        my_pool_of_game_managers.get_game_manager(game_id).game.step_up()
        #print(my_pool_of_game_managers.get_game_manager(game_id))
        return {"result":True}
    except:
        #print(my_pool_of_game_managers.get_game(game_id))
        return {"result":False}

    '''
    

if __name__ == "__main__":
    app.run(debug=True)