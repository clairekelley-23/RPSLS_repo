from gesture import Gestures 

class Game(Gestures):

    def __init__(self):
        super.__init__()

    def display_welcome(self):
        self.display_welcome = "Welcome to Rock Paper Scissors Lizard Spock!"
    
    def game_rules(self):
        print.self.game_rules = "Each game is the best of three\nUse the number keys to make a selection\n\nScissors cut paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes scissors\nScissors decapitates Lizard\nLizard eats paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock Crushes scissors"

    def player_matches(self):
        super().self.user_input = ''
        
        while True:
            self.user_input == input("How many players? 1 or 2 \n")

            if self.user_input == '1':
                print(self.gesture_options)

