MAC Changer Tool

This Python script allows you to change the MAC (Media Access Control) address of a network interface on Linux systems. It provides functionality to either generate a random MAC address or set a custom MAC address.
Requirements

    Python 3.x
    ifconfig or ip command for network interface management (ensure net-tools is installed for ifconfig)
    sudo privileges (required to change MAC address)

Features

    Random MAC Address Generation: You can generate a random MAC address.
    Custom MAC Address: You can set a specific MAC address manually.
    Network Interface Management: The script can bring the network interface down, change its MAC address, and bring it back up.

Installation

    Ensure you have Python 3 installed on your machine. If not, install Python 3 from your package manager or Python's website.
    Install net-tools (if ifconfig is not available):

    sudo apt update
    sudo apt install net-tools

Usage

The script can be run from the command line with the following options:
Command Line Options

    -i INTERFACE, --interface INTERFACE: Specify the network interface you want to change the MAC address for (e.g., eth0, wlan0).
    -r, --random: Generate a random MAC address.
    -m MAC, --mac MAC: Set a specific MAC address (e.g., 00:11:22:33:44:55).
    -h, --help: Display help information about the script.

Example Commands

    To change the MAC address to a specific one:

sudo python3 MAC_changer.py -i wlan0 -m 00:11:22:33:44:55

    This will set the MAC address of wlan0 to 00:11:22:33:44:55.

To generate and set a random MAC address:

    sudo python3 MAC_changer.py -i wlan0 -r

        This will generate a random MAC address and set it for the wlan0 interface.

Example Output

Current MAC address: 60:f6:77:7f:d7:7b
Changing MAC address to: 00:11:22:33:44:55
MAC address changed successfully!

Troubleshooting

    SIOCSIFFLAGS: Operation not permitted: This error occurs if you do not have root privileges. Run the script with sudo to fix this:

sudo python3 MAC_changer.py -i wlan0 -m 00:11:22:33:44:55

Command not found (ifconfig): If ifconfig is not found, it may not be installed. Install it by running:

sudo apt update
sudo apt install net-tools

Invalid MAC address format: Ensure the MAC address follows the correct format XX:XX:XX:XX:XX:XX, where XX are two hexadecimal digits.
