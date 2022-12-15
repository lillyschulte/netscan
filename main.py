# Import required libraries
import socket
import subprocess
import tkinter as tk

# Set the network range to scan
network = "192.168.1.0/24"

# Create the GUI window
window = tk.Tk()
window.title("Network Scanner")

# Create a text area to display the results
text_area = tk.Text(window)
text_area.pack(fill=tk.BOTH, expand=True)

# Function to scan the network and display the results
def scan_network():
    # Use the nmap command to scan the network
    output = subprocess.run(["nmap", "-sn", network], capture_output=True)

    # Clear the text area
    text_area.delete(1.0, tk.END)

    # Loop through the output lines
    for line in output.stdout.decode().splitlines():
        # Check for lines containing IP addresses
        if "Nmap scan report for" in line:
            # Extract the IP address from the line
            ip_address = line.split("for ")[1]

            # Print the IP address to the text area
            text_area.insert(tk.END, ip_address + "\n")

# Create a button to start the scan
scan_button = tk.Button(window, text="Scan Network", command=scan_network)
scan_button.pack(fill=tk.X)

# Start the GUI event loop
window.mainloop()
