from ai import AI
from human import Human

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_one.gesture_selection()

        self.player_two = AI()
        self.player_two.ai_selection()
   
    def winner(self):
        if self.player_one.score == 2:
            print(f"Congrats {self.player_one.name}! You have beaten {self.player_two.name}!")
        else:
            print(f"Bad Luck! {self.player_two.name} has won! Please play again soon!")

    
    def run_game(self):
        while self.player_one.score < 2 and self.player_two.score < 2:
            if self.player_one.choice == self.player_two.ai_choice:
                print(f"Both players have chosen {self.player_one.choice}!\nTry again!")
            elif self.player_one.choice == "rock":
                if self.player_two.ai_choice == "scissor":
                    print(f"Rock smashes scissor!\nCongrats, {self.player_one.name}! You have won this round!")
                    self.player_one.score += 1
                elif self.player_two.ai_choice == "lizard":
                    print(f"Rock smashes lizard!\nCongrats, {self.player_one.name}! You have won this round!")
                    self.player_one.score += 1
                else:
                    if self.player_two.ai_choice == "paper":
                        print(f"Paper covers rock!\n{self.player_two.name} has won this round!\nTry Again!")
                        self.player_two.score += 1
                    elif self.player_two.ai_choice == "spock":
                        print(f"Spock vaporizes rock!\n{self.player_two.name} has won this round!\nTry Again!")
                        self.player_two.score += 1
            elif self.player_one.choice == "paper":
                if self.player_two.ai_choice == "rock":
                    print(f"Paper covers rock!\nCongrats, {self.player_one.name}! You have won this round!")
                    self.player_one.score += 1
                elif self.player_two.ai_choice == "spock":
                    print(f"Paper disproves spock!\nCongrats, {self.player_one.name}! You have wont this round!")
                    self.player_one.score += 1
                else:
                    if self.player_two.ai_choice == "scissor":
                        print(f"Scissors cuts paper!\n{self.player_two.name} has won this round!\nTry again!")
                        self.player_two.score += 1
                    elif self.player_two.ai_choice == "lizard":
                        print(f"Lizard eats paper!\n{self.player_two.name} has won this round!\nTry again!")
            elif self.player_one.choice == "scissor":
                if self.player_two.ai_choice == "paper":
                    print(f"Scissor cuts paper!\nCongrats, {self.player_one.name}! You have won this round!")
                    self.player_one.score += 1
                elif self.player_two.ai_choice == "lizard":
                    print(f"Scissor decapitates lizard!\nCongrats, {self.player_one.name}! You have won this round!")
                    self.player_one.score += 1
                else:
                    if self.player_two.ai_choice == "rock":
                        print(f"Rock smashes scissors!\n{self.player_two.name} has won this round!\nTry again!")
                        self.player_two.score += 1
                    elif self.player_two.ai_choice == "spock":
                        print(f"Spock smashes scissor!\n{self.player_two.name} has won this round!\nTry again!")
            elif self.player_one.choice == "lizard":
                if self.player_two.ai_choice == "spock":
                    print(f"Lizard poisons spock!\nCongrats, {self.player_one.name}! You have won this round!")
                    self.player_one.score += 1
                elif self.player_two.ai_choice == "paper":
                    print(f"Lizard eats paper!\nCongrats, {self.player_one.name}! You have won this round!")
                    self.player_one.score += 1
                else:
                    if self.player_two.ai_choice == "rock":
                        print(f"Rock smashes lizard!\n{self.player_two.name} has won this round!\nTry again!")
                        self.player_two.score += 1
                    elif self.player_two.ai_choice == "scissor":
                        print(f"Scissor decapitates lizard!\n{self.player_two.name} wins this round!\nTry again!")
                        self.player_two.score += 1
            elif self.player_one.choice == "spock":
                if self.player_two.ai_choice == "scissor":
                    print(f"Spock smashes scissor!\nCongrats {self.player_one.name}! You have won this round!")
                    self.player_one.score += 1
                elif self.player_two.ai_choice == "rock":
                    print(f"Spock vaporizes rock!\nCongrats, {self.player_one.name}! You have won this round!")
                    self.player_one.score += 1
                else:
                    if self.player_two.ai_choice == "lizard":
                        print(f"Lizard poisons spock!\n{self.player_two.name} has won this round!\nTryagain!")
                        self.player_two.score += 1
                    elif self.player_two.ai_choice == "paper":
                        print(f"Paper disproves spock!\n{self.player_two.name} wins this round!\nTry again!")
                        self.player_two.score += 1
            
            if self.player_one.score < 2 and self.player_two.score < 2:
                self.player_one.reset_player_choice()
                self.player_one.gesture_selection()
                self.player_two.ai_selection()

