import socket, threading, sys, time
from PyQt5.QtWidgets import *
from aide import Aide
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
        self.__textip = QLineEdit("127.0.0.1")
        self.__textport = QLineEdit("5005")
        self.__conv = QTextBrowser()
        labmess = QLabel("Message:")
        self.__message = QLineEdit("")
        send = QPushButton(">")
        connexion = QPushButton("Connexion")
        quit = QPushButton("Quitter")
        aide = QPushButton("?")
        # info
        name = QPushButton("Nom")
        infoos = QPushButton("OS")
        inforam = QPushButton("RAM")
        infocpu = QPushButton("CPU")

        # bloc dans grid layout
        grid.addWidget(blocco, 0, 0, 4, 0)
        grid.addWidget(blocdis, 4, 0, 10, 8)
        grid.addWidget(blocinfo, 4, 8, 8, 2)

        #  les composants au grid layout
        blocco.layout().addWidget(host, 0, 0)
        blocco.layout().addWidget(port, 0, 2)
        blocco.layout().addWidget(self.__textip, 0, 1)
        blocco.layout().addWidget(self.__textport, 0, 3)
        blocco.layout().addWidget(connexion, 0, 4)
        blocdis.layout().addWidget(self.__conv, 1, 1)
        blocdis.layout().addWidget(labmess, 6, 0)
        blocdis.layout().addWidget(self.__message, 6, 1)
        blocdis.layout().addWidget(send, 6, 3)
        blocinfo.layout().addWidget(name, 1, 1)
        blocinfo.layout().addWidget(infoos, 3, 1)
        blocinfo.layout().addWidget(infocpu, 4, 1)
        blocinfo.layout().addWidget(inforam, 5, 1)
        grid.addWidget(aide, 13, 8)
        grid.addWidget(quit, 13, 9)

        connexion.clicked.connect(self.connect)
        quit.clicked.connect(self.close)
        send.clicked.connect(self.send)
        name.clicked.connect(self.name)
        infoos.clicked.connect(self.infoos)
        infocpu.clicked.connect(self.infocpu)
        inforam.clicked.connect(self.inforam)
        aide.clicked.connect(self.aide)

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
        self.__tsend = threading.Thread(target = self.__send, args=[msg, msgserv])
        self.__tsend.start()

    def __send(self, msg, msgserv):
        msg = self.__message.text()
        if self.isConnected():
            self.__verrou = threading.Lock()
            try:
                self.__verrou.acquire()
                self.__socket.send(msg.encode())
                self.__conv.append("Message envoyé: " + msg)
                msgserv = self.__socket.recv(1024).decode()
                if msgserv != "kill" and msgserv != "reset" and msgserv != "disconnect":
                    self.__conv.append("Message reçu: " + msgserv)
            except socket.error as err:
                print(f"erreur = {err}")
            finally:
                self.__verrou.release()
        else:
            print("Pas de connexion")

    def name(self, msg):
        msg = "name"
        self.__socket.send(msg.encode())
        msgserv = self.__socket.recv(1024).decode()
        if msgserv != "kill" and msgserv != "reset" and msgserv != "disconnect":
            self.__conv.append("Message reçu: " + msgserv)

    def infoos(self, msg):
        msg = "os"
        self.__socket.send(msg.encode())
        msgserv = self.__socket.recv(1024).decode()
        if msgserv != "kill" and msgserv != "reset" and msgserv != "disconnect":
            self.__conv.append("Message reçu: " + msgserv)

    def infocpu(self, msg):
        msg = "cpu"
        self.__socket.send(msg.encode())
        msgserv = self.__socket.recv(1024).decode()
        if msgserv != "kill" and msgserv != "reset" and msgserv != "disconnect":
            self.__conv.append("Message reçu: " + msgserv)

    def inforam(self, msg):
        msg = "ram"
        self.__socket.send(msg.encode())
        msgserv = self.__socket.recv(1024).decode()
        if msgserv != "kill" and msgserv != "reset" and msgserv != "disconnect":
            self.__conv.append("Message reçu: " + msgserv)

    def aide(self):
        self.__aide = Aide()
        self.__aide.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = client('127.0.0.1', 5005)

    host = "127.0.0.1"
    host1 = host, 5005
    time.sleep(2)

    msg = msgserv = ""
    while msg != "kill" and msg != "reset" and msg != "disconnect":
        window.show()
        app.exec()
    host1.close()