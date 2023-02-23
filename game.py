import random
from ai import AI
from human import Humans

class Game(AI, Humans):

    def __init__(self):
        super.__init__()

    def display_welcome(self):
        self.display_welcome = "Welcome to Rock Paper Scissors Lizard Spock!"
    
    def game_rules(self):
        self.game_rules = "Each game is the best of three\nUse the number keys to make a selection\n\nScissors cut paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes scissors\nScissors decapitates Lizard\nLizard eats paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock Crushes scissors"

    def game_play(self):
        print(self.display_welcome)
        print(self.game_rules)
        print(self.player_choice, self.assign_gesture)
        
    
    def player_choice(self):
        print("How many players? 1 or 2\n")
        self.user_input = " "

        while True:
            if self.user_input == '1':
                print(self.player_one, "vs", self.player_three)
                print(f'{self.player_one}\n{self.gesture_options}\n{self.assign_gesture}')
                print(f'{self.player_three}\n{self.gesture_options}\n{random.choice(self.assign_gesture)}')   
            elif self.user_input == '2':
                print(self.player_one, "vs", self.player_two)
                print(f'{self.player_one}\n{self.gesture_options}\n{self.assign_gesture}')
                print(f'{self.player_two}\n{self.gesture_options}\n{self.assign_gesture}')
            else:
                continue
    
    def assign_gesture(self):        
        self = '' 

        while True:
            user_input = input(f"{self.gesture_options} Choose your gesture.\n")
        
            if user_input == '0':
                print(f'{self.Players_name} chose Rock')
            elif user_input == '1':
                print(f'{self.Players_name} chose Paper')
                break
            elif user_input == '2':
                print(f'{self.Players_name} chose Scissors')
                break
            elif user_input == '3':
                print(f'{self.Players_name} chose Lizard')
                break
            elif user_input == '4':
                print(f'{self.Players_name} chose Spock')
                break
            else:
                print('Type a number 0-4', self.gesture_options)
                continue
        


