import random
from ai import AI
from human import Humans

class Game():
    def __init__(self):
        self.player_one = Humans()
        self.player_two = None

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
                    self.player_two = AI()
                    # self.player_one.chose_gesture()
                    # self.player_one.chosen_gesture
                    # self.player_two.chose_gesture()
                elif self.user_input == '2':
                    self.player_two = Humans()
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
        
print(f"AI: {AI_option}")
print(f"{player_one} option: {player_option}")



while NumberofRounds<3:
    //something about the players and choices here..//
    
NumberOfRounds += 1


if player_one_gesture==player_two_gesture
    print('Tie, next round')
    continue
elif player_two==0 and Player_one==3:
    print('Rock crushes Lizard')
    print(f'{player.name()} wins')
    continue
elif player_two==0 and player_one==2:
    print('Rock crushes scissors!')
    print(f'{player.name()} wins')
    continue
elif player_two==1 and player_one==0:
    print('Paper covers rock')
    print(f'{player.name()} wins')
    continue
elif player_two==1 and player_one==4
    print('Paper disproves Spock')
    print(f'{player.name()} wins')
    continue
elif player_two==2 and player_one==1:
    print('Scissors cut paper')
    print(f'{player.name()} wins')
    continue
elif player_two==2 and player_one==3:
    print('Scissors decapitates Lizard')
    print(f'{player.name()} wins')
    continue
elif player_two==3 and player__one==1:
    print('Lizard eats paper')
    print(f'{player.name()} wins')
    continue
elif player_two==3 and player_one==4:
    print('Lizard poisons Spock')
    print(f'{player.name()} wins')
    continue
elif player_two==4 and player_one==0:
    print('Spock vaporizes rock')
    print(f'{player.name()} wins')
    continue
elif player_two==4 and player_one==2:
    print('Spock smashes scissors')
    print(f'{player.name()} wins')
    continue
elif player_one==0 and Player_two==3:
    print('Rock crushes Lizard')
    print(f'{player.name()} wins')
    continue
elif player_one==0 and player_two==2:
    print('Rock crushes scissors!')
    print(f'{player.name()} wins')
    continue
elif player_one==1 and player_two==0:
    print('Paper covers rock')
    print(f'{player.name()} wins')
    continue
elif player_one==1 and player_two==4
    print('Paper disproves Spock')
    print(f'{player.name()} wins')
    continue
elif player_one==2 and player_two==1:
    print('Scissors cut paper')
    print(f'{player.name()} wins')
    continue
elif player_one==2 and player_two==3:
    print('Scissors decapitates Lizard')
    print(f'{player.name()} wins')
    continue
elif player_one==3 and player__two==1:
    print('Lizard eats paper')
    print(f'{player.name()} wins')
    continue
elif player_one==3 and player_two==4:
    print('Lizard poisons Spock')
    print(f'{player.name()} wins')
    continue
elif player_one==4 and player_two==0:
    print('Spock vaporizes rock')
    print(f'{player.name()} wins')
    continue
elif player_one==4 and player_two==2:
    print('Spock smashes scissors')
    print(f'{player.name()} wins')
    continue
else:
    print('Choose a valid option to play this game!')


gameOn=True

while gameOn:
