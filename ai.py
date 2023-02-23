import random
from player import Players


class AI (Players):

    def __init__(self, AI_name):
        self.player_three = 'AI'
        super().__init__(AI_name)

    def generate_choice(self):
        self.player_choice
        self.assign_gesture
        super().__init__(self.generate_choice)

    def chosen_gesture(self):
        gameOn=True
        while gameOn:
            self.chosen_gesture = random.choice(self.generate_choice)
        pass
        


