from player import Player

class EnemyPlayer(Player):

    def __init__(self, faction, faction_color, strength, bonus, brain):
        super().__init__(faction, faction_color, strength, bonus )
        self.brain = brain