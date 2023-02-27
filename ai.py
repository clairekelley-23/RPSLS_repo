import random
from player import Players


class AI (Players):

    def __init__(self, name):
        super().__init__()
        self.name = 'AI'
        self.score=0
        while self.score<3:
            print(self.gesture)
            self.chosen_gesture()
        if self.score==3:
            print("AI Wins the Game!")


    def chosen_gesture(self):
        self.chosen_gesture = random.choice(self.gesture)
        return
        
        


