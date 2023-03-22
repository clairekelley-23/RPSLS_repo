import random

class Players:

    def __init__(self, name):
        self.name=name
        self.chosen_gesture = None
        self.score=0
    
 
    def choose_move(self):
        while True:
            move_input = input("Enter your move (0 for Rock, 1 for Paper, 2 for Scissors, 3 for Lizard, 4 for Spock): ")
            if move_input in gestures:
                self.move = gestures[move_input]
                break
            else:
                print("Invalid input. Please try again.")

    def add_point(self):
        self.score += 1


gestures = {'0': 'Rock', '1': 'Paper', '2': 'Scissors', '3': 'Lizard', '4': 'Spock'}

options = ['0', '1', '2', '3', '4']
    
gestures['0'].add_beats(gestures['2'])
gestures['0'].add_beats(gestures['l'])
gestures['1'].add_beats(gestures['0'])
gestures['1'].add_beats(gestures['4'])
gestures['2'].add_beats(gestures['1'])
gestures['2'].add_beats(gestures['l'])
gestures['3'].add_beats(gestures['1'])
gestures['3'].add_beats(gestures['4'])
gestures['4'].add_beats(gestures['0'])
gestures['4'].add_beats(gestures['2'])




 
