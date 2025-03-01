import unittest

from smallworld import SmallWorld
from coordinates import Coordinates
from game import Game

class Test(unittest.TestCase):

    def test_world(self):
        pass

    def test_config(self):
        testGame = Game()
        testWorld = testGame.get_world()

        """
        Testataan koordinaatit
        """
        self.assertEqual(testWorld.contains(Coordinates(3,3)), True, 
                         "Maailmalla ei ole sille kuuluvia koordinaatteja, kuuluisi palauttaa True")
        self.assertNotEqual(testWorld.contains(Coordinates(8, 8)), True, 
                            "Maailma ylittä oman kokonsa, kuuluisi palauttaa False")

        """
        Testataan maailman koko
        """
        self.assertEqual(testWorld.get_width(), 8, 
                         "Maailma ei vastaa annettua kokoa (width)")
        self.assertNotEqual(testWorld.get_height(), 5, 
                            "Maailma ei vastaa annettua kokoa (height)")

        """
        Testataan maasto
        """
        self.assertEqual(testWorld.get_square(Coordinates(7, 6)).get_terrain().get_group(), 'Forest', 
                         "Väärä maasto kohdassa (7, 6), kuuluisi olla Forest")
        self.assertEqual(testWorld.get_square(Coordinates(1, 1)).get_terrain().get_penalty(), 2, 
                         "Penalty on asetettu väärin kohdass (1, 1), kuuluisi olla 2")

        """
        Testataan pelaajien luonti
        """
        self.assertEqual(testGame.get_player('Undead'), testGame.get_players()[2], 
                         'Pelaajien haku factionilla ei toimi, kuuluisi palauttaa listalta 3 pelaaja')
        self.assertNotEqual(testGame.get_player('Taistelu-Jaska'), testGame.get_players()[1], 
                            'Pelaajien haku factionilla ei toimi')
        self.assertEqual(testGame.get_players()[1].get_color(), (0, 150, 0), 
                         "Pelaajalla väärä väri")

        testGame.get_player('Humans').create_army(2, Coordinates(2,2))




if __name__ == "__main__":
    unittest.main()
