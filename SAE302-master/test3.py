import time

from client import server

host1 = "127.0.0.1" #input("1er serveur")
host2 = "127.0.0.1" #input("2eme serveur")
hostsock1 = server(host1, 5005)
hostsock2 = server(host2, 4004)
hostsock1.connect()
hostsock2.connect()
time.sleep(2)

for i in range(10):
    print(f"{i} envoi")
    hostsock1.send("OS")
    hostsock2.send("CPU")

hostsock1.close()
hostsock2.close()