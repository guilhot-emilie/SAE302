import time, socket
from client import client
#from serveur import serveur

host = "127.0.0.1" #input("adresse du 1er serveur:")
host1 = client(host, 5005)
host1.connect()
time.sleep(2)

msg = msgserv = ""
while msg != "kill" and msg != "reset" and msg != "disconnect":
    msg = input("Entrez votre message:")
    host1.send(msg)
    host1.recep(msgserv)
host1.close()