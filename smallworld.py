from square import Square

class SmallWorld():


    def __init__ (self, game_size, world_terrain):

        width = game_size[0]
        height = game_size[1]

        """
        Alustetaan kartta maailmalle, ja luodaan Square:t oikeisiin koordinaatteihin
        tämä tarkoittaa sitä, että self.squaresissa pitää asettaa arvot "käänteisesti",
        jotta ne vastaavat koordinaateissa niille kuuluvaa paikkaa
        Tämän voisi myös tiedostonluvussa tehdä toisin...
        """

        """Luodaan maailman kokoa vastaava lista self.squares"""
        self.squares = [None] * height
        for x in range(height):  
            self.squares[x] = [None] * width

        for y in range(self.get_height()):
            for x in range(self.get_width()):
                self.squares[y][x] = Square(world_terrain[y][x])
                
    def get_width(self):
        """
        Palauttaa kartan leveyden
        """
        return len(self.squares[0])


    def get_height(self):
        """
        Palauttaa kartan pituuden
        """
        return len(self.squares)
    
    def contains(self, coordinates):
        """
        Tarkastaa onko kyseiset koordinaatit kartalla:
        ja palauttaa totuusarvon sen mukaan
        """
        x_coordinate = coordinates.get_x()
        y_coordinate = coordinates.get_y()
        return 0 <= x_coordinate < self.get_width() and 0 <= y_coordinate < self.get_height()


    def get_square(self, coordinates):
        """
        Palauttaa koordinaateissa sijaitsevan Squaren:
        palauttaa None jos ei mitään ollut kyseisissä koordinaateissa
        """

        if self.contains(coordinates):
            return self.squares[coordinates.get_y()][coordinates.get_x()]
        else:
            return None
    

