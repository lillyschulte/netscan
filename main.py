# Import required libraries
import socket
import subprocess

# Set the network range to scan
network = "192.168.1.0/24"

# Use the nmap command to scan the network
output = subprocess.run(["nmap", "-sn", network], capture_output=True)

# Loop through the output lines
for line in output.stdout.decode().splitlines():
    # Check for lines containing IP addresses
    if "Nmap scan report for" in line:
        # Extract the IP address from the line
        ip_address = line.split("for ")[1]

        # Print the IP address
        print(ip_address)
