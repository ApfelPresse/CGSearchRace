from Game import Game


class Referee:

    def __init__(self, user_input):
        self.game = Game(user_input)

    def game_turn(self):
        self.game.on_round()
