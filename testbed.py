import os 
import time
print("[1/2] LOADING ROUTES INTO ROUTING TABLES...")
os.system("ip route add 10.10.0.0/24 via 10.10.100.1 2> /dev/null")
os.system("ip route add 10.10.0.0/24 via 10.10.101.1 2> /dev/null")
os.system("ip route add 10.10.1.0/24 via 10.10.101.2 2> /dev/null")
os.system("ip route add 10.10.1.0/24 via 10.10.102.1 2> /dev/null")
os.system("ip route add 192.168.0.0/24 via 10.10.100.2 2> /dev/null")
os.system("ip route add 192.168.0.0/24 via 10.10.102.2 2> /dev/null")
time.sleep(5)
print("[2/2] ROUTES ADDED AND ROUTING TABLES UPDATED!")
