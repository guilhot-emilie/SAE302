import platform, psutil
from socket import *

uname = platform.uname()

def commande(msg):
    if msg == "OS":
        conn.send(f"OS: {uname.system} {uname.version}").encode()
        print(f"OS: {uname.system} {uname.version}")
    elif msg == "Name":
        print(f"Nom du pc: {uname.node}")
    elif msg == "IP":
        print ("adresse IP",gethostbyname(gethostname()))
    elif msg == "cpu":
        print("cpu pourcentage:",psutil.cpu_percent(1),"%")
    elif msg == "ram":
        print("RAM totale:",round(psutil.virtual_memory().total / (1024.0 ** 3), 2),"GB")
        print("RAM utilisée:", round(psutil.virtual_memory().used / (1024.0 ** 3), 2), "GB")
        print("RAM libre:", round(psutil.virtual_memory().free / (1024.0 ** 3), 2), "GB")
    else:
        pass