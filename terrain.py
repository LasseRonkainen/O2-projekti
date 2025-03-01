from PyQt6 import QtWidgets, QtCore, QtGui


class Terrain():

    def __init__(self, group):

        self.group = group
        self.color = QtGui.QColor(0, 0, 0)
        self.penalty  = 100
        self.set_terrain()

        """
        Asetellaan maaston mukaan väri ja "rangaistus", 
        joka vaikuttaa siis kyseisen maaston omaavan laatan valloitukseen.
        Maaston väri on pikimusta ja rangaistus 100, mikä meinaa virhettä tod.näk configissa
        """

    def set_terrain(self):

        if self.group == 'Field':
            self.color = QtGui.QColor(100, 100, 20)
            self.penalty = 2
        elif self.group == 'Forest':
            self.color = QtGui.QColor(20, 150, 20)
            self.penalty = 3
        elif self.group == 'Hill':
            self.color = QtGui.QColor(50, 50, 50)
            self.penalty = 3            


    def get_color(self):
        """
        Palauttaa maaston värin GUI:ta varten: QColor
        """
        return self.color
    
    def get_penalty(self):
        """
        Palauttaa maaston edellyttämän "rangaistuslisän"
        maastossa sijaitsevan laatan valloittamiseksi: Int
        """
        return self.penalty
    
    def get_group(self):
        """
        Palauttaa maaston tyypin: String
        """
        return self.group