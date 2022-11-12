from ai import AI
from human import Human
from player import Player

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_one.gesture_selection()

        self.player_two = AI()
        self.player_two.ai_selection()

    def game_moves(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            if self.player_one.choice == self.player_two.choice:
                print(f"Both users have chosen {self.player_one.choice}!\nTry again!")
            elif self.player_one.choice == "rock":
                if self.player_two.choice == "scissor":
                    print(f"Rock smashes scissor!ç")
                    self.player_one.score += 1
                if self.player_two.choice == "lizard":
                    print(f"Rock smashes lizard!\nCongrats, {self.player_one.name}! You have won this round!")
                    self.player_one.score += 1
                else:
                    if self.player_two.choice == "paper":
                        print(f"{self.player_two.choice} covers {self.player_one.choice}!\nThe AI has won this round!\nTry Again!")
                        self.player_two.score += 1
                    if self.player_two.choice == "spock":
                        print(f"{self.player_two.choice} vaporizes {self.player_one.choice}!\nThe AI has won this round!\nTry Again!")
                        self.player_two.score += 1
            elif self.player_one.choice == "paper":
                if self.player_two.choice == "rock":
                    print(f"Paper covers rock!\nCongrats, {self.player_one.name}! You have won this round!")
                    self.player_one.score += 1
                if self.player_one.choice == "spock":
                    print(f"Paper disproves spock!\nCongrats, {self.player_one.name}! You have wont this round!")
                    self.player_one.score += 1
                else:
                    if self.player_two.choice == "scissor":
                        print(f"{self.player_two.choice} cuts {self.player_one.choice}!\nThe AI has won this round!\nTry again!")
                        self.player_two.score += 1
            elif self.choice == "scissor":
                if self.ai_choice == "paper":
                    print(f"Scissor cuts paper!")
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
