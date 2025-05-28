from netmiko import ConnectHandler
from getpass import getpass
import openpyxl

# Get credentials securely
username = input("Enter your username: ")
password = getpass("Enter your password: ")

# Read devices from file
with open("device.txt") as f:
    devices = [line.strip() for line in f if line.strip()]

# Create Excel workbook
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Device Info"
ws.append(["IP Address", "OS Version", "Serial Number"])

for ip in devices:
    try:
        print(f"Connecting to {ip}...")
        device = {
            "device_type": "cisco_ios",
            "host": ip,
            "username": username,
            "password": password,
        }
        connection = ConnectHandler(**device)

        # Get OS version and serial number
        version_output = connection.send_command("show version")
        os_version = ""
        serial_number = ""

        for line in version_output.splitlines():
            if "Cisco IOS Software" in line:
                os_version = line.strip()
            if "System serial number" in line or "Processor board ID" in line:
                serial_number = line.split()[-1]

        ws.append([ip, os_version, serial_number])
        connection.disconnect()
    except Exception as e:
        print(f"Failed to connect to {ip}: {e}")
        ws.append([ip, "Error", "Error"])

# Save Excel file
wb.save("network_device_inventory.xlsx")
print("Inventory collected and saved to network_device_inventory.xlsx")
