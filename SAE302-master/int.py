import sys
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        qw = QWidget()
        self.setCentralWidget(qw)
        grid = QGridLayout()
        qw.setLayout(grid)

        #Box
        blocco = QGroupBox("Connexion")
        blocco.setLayout(QGridLayout())
        blocdis = QGroupBox("Discussion")
        blocdis.setLayout(QGridLayout())
        blocinfo = QGroupBox("Information Serveur")
        blocinfo.setLayout(QGridLayout())

        labip = QLabel("IP:")
        labport = QLabel("Port:")
        self.__textip = QLineEdit("")
        self.__textport = QLineEdit("")
        conv = QLabel("")
        labmess = QLabel("Message:")
        msg = QLineEdit("")
        send = QPushButton(">")
        connexion = QPushButton("Connexion")
        envoyer = QPushButton("Envoyer")
        quit = QPushButton("Quitter")
        aide = QPushButton("Aide")
        #info
        name = QLabel("Nom")
        ip = QLabel("IP")
        os = QLabel("OS")
        ram = QLabel("RAM")
        cpu = QLabel("CPU")
        croixname = QCheckBox()
        croixip = QCheckBox()
        croixos = QCheckBox()
        croixram = QCheckBox()
        croixcpu = QCheckBox()

        # bloc dans grid layout
        grid.addWidget(blocco, 0, 0, 4, 0)
        grid.addWidget(blocdis, 4, 0, 10, 6)
        grid.addWidget(blocinfo, 4, 6, 8, 4)

        #  les composants au grid layout
        blocco.layout().addWidget(labip, 0, 0)
        blocco.layout().addWidget(labport, 0, 2)
        blocco.layout().addWidget(self.__textip, 0, 1)
        blocco.layout().addWidget(self.__textport, 0, 3)
        blocco.layout().addWidget(connexion, 0, 4)
        blocdis.layout().addWidget(conv, 1, 1)
        blocdis.layout().addWidget(labmess, 6, 0)
        blocdis.layout().addWidget(msg, 6, 1)
        blocdis.layout().addWidget(send, 6, 2)
        blocinfo.layout().addWidget(name, 1, 1)
        blocinfo.layout().addWidget(ip, 2, 1)
        blocinfo.layout().addWidget(os, 3, 1)
        blocinfo.layout().addWidget(cpu, 4, 1)
        blocinfo.layout().addWidget(ram, 5, 1)
        blocinfo.layout().addWidget(croixname, 1, 2)
        blocinfo.layout().addWidget(croixip, 2, 2)
        blocinfo.layout().addWidget(croixos, 3, 2)
        blocinfo.layout().addWidget(croixcpu, 4, 2)
        blocinfo.layout().addWidget(croixram, 5, 2)
        blocinfo.layout().addWidget(envoyer, 6, 3)
        grid.addWidget(aide, 12, 7)
        grid.addWidget(quit, 12, 8)


        quit.clicked.connect(self._actionQuitter)

        self.setWindowTitle("tchat serveur")


    def _actionQuitter(self):
        QCoreApplication.exit(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()