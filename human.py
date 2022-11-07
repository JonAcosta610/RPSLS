from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def gesture_selection(self):
        while self.choice not in self.gesture_list:
            print(self.gesture_list)
            self.choice = input("Please choose one of the above! ")
            print(f"The user has chosen {self.choice}!")