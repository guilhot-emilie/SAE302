import socket, threading, sys
from PyQt5.QtWidgets import *

class client(QMainWindow):
    def __init__(self, host, port):
        super().__init__()
        self.__port = port
        self.__host = host
        self.__socket = None

        qw = QWidget()
        self.setCentralWidget(qw)
        grid = QGridLayout()
        qw.setLayout(grid)

        # Box
        blocco = QGroupBox("Connexion")
        blocco.setLayout(QGridLayout())
        blocdis = QGroupBox("Discussion")
        blocdis.setLayout(QGridLayout())
        blocinfo = QGroupBox("Information Serveur")
        blocinfo.setLayout(QGridLayout())

        host = QLabel("IP:")
        port = QLabel("Port:")
        self.__textip = QLineEdit("")
        self.__textport = QLineEdit("")
        self.__conv = QLabel("")
        labmess = QLabel("Message:")
        self.__message = QLineEdit("")
        reception = QPushButton("Reception")
        send = QPushButton(">")
        connexion = QPushButton("Connexion")
        envoyer = QPushButton("Envoyer")
        quit = QPushButton("Quitter")
        aide = QPushButton("Aide")
        # info
        name = QLabel("Nom")
        infoip = QLabel("IP")
        infoos = QLabel("OS")
        inforam = QLabel("RAM")
        infocpu = QLabel("CPU")
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
        blocco.layout().addWidget(host, 0, 0)
        blocco.layout().addWidget(port, 0, 2)
        blocco.layout().addWidget(self.__textip, 0, 1)
        blocco.layout().addWidget(self.__textport, 0, 3)
        blocco.layout().addWidget(connexion, 0, 4)
        blocdis.layout().addWidget(reception, 1, 1)
        blocdis.layout().addWidget(self.__conv, 2, 1)
        blocdis.layout().addWidget(labmess, 6, 0)
        blocdis.layout().addWidget(self.__message, 6, 1)
        blocdis.layout().addWidget(send, 6, 2)
        blocinfo.layout().addWidget(name, 1, 1)
        blocinfo.layout().addWidget(infoip, 2, 1)
        blocinfo.layout().addWidget(infoos, 3, 1)
        blocinfo.layout().addWidget(infocpu, 4, 1)
        blocinfo.layout().addWidget(inforam, 5, 1)
        blocinfo.layout().addWidget(croixname, 1, 2)
        blocinfo.layout().addWidget(croixip, 2, 2)
        blocinfo.layout().addWidget(croixos, 3, 2)
        blocinfo.layout().addWidget(croixcpu, 4, 2)
        blocinfo.layout().addWidget(croixram, 5, 2)
        blocinfo.layout().addWidget(envoyer, 6, 3)
        grid.addWidget(aide, 12, 7)
        grid.addWidget(quit, 12, 8)

        connexion.clicked.connect(self.connect)
        reception.clicked.connect(self.recep)
        quit.clicked.connect(self.close)
        send.clicked.connect(self.send)

        self.setWindowTitle("tchat serveur")

    def connect(self):
        self.__tconnected = threading.Thread(target = self.__connected)
        self.__tconnected.start()

    def __connected(self):
        self.__socket = socket.socket()
        self.__socket.connect((self.__host, self.__port))

    def isConnected(self):
        return(self.__socket!=None)

    def close(self):
        self.__tsend.join()
        self.__send("kill")
        self.__socket.close()

    def send(self, msg):
        self.__tsend = threading.Thread(target = self.__send, args=[msg])
        self.__tsend.start()

    def __send(self, msg):
        msg = self.__message.text()
        if self.isConnected():
            self.__verrou = threading.Lock()
            try:
                self.__verrou.acquire()
                self.__socket.send(msg.encode())
            except socket.error as err:
                print(f"erreur = {err}")
            finally:
                self.__verrou.release()
        else:
            print("Pas de connexion")

    def recep(self, msgserv):
        msgserv = ""
        msgserv = self.__socket.recv(1024).decode()
        if msgserv != "kill" and msgserv != "reset" and msgserv != "disconnect":
            self.__conv = QLabel("Message reçu:", msgserv)
        else:
            self.__conv = QLabel("Aucun message reçu")
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = client('127.0.0.1', 5005)
    window.show()
    app.exec()