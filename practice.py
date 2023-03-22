import random

class Game:
    def __init__(self):
        self.options = ["rock", "paper", "scissors", "lizard", "spock"]
        self.winning_combinations = {
            "rock": ["scissors", "lizard"],
            "paper": ["rock", "spock"],
            "scissors": ["paper", "lizard"],
            "lizard": ["paper", "spock"],
            "spock": ["rock", "scissors"]
        }
        self.player_score = 0
        self.computer_score = 0

    def get_player_choice(self):
        while True:
            player_choice = input("Enter your choice (rock/paper/scissors/lizard/spock): ")
            if player_choice in self.options:
                return player_choice
            print("Invalid choice. Please try again.")

    def get_computer_choice(self):
        return random.choice(self.options)

    def get_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        elif computer_choice in self.winning_combinations[player_choice]:
            return "player"
        else:
            return "computer"

    def play_round(self):
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        print(f"You chose {player_choice}. The computer chose {computer_choice}.")
        winner = self.get_winner(player_choice, computer_choice)
        if winner == "player":
            self.player_score += 1
            print("You win this round!")
        elif winner == "computer":
            self.computer_score += 1
            print("The computer wins this round!")
        else:
            print("This round is a tie.")

    def play_game(self):
        print("Let's play Rock Paper Scissors Lizard Spock!")
        for i in range(3):
            print(f"Round {i+1}:")
            self.play_round()
            print(f"Score: Player {self.player_score}, Computer {self.computer_score}")
        if self.player_score > self.computer_score:
            print("Congratulations! You win!")
        elif self.player_score < self.computer_score:
            print("Sorry, the computer wins.")
        else:
            print("The game is a tie.")

game = Game()
game.play_game()


game = Game()
game.play_game()
