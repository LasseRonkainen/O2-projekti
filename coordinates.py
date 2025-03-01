
class Coordinates():
    """
    Coordinaatit luontaisesti vasemmalta oikealle x
    ja ylhäältä alas y (helposti listojen kanssa voi mennä ristiin nämä)
    Koko luokan pointti on hakea viereisiä koordinaattipareja, 
    mikä on pelimekaaniikan kannalta oleellinen
    """

    def __init__(self, x, y):

        self.x = x
        self.y = y    

    def get_x(self):
        return self.x


    def get_y(self):
        return self.y


    def get_neighbors(self):
        """
        TODO toteuta
        Palauttaa kaikki viereiset koordinaattiparit
        """
        return self
    
    def is_neighbor(self, coordinates):
        """
        TODO toteuta
        Tarkastaa, onko kyseinen koordinaattipari viereistä tämän koordinaattiparin kanssa
        ja palauttaa vastaavan totuusarvon
        """
        return True


    def __str__(self):
        """
        Palauttaa Stringin muodossa (X, Y)
        """
        return '({:.0f}, {:.0f})'.format(self.get_x(), self.get_y())
