from player import Players


class Humans (Players):

    def player_one(self):
        super().__init__()
        self.name= 'Player One'
        self.gesture= gesture_options()
        print(gesture_options)
        while self.score<2:
            print(gesture_options)
        if self.score==2:
            print("Player One Wins the Game!")
        return self.player_one

    def player_two(self):
        super().__init__()
        self.name='Player Two'
        self.gesture= gesture_options()
        print(gesture_options)
        while self.score<2:
            print(gesture_options)
        if self.score==2:
            print("Player Two Wins the Game!")
        return self.player_two
    
       
def gesture_options(self):
        self.gesture_options = ['Choice 0: Rock, Choice 1: Paper, Choice 2: Scissors, Choice 3: Lizard, Choice 4: Spock']
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

        


