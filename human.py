from player import Player
from ai import AI

class Human(Player, AI):
    def __init__(self, name):
        super().__init__(name)

    def gesture_selection(self):
        while self.choice not in self.gesture_list:
            print(self.gesture_list)
            self.choice = input("Please choose one of the above! ")
            print(f"The user has chosen {self.choice}!")

    def game_moves(self):
        while self.score == 0:
            if self.gesture_list == self.choice:
                print(f"Both users have chosen {self.gesture_list}")
            if self.gesture_list == "rock":
                if self.choice == "scissor":
                    print("Rock smashes scissor!")
                    # self.score += 1
                if self.choice == "lizard":
                    print("Rock smashes lizard!")
            if self.gesture_list == "paper":
                if self.choice == "rock":
                    print("Paper covers rock!")
                if self.choice == "spock":
                    print("paper disproves spock!")
            if self.gesture_list == "scissor":
                if self.choice == "paper":
                    print("Scissor cuts paper!")
                if self.choice == "lizard":
                    print("Scissor decapitates lizard!")
            if self.gesture_list == "lizard":
                if self.choice == "spock":
                    print("Lizard poisons spock!")
                if self.choice == "paper":
                    print("Lizard eats paper!")
            if self.gesture_list == "spock":
                if self.choice == "scissor":
                    print("Spock smahses scissor!")
                if self.choice == "rock":
                    print("Spock vaporizes rock!")