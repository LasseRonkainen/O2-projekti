from player import Player


class HumanPlayer(Player):

    def __init__(self, faction, faction_color, strength, bonus):
        super().__init__(faction, faction_color, strength, bonus)