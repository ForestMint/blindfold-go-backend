import sente

import string

from sente import sgf

class GameManager():
    def __init__(self,size,handicap,komi):
        #self.game=sente.Game(size, sente.rules.JAPANESE)
        self.size = int(size)
        self.game= sente.Game()
        self.blindfolded_player_is_black=True

    def is_blindfolded_player_black(self):
        return self.blindfolded_player_is_black
    
    def is_game_over(self):
        return False
    
    def pss(self):
        self.game.pss()
        print(self.game)
        sgf.dump(self.game, "./games/my_game.sgf")

    def undo(self):
        self.game.step_up()
        print(self.game)
        sgf.dump(self.game, "./games/my_game.sgf")

    def resign(self):
        self.game.resign()
        print(self.game)
        sgf.dump(self.game, "./games/my_game.sgf")
    
    def is_move(self,candidate_speech):

        list_of_abscissae=list(string.ascii_uppercase)
        list_of_abscissae.remove("I")
        list_of_abscissae=list_of_abscissae[0:self.size]
        list_of_ordinates=range(1,self.size+1)
        list_of_existing_moves=[]
        for abscissa in list_of_abscissae:
            for ordinate in list_of_ordinates:
                list_of_existing_moves.append(abscissa+str(ordinate))
        list_of_existing_moves.append("PASS")
        list_of_existing_moves.append("RESIGN")
        list_of_existing_moves.append("UNDO")


        return {"result":candidate_speech.upper() in list_of_existing_moves}
    

        
    def is_game_over(self):
        return self.game.is_over()

    def play_move(self, move):
        

        part_1=move[:1].upper()

        print(part_1)
        part_2=move[1:]

        abscissa = "ABCDEFGHJKLMNOPQRST".index(part_1)+1
        ordinate = int(part_2)

        self.game.play(abscissa, ordinate)

        print(self.game)
        sgf.dump(self.game, "./games/my_game.sgf")

