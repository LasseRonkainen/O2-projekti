from PyQt6 import QtWidgets, QtCore, QtGui
from coordinates import Coordinates

class GUI(QtWidgets.QMainWindow):


    def __init__(self, game):
        super().__init__()

        self.game = game
        self.game.get_world()

        self.square_width,self.square_height = game.square_size
        self.window_width,self.window_height = game.window_size
        self.window_x_offset,self.window_y_offset = game.window_offset

        #Tehdään layoutit, game_layout on ikkunan main layout tässä
        self.setCentralWidget(QtWidgets.QWidget())
        self.game_layout = QtWidgets.QHBoxLayout()
        self.interface_layout = QtWidgets.QVBoxLayout()
        self.game_layout.addLayout(self.interface_layout)


        self.init_window()      #self.view/self.scene voidaan korvata view/scene
        self.init_interface()
        self.centralWidget().setLayout(self.game_layout)


    def init_window(self):

        #Peli-ikkuna
        self.setGeometry(self.window_x_offset, self.window_y_offset, self.window_width, self.window_height)
        self.setWindowTitle('SmallWorld')
        self.show()

        #Scene
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 600, 700)

        #Kartta tehdään erillisessä funktiossa selvyyden vuoksi
        self.init_world(self.scene)

        #View scene näyttämiseen
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.game_layout.addWidget(self.view)

    def init_world(self, scene):
        
        """
        Tehdään kartta, käytännössä piirrellään neliöitä gridimäisesti. 
        Haetaan maastoa kuvaavat värit ja lisätään sceneen neliöt
        """

        for y in range(self.game.get_world().get_height()):
            for x in range(self.game.get_world().get_width()):
                square = QtWidgets.QGraphicsRectItem()
                square.setRect(x*self.square_width, y*self.square_height, self.square_width, self.square_height)            
                square.setBrush(self.game.get_world().get_square(Coordinates(x, y)).get_terrain().get_color())
                scene.addItem(square)

    def init_interface(self):

        #TODO config also changes values in this class or adjustsize fixes it?

        #Scene
        self.scene = QtWidgets.QGraphicsScene()
        self.scene.setSceneRect(0, 0, 100, 700)

        #Tekstit pelaajan vahvuuttaa ja pisteitä näyttämään, pelaajan heimon edustama väri boxiin
        strength = QtWidgets.QGraphicsTextItem()
        score = QtWidgets.QGraphicsTextItem()
        faction = QtWidgets.QGraphicsRectItem()
        strength.setPlainText('Strength: 0')
        score.setPlainText('Score: 0')
        
        #Fontti
        font = self.font()   
        font.setPointSize(15)
        font.setWeight(450)

        #Fontti ja paikat härveleille
        strength.setFont(font)
        score.setFont(font)
        strength.setPos(0, 100)
        score.setPos(0, 300)
        faction.setRect(0, 500, 100, 100)

        #Lisätään sceneen ja tehdään view, lisätään interface layoutiin
        self.scene.addItem(strength)
        self.scene.addItem(score)
        self.scene.addItem(faction)
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.interface_layout.addWidget(self.view)





