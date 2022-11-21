

class Player:

    def __init__(self) -> None:
        pass
    def player_options(self):
        self.human_vs_ai = 1
        self.human_vs_human = 2
        self.ai_vs_ai = 3
    def choose_player(self, player_options):
        print("How many players? 1, 2, or 3 for a surprise\n")
        if self.answer == 1 OR 2 OR 3:
            print(player_options)
