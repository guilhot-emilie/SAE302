import platform, psutil
from socket import *

uname = platform.uname()
print("="*40, "System Information", "="*40)

print(f"OS: {uname.system} {uname.version}")
print(f"Nom du pc: {uname.node}")
print ("adresse IP",gethostbyname(gethostname()))
print("cpu pourcentage:",psutil.cpu_percent(1),"%")
print("RAM totale:",round(psutil.virtual_memory().total / (1024.0 ** 3), 2),"GB")
print("RAM utilisée:", round(psutil.virtual_memory().used / (1024.0 ** 3), 2), "GB")
print("RAM libre:", round(psutil.virtual_memory().free / (1024.0 ** 3), 2), "GB")

