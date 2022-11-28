from gesture import Gestures
import random

class Players(Gestures):

    def __init__(self, name):
        super().__init__()
        self.player_one =  name
        self.player_two = name
        self.player_three = name

    def player_choice(self):
        print("How many players? 1 or 2\n")
        self.user_input = " "

        while True:
            if self.user_input == '1':
                print(self.player_one, "vs", self.player_three)
                print(f'{self.player_one}\n{self.gesture_options}\n{self.assign_gesture}')
                print(f'{self.player_three}\n{self.gesture_options}\n{random.choice(self.assign_gesture)}')   
            elif self.user_input -- '2':
                print(self.player_one, "vs", self.player_two)
                print(f'{self.player_one}\n{self.gesture_options}\n{self.assign_gesture}')
                print(f'{self.player_two}\n{self.gesture_options}\n{self.assign_gesture}')
            else:
                continue

            super().__init__(self.player_choice)