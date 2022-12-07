import socket, threading

class server:
    def __init__(self, host, port):
        self.__port = port
        self.__host = host
        self.__socket = None
        # self.verrou = threading.Lock()
        # self.verrou.acquire()
        # self.verrou.release()

    def __connected(self):
        self.__socket = socket.socket()
        self.__socket.connect((self.__host, self.__port))

    def isConnected(self):
        return(self.__socket!=None)

    def close(self):
        self.__tsend.join()
        self.__send("deco")
        self.__socket.close()

    def connect(self):
        self.__tconnected = threading.Thread(target = self.__connected)
        self.__tconnected.start()

    def send(self, msg):
#        self.__send(msg)
        self.__tsend = threading.Thread(target = self.__send, args=[msg])
        self.__tsend.start()

    def __send(self, msg):
        if self.isConnected():
            self.__verrou = threading.Lock()
            try:
                self.__verrou.acquire()
                self.__socket.send(msg.encode())
                msg = self.__socket.recv(1024).decode()
            except socket.error as err:
                print(f"erreur = {err}")
            else:
                print(f"Reponse du serveur : {msg}")
            finally:
                self.__verrou.release()
        else:
            print("Pas de connexion")
