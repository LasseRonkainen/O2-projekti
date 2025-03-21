from PyQt6 import QtWidgets, QtCore, QtGui
from army import Army

class Player():

    def __init__(self, faction, color, strength, bonus):
        
        #Haetaan configista
        self.faction = faction
        self.color =  QtGui.QColor(color[0], color[1], color[2])
        self.strength = strength
        self.bonus = bonus

        #Haetaan statesta, defaultina nämä
        self.armies = []
        self.score = 0

        #Mahdolliseen värkkäilyyn
        self.world = None


    def set_world(self, world):
        """
        Asettaa pelaajalle pelimaailman, tarvitaan joissain funktioissa
        """
        self.world = world

    def get_faction(self):
        """
        Palauttaa pelaajan factionin: String
        """
        return self.faction
    
    def get_color(self):
        """
        Palauttaa pelaajan edustaman factionin värin: QColor
        """
        return self.color
    
    def get_bonus(self):

        return self.bonus

    def get_strength(self):
        return self.strength
    
    def get_score(self):
        return self.score
    
    def get_armies(self):
        return self.armies   

    def get_army(self, coordinates):

        for army in self.armies:
            if army.get_coordinates() == coordinates:
                return army

        return None
    
    def calculate_score(self):
        self.score += 0 # TODO

    def create_army(self, size, coordinates):

        """
        Luo annetun kokoisen armeijan annettuihin koordinaatteihin.
        Palautetaanko vaikka totuusarvo varmistamaan?        
        """
        army = Army(self, size, coordinates)
        self.armies.append(army)