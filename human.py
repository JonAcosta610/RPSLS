from player import Player
import random

class Human(Player):
    def __init__(self):
        super().__init__()
        self.name = input("Please enter your name here: ")
        print(f"Hello {self.name}! Welcome to Rock, Paper, Scissor, Lizard, Spock!\nYour opponent today is T-1000!\nGood Luck!")


    def gesture_selection(self):
        while self.choice not in self.gesture_list:
            print(self.gesture_list)
            self.choice = input("Please choose one of the above! ")
            print(f"The user has chosen {self.choice}!")

    def ai_selection(self):
        self.ai_choice = random.choice(self.gesture_list)
        print(f"AI has chosen {self.ai_choice}!")

    def game_moves(self):
        while self.score < 3:
            if self.choice == self.ai_choice.ai_choice:
                print(f"Both users have chosen {self.choice}")
            elif self.choice == "rock":
                if self.ai_choice == "scissor":
                    print("Rock smashes scissor!")
                    self.score += 1
                if self.ai_choice == "lizard":
                    print("Rock smashes lizard!")
                    self.score += 1
                else:
                    print("AI has won!")
            elif self.choice == "paper":
                if self.ai_choice == "rock":
                    print("Paper covers rock!")
                    self.score += 1
                if self.ai_choice == "spock":
                    print("paper disproves spock!")
                    self.score += 1
            elif self.choice == "scissor":
                if self.ai_choice == "paper":
                    print("Scissor cuts paper!")
                    self.score += 1
                if self.ai_choice == "lizard":
                    print("Scissor decapitates lizard!")
                    self.score += 1
            elif self.choice == "lizard":
                if self.ai_choice == "spock":
                    print("Lizard poisons spock!")
                    self.score += 1
                if self.ai_choice == "paper":
                    print("Lizard eats paper!")
                    self.score += 1
            elif self.choice == "spock":
                if self.ai_choice == "scissor":
                    print("Spock smahses scissor!")
                    self.score += 1
                if self.ai_choice == "rock":
                    print("Spock vaporizes rock!")
                    self.score += 1
