import time
from client import client

host1 = "127.0.0.1" #input("adresse du 1er serveur:")
hostsock1 = client(host1, 5005)
hostsock1.connect()
time.sleep(2)

msg = ""
msgserv = ""
while msg != "deco" and msgserv != "deco":
    msg = input("Entrez votre message:")
    hostsock1.send(msg)
    hostsock1.recep(msgserv)
hostsock1.close()
