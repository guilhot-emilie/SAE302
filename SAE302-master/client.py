import socket, threading

class client:
    def __init__(self, host, port):
        self.__port = port
        self.__host = host
        self.__socket = None

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
        msgserv = self.__socket.recv(1024).decode()
        print("Message reçu:", msgserv)

    def rb(self, msg):
        msg = self.__socket.recv(1024).decode()