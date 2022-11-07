import random

list_choice = ["rock", "paper", "scissor"]

class player:
    
    def __init__(self):
        self.choice = "None"
        self.score = 0

    def get_input(self, choice, run):
        z = 0
        for x in range(3):
            if choice == self.list_choice[x]:
                z = 1
        if z == 0:
            print("wrong input")
            run = False
            return run
        if z == 1:
            print("input accepted")
            self.choice = choice
            return run
    
    def return_choice(self):
        return self.choice
    
    def check(self, computer, choice):
        pass
    
    def return_score(self):
        return self.score
