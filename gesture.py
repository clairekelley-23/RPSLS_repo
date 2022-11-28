
class Gestures:

    def __init__(self):
        self.gesture_options = ['Choice 0: Rock', 'Choice 1: Paper', 'Choice 2: Scissors', 'Choice 3: Lizard', 'Choice 4: Spock']
    
    def assign_gesture(self):
        
        self.user_input = ''
        
        while True:
            user_input = input(f"{self.gesture_options} Choose your gesture.\n")
        
            if user_input == '0':
                print(f'{} chose Rock')
            elif user_input == '1':
                print(f'{} chose Paper')
                break
            elif user_input == '2':
                print(f'{} chose Scissors')
                break
            elif user_input == '3':
                print(f'{} chose Lizard')
                break
            elif user_input == '4':
                print(f'{} chose Spock')
                break
            else:
                print('Type a number 0-4', self.gesture_options)
                continue