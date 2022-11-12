# use an choice randomizer that will allow the AI to choose a random option
# each choice will represent one of the 5 options.
from player import Player

import random


class AI(Player):
    def __init__(self):
        super().__init__()
        self.name = "T-1000"
        pass

    def ai_selection(self):
        self.ai_choice = random.choice(self.gesture_list)
        print(f"AI has chosen {self.ai_choice}!")
        pass

    def game_moves(self):
        pass

    

