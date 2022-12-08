import socket

def serveur():
    msg = msgserv = ""
    port = 5005
    conn = None
    server_socket = None
    while msg != "kill" :
        msg = msgserv = ""
        server_socket = socket.socket()
        """ options qui permette de réutiliser l'adresse et le port rapidement"""
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        server_socket.bind(("0.0.0.0", port))

        server_socket.listen(1)
        print('Serveur en attente de connexion')
        while msg != "kill" and msg != "reset":
            msgserv = msg = ""
            try :
                conn, addr = server_socket.accept()
                print(addr)
            except ConnectionError:
                print ("Erreur de connection")
                break
            else :
                while msg != "kill" and msg != "reset" and msg != "disconnect":
                    msg = conn.recv(1024).decode()
                    print('Message du Client: ', msg)
                    msgserv = input('Entrez votre message: ')
                    """ 
                    le serveur va ici récupere les commandes du client et lui renvoyer. Dans la suite de la SAÉ, 
                    le serveur fera pareil mais en renvoyant le résultat des commandes demandées par le client.
                    """
                    conn.send(msgserv.encode())
                conn.close()
        print ("Connection closed")
        server_socket.close()
        print ("Server closed")

# Coder les commande ici

if __name__ == '__main__':
    serveur()