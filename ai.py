# use an choice randomizer that will allow the AI to choose a random option
# each choice will represent one of the 5 options.
from player import Player

import random


class AI(Player):
    def __init__(self, name):
        super().__init__(name)
        self.ai_score = 0
        pass

    def gesture_selection(self):
        self.ai_choice = random.choice(self.gesture_list)
        print(f"AI has chosen {self.ai_choice}!")
        pass

    def game_moves(self):
        pass

    # def ai_choice(self):
    #     self.computer_choice = random.choice(game_choices)
    #     print(f"\nThe AI has chosen {self.computer_choice}!")
    #     if self.computer_choice == self.player.player_input:
    #         print("fBoth Players selected {self.computer_choice}. It's a tie! Try again!")
    #     elif 

    

