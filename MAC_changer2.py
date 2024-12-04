import subprocess
import string
import random
import re

def get_random_mac_address():
    """Generate and return a MAC address in the format of Linux"""
    # Get the hex digits uppercased
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper()))
    # 2nd character must be 0, 2, 6, 8, A, C, or E
    mac = ""
    for i in range(6):
        for j in range(2):
            if j == 0:  # 1st character in each MAC pair must follow specific rules
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")

def get_current_mac_address(iface):
    """Use the ifconfig command to get the interface details, including the MAC address"""
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search(r"ether (.+?) ", output).group(1).strip()

def change_mac_address(iface, new_mac_address):
    """Change the MAC address of a network interface"""
    # Disable the network interface
    subprocess.check_output(f"ifconfig {iface} down", shell=True)
    # Change MAC
    subprocess.check_output(f"ifconfig {iface} hw ether {new_mac_address}", shell=True)
    # Enable the network interface again
    subprocess.check_output(f"ifconfig {iface} up", shell=True)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Python MAC changer on Linux")
    parser.add_argument("-r", "--random", action="store_true", help="Whether to generate a random MAC address")
    parser.add_argument("-m", "--mac", help="The new MAC address you want to change to")
    parser.add_argument("-i", "--interface", required=True, help="The network interface to modify")
    args = parser.parse_args()
    
    iface = args.interface
    if args.random:
        # If random parameter is set, generate a random MAC
        new_mac = get_random_mac_address()
    elif args.mac:
        # Use the provided MAC address
        new_mac = args.mac
    else:
        raise ValueError("You must specify either --random or --mac")
    
    current_mac = get_current_mac_address(iface)
    print(f"Current MAC address: {current_mac}")
    print(f"Changing MAC address to: {new_mac}")
    
    change_mac_address(iface, new_mac)
    print("MAC address changed successfully!")
