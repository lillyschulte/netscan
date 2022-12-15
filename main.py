# Import required libraries
import socket
import subprocess
import tkinter as tk
from tkinter import Entry
from tkinter import ttk

# Create the GUI window
window = tk.Tk()
window.title("Network Scanner")

# Create a text area to display the results
text_area = tk.Text(window)
text_area.pack(fill=tk.BOTH, expand=True)

# Create a progress bar
progress_bar = ttk.Progressbar(window, mode="determinate")
progress_bar.pack(fill=tk.X)

# Create a Label widget to display the text
label = tk.Label(window, text="Input network ip:")
label.pack()

# Create a checkbox widget to allow the user to include manufacturer information in the results
include_manufacturer = tk.BooleanVar()
include_manufacturer_checkbox = tk.Checkbutton(window, text="Include OS", variable=include_manufacturer)
include_manufacturer_checkbox.pack()

# Function to scan the network and display the results
def scan_network():
    # Get the user input for the network variable
    network = network_input.get()

    # Set the maximum value of the progress bar
    progress_bar["maximum"] = 100

    # Start the progress bar
    progress_bar.start()

    # Use the nmap command to scan the network and get the MAC addresses
    output = subprocess.run(["nmap", "-sn", "-sP", network], capture_output=True)

    # Check if the user has selected to include manufacturer information
    if include_manufacturer.get():
        # Use the nmap command to get the manufacturer of each device
        output2 = subprocess.run(["nmap", "-O", network], capture_output=True)
    else:
        output2 = None

    # Stop the progress bar
    progress_bar.stop()

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

        # Check for lines containing MAC addresses
        if "MAC Address:" in line:
            # Extract the MAC address from the line
            mac_address = line.split("MAC Address: ")[1]

            # Print the MAC address to the text area
            text_area.insert(tk.END, mac_address + "\n")

    # Check if the user has selected to include manufacturer information
    if output2:
        # Loop through the output2 lines
        for line in output2.stdout.decode().splitlines():
            # Check for lines containing device manufacturer
            if "Device type" in line:
                # Extract the manufacturer from the line
                manufacturer = line.split("Device type: ")[1]

                # Print the manufacturer to the text area
                text_area.insert(tk.END, manufacturer + "\n")


# Create an Entry widget to allow user input
network_input = tk.Entry(window)
network_input.insert(0, "192.168.1.0/24")
network_input.pack(fill=tk.X)

# Create a button to start the scan
scan_button = tk.Button(window, text="Scan Network", command=scan_network)
scan_button.pack(fill=tk.X)

# Start the GUI event loop
window.mainloop()
