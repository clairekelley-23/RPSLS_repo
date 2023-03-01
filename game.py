import random
import math
from ai import AI
from human import Humans

class Game():
    def __init__(self):
        super().__init__()
        self.player_one = Humans('Player One')
        self.player_two = None

    def display_welcome():
        welcome = 'Welcome to Rock Paper Scissors Lizard Spock!'
        return welcome
        
    def game_rules():
        game_rules = "Each game is the best of three\nUse the number keys to make a selection\n\nScissors cut paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes scissors\nScissors decapitates Lizard\nLizard eats paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock Crushes scissors"
        return game_rules

    def best_of(n):
            player_one_score=0
            player_two_score=0
            wins_necessary=math.ceil(n/2)
            print(wins_necessary)

     
# winning condiditions 0>2,3 and 1>0,4 and 2>1,3 and 3>4,1 and 4>2,0
        # elif (player_one== 0 and player_two==2 or 3) or (player_one==1 and player_two==0 or 4) or (player_one==2 and player_two==1 or 3) or (player_one==3 and player_two==4 or 1) or (player_one==4 and player_two==2,0):
        #     return True
        # elif (player_two== 0 and player_one==2 or 3) or (player_two==1 and player_one==0 or 4) or (player_two==2 and player_one==1 or 3) or (player_two==3 and player_one==4 or 1) or (player_two==4 and player_one==2,0):
        #     return True
        # return False
    def player_choice(self):
        print("How many players? 1 or 2\n")
        self.user_input = " "
        while True:
            if self.user_input == '1':
                self.player_two = AI()
                self.player_one = Humans.player_one()
            elif self.user_input == '2':
                self.player_two = Humans.player_two()
                self.player_one = Humans.player_one()
            else:
                continue
            return self.player_choice
            

    def run_game(self):
        print(self.display_welcome)
        print(self.game_rules)
        print(self.player_choice)
        print(self.game_rounds)
        print(self.end_game)

    def game_rounds(self):
        self.best_of(3)  
        self.number_of_rounds=0
        while self.Players.score<2:
            number_of_rounds+=1
        print(self.player_choice)
        
        self.user_input.player_one= ''
        self.user_input.player_two= ''

        while True:
            if self.player_one==self.player_two:
                return "It's a tie! Choose another. "
            elif self.player_two==0 and self.player_one==3:
                print('Rock crushes Lizard')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_two==0 and self.player_one==2:
                print('Rock crushes scissors!')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_two==1 and self.player_one==0:
                print('Paper covers rock')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_two==1 and self.player_one==4:
                print('Paper disproves Spock')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_two==2 and self.player_one==1:
                print('Scissors cut paper')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_two==2 and self.player_one==3:
                print('Scissors decapitates Lizard')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_two==3 and self.player__one==1:
                print('Lizard eats paper')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_two==3 and self.player_one==4:
                print('Lizard poisons Spock')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_two==4 and self.player_one==0:
                print('Spock vaporizes rock')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_two==4 and self.player_one==2:
                print('Spock smashes scissors')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_one==0 and self.Player_two==3:
                print('Rock crushes Lizard')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_one==0 and self.player_two==2:
                print('Rock crushes scissors!')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_one==1 and self.player_two==0:
                print('Paper covers rock')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_one==1 and self.player_two==4:
                print('Paper disproves Spock')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_one==2 and self.player_two==1:
                print('Scissors cut paper')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_one==2 and self.player_two==3:
                print('Scissors decapitates Lizard')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_one==3 and self.player__two==1:
                print('Lizard eats paper')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_one==3 and self.player_two==4:
                print('Lizard poisons Spock')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_one==4 and self.player_two==0:
                print('Spock vaporizes rock')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            elif self.player_one==4 and self.player_two==2:
                print('Spock smashes scissors')
                print(f'{self.player.name()} wins')
                number_of_rounds+=1
            else:
                print('Choose a valid option to play this game!')  
            
    
        
    def end_game(self,best_of):
        best_of(3)
        self.Players.score==2
        while True:
            print(f'{self.Players.name()} won best of 3!')
            print('Would you like to play again? Y or N ')
        
            if self.player_one=='Y' or self.player_two=='Y':
                return self.game_rounds
            else:
                print('Thanks for playing!')
                break
       



# while True:
#         game_rounds() 



# def game_play(self):
#     game_play==
#         (display_welcome())
#         (game_rules())
#         (player_choice())
#         (game_rounds())
#         (best_of())
#         (display_winner())
#     return game_play



           