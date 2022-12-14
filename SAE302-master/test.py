import platform, cpuinfo, psutil
from socket import *
#télécharger py-cpuinfo

uname = platform.uname()
print("="*40, "System Information", "="*40)

print(f"OS: {uname.system} {uname.version}")
print(f"Nom du pc: {uname.node}")
print ("adresse IP",gethostbyname(gethostname()))
print("cpu pourcentage:",psutil.cpu_percent(1),"%")
print("RAM totale:",round(psutil.virtual_memory().total / (1024.0 ** 3), 2),"GB")


print("="*40, "TEST", '='*40)

memorytotal = psutil.virtual_memory().total / (1024.0 ** 3)
