import socket
import time

port = 5005
server_socket = socket.socket()
server_socket.bind(("0.0.0.0", port))
server_socket.listen(1)

print('En attente du client')
conn, address = server_socket.accept()
print(f'Client connecté {address}')

msg = ""
msgserv = ""

while msg !="deco":
    msg= conn.recv(1024).decode()
    print("Message reçu:",msg)
    if msg == "deco":
        conn.send("deco".encode())
    else:
        msgserv = input("Entrez votre message:")
        conn.send(msgserv.encode())
time.sleep(2)
conn.close()
print("Fermeture de la socket client")
server_socket.close()
print("Fermeture de la socket serveur")