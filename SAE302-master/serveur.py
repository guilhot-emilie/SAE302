import socket, platform, psutil
from test import commande
#from socket import *

class serveur():
    def serveur():
        msg = msgserv = ""
        port = 5005
        conn = None
        server_socket = None
        while msg != "kill":
            msg = msgserv = ""
            server_socket = socket.socket()
            """ options qui permette de réutiliser l'adresse et le port rapidement"""
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind(("0.0.0.0", port))

            server_socket.listen(1)
            print('Serveur en attente de connexion...')
            while msg != "kill" and msg != "reset":
                msgserv = msg = ""
                try:
                    conn, addr = server_socket.accept()
                    print("Connexion avec le client établie", addr)
                except ConnectionError:
                    print("Erreur de connexion")
                    break
                else:
                    while msg != "kill" and msg != "reset" and msg != "disconnect":
                        msg = conn.recv(1024).decode()
                        print('Message du Client: ', msg)

                        if msg == "kill" or msg == "reset" or msg == "disconnect":
                            msgserv = "kill"
                            conn.send(msgserv.encode())
                            break
                        if msg == 'OS' or msg == 'Name' or msg == 'IP' or msg == 'cpu' or msg == 'ram':
                            commande(msg)
                            print(msgserv)
                            conn.send(msgserv.encode())
                        else:
                            msgserv = input('Entrez votre message: ')
                            conn.send(msgserv.encode())
                    conn.close()
            print("Fin de la connexion")
            server_socket.close()
            print("Serveur fermé")


if __name__ == '__main__':
    serveur.serveur()