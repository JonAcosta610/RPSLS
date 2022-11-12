from player import Player
import random

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input("Please enter your name here: ")
        print(f"Hello {self.name}! Welcome to Rock, Paper, Scissor, Lizard, Spock!\nYour opponent today is T-1000!\nTwo out of three wins!\nGood Luck!")


    def gesture_selection(self):
        while self.choice not in self.gesture_list:
            print(self.gesture_list)
            self.choice = input("Please choose one of the above! ")
            print(f"The user has chosen {self.choice}!")

    def ai_selection(self):
        self.ai_choice = random.choice(self.gesture_list)
        print(f"AI has chosen {self.ai_choice}!")
