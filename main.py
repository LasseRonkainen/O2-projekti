import sys
from PyQt6.QtWidgets import QApplication

from gui import GUI
from game import Game

def main():


    game = Game()

    #QApplication pitää olla aina
    global app # Globaali app koska ilmeisesti ei crashaa silloin
    app = QApplication(sys.argv)
    gui = GUI(game)

    #Aloitetaan Qt event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
