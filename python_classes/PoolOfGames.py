from GameManager import GameManager
import uuid

class PoolOfGames():

    def __init__(self):
        self.dict_of_games={}

    def create_game(self,size,handicap,komi):
        new_game=GameManager(size,handicap,komi)
        game_uuid=uuid.uuid1()
        self.dict_of_games[uuid]=game_uuid
        return game_uuid

