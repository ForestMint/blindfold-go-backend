from GameManager import GameManager
import uuid

class PoolOfGameManagers():

    def __init__(self):
        self.dict_of_game_managers={}

    def add_new_game_manager(self,size,handicap,komi):
        new_game_manager=GameManager(size,handicap,komi)
        game_manager_uuid=str(uuid.uuid1())
        
        self.dict_of_game_managers[game_manager_uuid]=new_game_manager
        return {"game_manager_uuid":game_manager_uuid}
    
    def get_game_manager(self,game_manager_uuid):
        



        return {"game_manager":self.dict_of_game_managers[game_manager_uuid]}

