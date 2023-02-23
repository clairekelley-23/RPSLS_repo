from player import Players


class Humans (Players):

    def __init__(self, name):
        super().__init__(name)
    

    def __init__(self, name):
        super().__init__(self.name)
        self.name = 'Player one',
        self.name = 'Player two'  

    def gesture_options(self):
        self.gesture_options = ['Choice 0: Rock', 'Choice 1: Paper', 'Choice 2: Scissors', 'Choice 3: Lizard', 'Choice 4: Spock']
       
        

        

Player_one = Humans('Player One', Players.gesture_options)
Player_two = Humans('Player Two', Players.gesture_options)

