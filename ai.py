import random
from player import Players


class AI (Players):

    def get_gesture(self):
        self.chosen_gesture = random.choice(options)
        
        
gestures = {'0': 'Rock', '1': 'Paper', '2': 'Scissors', '3': 'Lizard', '4': 'Spock'}
options = ['0', '1', '2', '3', '4']


