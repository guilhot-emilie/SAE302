import time
from client import server

host1 = "127.0.0.1" #input("adresse du 1er serveur:")
#host2 = "127.0.0.1" #input("adresse du 2eme serveur:")
hostsock1 = server(host1, 5005)
#hostsock2 = server(host2, 4004)
hostsock1.connect()
#hostsock2.connect()
time.sleep(2)

#hostsock2.close()

msg = ""
msgserv = ""
while msg !="deco" :
    msg = input("Entrez votre message:")
    hostsock1.send(msg)
    print ("msg envoyé")
    hostsock1.recep(msgserv)
    #msgserv = client_socket.recv(1024).decode()
    #print("Message reçu:",msgserv)
hostsock1.close()