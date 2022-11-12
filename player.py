# use inputs to allow player to choose their option
class Player:

    def __init__(self):
        self.name = ""
        self.choice = None
        self.score = 0
        self.gesture_list = ["rock", "paper", "scissor", "lizard", "spock"]
        # print(f"Hello {self.name}! Welcome to Rock, Paper, Scissor, Lizard, Spock!\nYour opponent today is T-1000!\nGood Luck!")


    def gesture_selection(self):
        pass

    # def game_moves(self):
    #     while self.score < 3:
    #         if self.choice == self.ai_choice.ai_choice:
    #             print(f"Both users have chosen {self.choice}")
    #         elif self.choice == "rock":
    #             if self.ai_choice == "scissor":
    #                 print("Rock smashes scissor!")
    #                 self.score += 1
    #             if self.ai_choice == "lizard":
    #                 print("Rock smashes lizard!")
    #                 self.score += 1
    #             else:
    #                 print("AI has won!")
    #         elif self.choice == "paper":
    #             if self.ai_choice == "rock":
    #                 print("Paper covers rock!")
    #                 self.score += 1
    #             if self.ai_choice == "spock":
    #                 print("paper disproves spock!")
    #                 self.score += 1
    #         elif self.choice == "scissor":
    #             if self.ai_choice == "paper":
    #                 print("Scissor cuts paper!")
    #                 self.score += 1
    #             if self.ai_choice == "lizard":
    #                 print("Scissor decapitates lizard!")
    #                 self.score += 1
    #         elif self.choice == "lizard":
    #             if self.ai_choice == "spock":
    #                 print("Lizard poisons spock!")
    #                 self.score += 1
    #             if self.ai_choice == "paper":
    #                 print("Lizard eats paper!")
    #                 self.score += 1
    #         elif self.choice == "spock":
    #             if self.ai_choice == "scissor":
    #                 print("Spock smahses scissor!")
    #                 self.score += 1
    #             if self.ai_choice == "rock":
    #                 print("Spock vaporizes rock!")
    #                 self.score += 1
        
    # def player_choice(self):    
    #     self.player_input = input("Please select your choice! ")
    #     if self.player_input
    #     print(f"The user has chosen {self.player_input}!")