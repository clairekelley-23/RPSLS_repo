import random
from player import Players


class AI (Players):

    def __init__(self):
        super().__init__()
        self.player_two = 'AI'
        while self.score<2:
            print(self.gesture)
            self.chosen_gesture()
        if self.score==2:
            print("AI Wins the Game!")
        return self.player_two


    def chosen_gesture(self):
        self.chosen_gesture = random.choice(self.gesture)
        return (self.chosen_gesture)
        
        


