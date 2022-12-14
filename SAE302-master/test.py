import platform, cpuinfo, psutil
from socket import *
#télécharger py-cpuinfo

uname = platform.uname()
print("="*40, "System Information", "="*40)

print(f"OS: {uname.system} {uname.version}")
print(f"Nom du pc: {uname.node}")
print ("adresse IP",gethostbyname(gethostname()))
print("cpu pourcentage:",psutil.cpu_percent(1),"%")

print("="*40, "TEST", '='*40)

print(f"Processor: {uname.processor}")
print(f"cpu info: {cpuinfo.get_cpu_info()}")

print(psutil.virtual_memory())
