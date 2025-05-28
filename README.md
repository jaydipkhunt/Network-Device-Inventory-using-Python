Project Title: Network Device Inventory Script
Description
This project provides a Python script (Excel.py) that connects to multiple Cisco IOS devices, retrieves OS version and serial number information, and exports the data to an Excel file. It uses the netmiko library for SSH connectivity and openpyxl for Excel file manipulation.

**Features**
Secure credential input using getpass
IP addresses loaded from an external file (device.txt)

**Gathers:**
IP address
OS version
Serial number
Exports results to network_device_inventory.xlsx
Basic error handling for unreachable or invalid devices

**Files**
Excel.py: Main script to perform device data collection.
device.txt: List of IP addresses of Cisco devices (one per line).
network_device_inventory.xlsx: Output file (generated on script execution).

**Requirements**
Python 3.x
netmiko
openpyxl
Installation
bashCopyEditpip install netmiko openpyxl

**Usage**

bashCopyEditpython Excel.py

You will be prompted for your username and password.

**Example device.txt**

192.168.1.1
192.168.1.2
