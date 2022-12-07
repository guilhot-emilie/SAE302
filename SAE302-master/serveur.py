import socket
import time

port = 5005

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", port))
server_socket.listen(1)

print('En attente du client')
conn, address = server_socket.accept()
print(f'Client connecté {address}')

message = ""
while message != "deco":
    # Réception du message du client
    msgb = conn.recv(1024) # message en by
    message = msgb.decode()
    print(f"Message du client : {message}")

    # J'envoie un message
    #reply = input("Saisir un message : ")
    conn.send(message.encode())
    print(f"Message {message} envoyé")

time.sleep(2)

# Fermeture
conn.close()
print("Fermeture de la socket client")
server_socket.close()
print("Fermeture de la socket serveur")


msg = ""
msgserv = ""
while msg !="arret" and msgserv !="arret" :
    conn, address = server_socket.accept()
    msgserv = msg = ""
    while msg !="bye" and msgserv !="bye" and msg !="arret" and msgserv !="arret" :
        msg= conn.recv(1024).decode()
        print("Message reçu:",msg)
        if msg == "bye":
            conn.send("bye".encode())
        else:
            msgserv = input("Entrez votre message:")
            conn.send(msgserv.encode())
    conn.close()
server_socket.close()