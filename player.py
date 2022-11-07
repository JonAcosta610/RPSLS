# use inputs to allow player to choose their option
class Player:

    def __init__(self, name):
        self.name = name
        self.choice = None
        self.score = 0
        self.gesture_list = ["rock", "paper", "scissor", "lizard", "spock"]

    def gesture_selection(self):
        pass

    def game_moves(self):
        pass
        
    # def player_choice(self):    
    #     self.player_input = input("Please select your choice! ")
    #     if self.player_input
    #     print(f"The user has chosen {self.player_input}!")