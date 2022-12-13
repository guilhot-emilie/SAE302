import platform, cpuinfo, psutil
from socket import *
#télécharger py-cpuinfo
#psutils

print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"OS: {uname.system} {uname.version}")
print(f"Nom du pc: {uname.node}")
print ("adresse IP",gethostbyname(gethostname()))

print("="*40, "TEST", '='*40)

print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
print(f"cpu info: {cpuinfo.get_cpu_info()}")

print(psutil.virtual_memory())


