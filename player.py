import random

class Players:

    def __init__(self, name, gesture):
        self.name = name
        self.gesture= self.gesture_options

    def gesture_options(self):
        print(f'Choice 0: Rock', 'Choice 1: Paper', 'Choice 2: Scissors', 'Choice 3: Lizard', 'Choice 4: Spock')
        self.user_input = '' 

        while True:
            user_input = input(f"{self.gesture_options} Choose your gesture.\n")
        
            if user_input == '0':
                print(f'{self.Players.name} chose Rock')
            elif user_input == '1':
                print(f'{self.Players.name} chose Paper')
                break
            elif user_input == '2':
                print(f'{self.Players.name} chose Scissors')
                break
            elif user_input == '3':
                print(f'{self.Players.name} chose Lizard')
                break
            elif user_input == '4':
                print(f'{self.Players.name} chose Spock')
                break
            else:
                print('Type a number 0-4', self.gesture_options)
                continue


 
