from terrain import Terrain

class Square():
    """
    The class Square represents as single quare/tile in smallworld.
    A square can contain either an army or it can have None. 
    Square must always have terrain.
    """

    def __init__(self, terrain):
        """
        Luodaan laatta, jolla sijaitsevan armeija (army) oletusarvo None
        Square:lla on aina terrain (Terrain)
        """ 
        self.army = None
        self.terrain = Terrain(terrain)

    def get_army(self):
        """
        Palauttaa laattalla olevan armeijan: Army
        tai None jos armeijaa ei mailla halmeilla
        """
        return self.army

    def set_army(self, army):
        """
        Asettaa laattalle armeijan (Army)
        annetaan nyt vielä paluuarvo takaisin varmistamiseksi
        """
        if not self.is_occupied():
            self.army = army
            return True
        else:
            return False


    def remove_army(self):
        """
        Poistaa laattalla olevan armeijan ja antaa sen paluuarvona,
        asettaa laattan armeijaksi (self.army) None
        """
        removed_army = self.get_army()
        self.army = None
        self.occupied = False
        return removed_army
    
    def get_terrain(self):
        """
        Antaa laattalla vallitsevan maaston (Terrain)
        """
        return self.terrain
    
    def get_conquer_conditions(self):
        """
        Laskee laattalla olevan armeijan ja maaston mukaan armeijan koon,
        mikä vaaditaan laatan valloittamiseksi ja palauttaa sen lukuarvona Int
        Aina vaaditaan vähintään 1 sotahullu valtaamaan
        """

        requirement += self.get_terrain().get_penalty()
        
        if self.get_army():
            requirement += self.get_army().get_size()

        return requirement




