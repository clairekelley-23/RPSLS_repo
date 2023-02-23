from player import Players


class Humans (Players):

    def __init__(self, name, gesture):
        super().__init__(name, gesture)
    

    def player_one(self, gesture):
        super().__init__(name, gesture)
        self.name= 'Player One'
        self.gesture= input(gesture)

    # def __init__(self, name):
    #     super().__init__(self, name)
    #     self.name = 'Player one'
    #     self.name = 'Player two' 

    def chosen_gesture(self):
        pass
       
        

        

Player_one = Humans('Player One', Players.gesture_options)
Player_two = Humans('Player Two', Players.gesture_options)

