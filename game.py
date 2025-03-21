from configerror import ConfigError
from smallworld import SmallWorld
from human_player import HumanPlayer
from enemy_player import EnemyPlayer

class Game():

    def __init__(self):

        self.turn_number = 0
        self.turn = None
        self.players = []
        self.world = None

        #config muuttujia, käytetään vain pelin luomisessa
        self.window_size = None
        self.window_offset = None
        self.square_size = None
        self.game_size = None

        self.terrain_file = None
        self.world_terrain = []
    
        #Luetaan configit, kartta ja    TODO state, setupataan peli
        self.read_config('config.txt')
        self.read_world(self.terrain_file)
        self.set_game()

    
    def get_world(self):
        """
        Palauttaa luodun maailman (SmallWorld), mikäli sellainen luoto
        tai None jos ei moista ole
        """
        return self.world
    
    def get_players(self):
        """
        Palauttaa listan kaikista pelin pelaajista
        """
        return self.players
    
    def get_player(self, faction):
        """
        Palauttaa pelaajan sen factionin perusteella 
        tai None kyseisellä factionilla ei ole pelaajaa
        """
        for player in self.players:
            if player.get_faction() == faction:
                return player
            
        return None
    
    def get_human_player(self):
        for player in self.players:
            if isinstance(player, HumanPlayer):
                return player

    def set_game(self):
        """
        Luodaan kartta ja pelaajat luetuilla parametreillä
        """

        self.world = SmallWorld(self.game_size, self.world_terrain)
        player = HumanPlayer('Humans', (0,0,150), 2, "Field")
        player.set_world(self.get_world())
        player2 = EnemyPlayer('Orcs', (0,150,0), 3, None, "Hill")
        player2.set_world(self.get_world())
        player3 = EnemyPlayer('Undead', (150,0,0), 7, None, None)
        player3.set_world(self.get_world())
        self.players.append(player)
        self.players.append(player2)
        self.players.append(player3)

    def read_config(self, file):       
        """
        Luetaan kaksoispisteellä erotettuna tiedon nimi ja arvo, eval(x) saadaan suoraan muunnokset tuplista int-muotoon
        """

        try:
            with open(file, 'r') as f:

                line = f.readline().strip()
         
                if line == "Config": #Näyttää olevan vaan väliaikasesti ettei lue tekemätöntä osaa...

                    while line != "#End":

                        line = f.readline().strip()
                         
                        if line != "" and line[0] != "#":

                            line = line.split(':')
                            info = line[0]
                            value = line[1]
                    
                            if info == "window_size":
                                self.window_size = eval(value)
                            elif info == "window_offset":
                                self.window_offset = eval(value)
                            elif info == "square_size":
                                self.square_size = eval(value)
                            elif info == "game_size":
                                self.game_size = eval(value)
                            elif info == "map_terrain":
                                self.terrain_file = value

                        """
                        Rivi jaetaan kahtia kaksoispisteen kohdalta
                        Vasemmalle puolelle jää muuttuja ja oikealle muuttujan arvo
                        # - rivejä ei lueta vaan ne helpottavat configin muokkausta
                        """

                else:
                    raise ConfigError("ei ole config tiedosto")
                
            f.close()

            """Tarkistetaan, että kaikki tarvittava on"""
            if (self.window_size and self.window_offset and self.square_size
                 and self.game_size and self.terrain_file):
                pass
            else:
                raise ConfigError("Config ei ole tallentanut tarvittavia tietoja")

        except OSError:
            raise ConfigError("tiedosdonluku ei onnistunut")

    def read_world(self, file):

        """
        Luetaan pelikartan tiedot ja käännetään ne numeroista merkkijonoiksi,
        voitaisiin myös suoraan kirjoittaa config tiedostoon merkkijonoina,
        mutta tehdään nyt tässä
        """

        width = self.game_size[0]
        height = self.game_size[1]

        self.world_terrain = height * [None]
        for i in range(height):   
            self.world_terrain[i] = [None] * width

        """Luodaan lista pelimaailmaa varten"""

        try:

            with open(file, 'r') as f:
                lines = f.readlines()
                
                if len(lines) == len(self.world_terrain):

                    for i, line in enumerate(lines):
                        line = line.strip()
                        line = line.replace(" ", "")    #Karttatiedostossa tabulaattori numeroiden välissä

                        if len(line) == len(self.world_terrain[i]):

                            for j, l in enumerate(line):
                                if l == '1':
                                    terrain = 'Field'
                                elif l == '2':
                                    terrain = 'Forest'
                                elif l == '3':
                                    terrain = 'Hill'
                                else:
                                    terrain = 'Abyss'

                                self.world_terrain[i][j] = terrain 
                    
                        else:
                            raise ConfigError("terrainin koko ei vastaa maailman kokoa (leveys)")
                        
                else:
                    raise ConfigError("terrainin koko ei vastaa maailman kokoa (korkeus)")
                               
            f.close()

            if (width == len(self.world_terrain[0]) and height == len(self.world_terrain)):
                pass
            else:
                raise ConfigError("Kartan koko luettu väärin")


        except OSError:
            raise ConfigError("tiedosdonluku ei onnistunut")
