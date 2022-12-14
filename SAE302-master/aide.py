import sys
from PyQt5.QtWidgets import *


class Aide(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        lab = QLabel("Cette fenêtre permet de discuter avec un serveur à distance.\n Le port et l'adresse du serveur sont déjà mise par défaut mais il est possible de les modifier.")
        lab2 = QLabel("Pour vous connecter au serveur appuyer sur 'Connexion'. \n La conversation aparaît dans la partie discussion, vous pouvez entrer votre message dans la partie dédié en bas puis l'envoyer en appuyant sur la flèche. ")
        lab3 = QLabel("Sur le côté vous pouvez demander à avoir accès à certaines informations du serveur en appuyant dessus, elles apparaitront dans la conversation.")
        lab4 = QLabel("En envoyant kill éteindre le serveur et la connexion.")
        lab5 = QLabel("En envoyant reset, le client se déconnecte et le serveur attend de nouveau une connexion.")
        lab6 = QLabel("En envoyant disconnect, le client se déconnecte.")

        #  les composants au grid layout
        grid.addWidget(lab, 0, 0)
        grid.addWidget(lab2, 1, 0)
        grid.addWidget(lab3, 2, 0)
        grid.addWidget(lab4, 3, 0)
        grid.addWidget(lab5, 4, 0)
        grid.addWidget(lab6, 5, 0)

        self.setWindowTitle("Aide")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Aide()
    window.show()
    app.exec()