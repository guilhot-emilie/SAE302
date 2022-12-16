import socket, platform, psutil
uname = platform.uname()
class serveur():
    def serveur():
        msg = msgserv = ""
        port = 5005
        conn = None
        server_socket = None
        while msg != "kill":
            msg = msgserv = ""
            server_socket = socket.socket()
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
                        if msg == "os":
                            msgserv = "OS: " + " " + str(uname.system) + " " + str(uname.version)
                            conn.send(msgserv.encode())
                        elif msg == "name":
                            msgserv = "Nom du pc :" + str(uname.node)
                            conn.send(msgserv.encode())
                        elif msg == "cpu":
                            msgserv = "cpu pourcentage :" + str(psutil.cpu_percent(1)) + "%"
                            conn.send(msgserv.encode())
                        elif msg == "ram":
                            msgserv = "RAM totale :" + str(round(psutil.virtual_memory().total / (1024.0 ** 3), 2)) + "GB\n" + "RAM utilisée :" + str(round(psutil.virtual_memory().used / (1024.0 ** 3), 2)) + "GB\n" + "RAM libre :" + str(round(psutil.virtual_memory().free / (1024.0 ** 3), 2)) + "GB"
                            conn.send(msgserv.encode())
                        else:
                            msgserv = input('Entrez votre message: ')
                            conn.send(msgserv.encode())
                            print("msg envoyé")
                    conn.close()
            print("Fin de la connexion")
            server_socket.close()
            print("Serveur fermé")


if __name__ == '__main__':
    serveur.serveur()