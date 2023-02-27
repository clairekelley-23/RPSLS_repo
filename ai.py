import random
from player import Players


class AI (Players):

    def __init__(self, name):
        self.name = 'AI'
        super().__init__()


    def chosen_gesture(self):
        self.chosen_gesture = random.choice(self.gesture)
        return
        
        


