import socket
import threading
import tkinter as tk
from tkinter import messagebox, scrolledtext

# Function to scan ports
def scan_ports(target, start_port, end_port, output_box):
    try:
        ip = socket.gethostbyname(target)  # Resolve hostname to IP
    except socket.gaierror:
        output_box.insert(tk.END, "Invalid hostname.\n")
        return

    output_box.insert(tk.END, f"Scanning {ip} from port {start_port} to {end_port}...\n")
    output_box.update()  # Ensure the output box updates immediately

    # Loop through port range and check each port
    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Set timeout for connection attempt
            result = sock.connect_ex((ip, port))
            if result == 0:
                output_box.insert(tk.END, f"Port {port} is OPEN\n")  # Open port
            else:
                output_box.insert(tk.END, f"Port {port} is CLOSED\n")  # Closed port
            sock.close()
            output_box.update()  # Update GUI after each port check
        except Exception as e:
            output_box.insert(tk.END, f"Error on port {port}: {e}\n")
            output_box.update()  # Update on error

    output_box.insert(tk.END, "Scan complete.\n")
    output_box.update()  # Final update to show scan completion

# Function to start scanning in a new thread
def start_scan():
    target = target_entry.get()
    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid port numbers.")
        return

    output_box.delete(1.0, tk.END)  # Clear the output box before starting a new scan
    scan_thread = threading.Thread(target=scan_ports, args=(target, start_port, end_port, output_box))
    scan_thread.start()

# Tkinter GUI setup
app = tk.Tk()
app.title("Live Port Scanner 💻")
app.geometry("500x400")
app.resizable(False, False)

# Target IP/Hostname input
tk.Label(app, text="Target IP / Hostname:").pack()
target_entry = tk.Entry(app, width=50)
target_entry.pack(pady=5)

# Start Port input
tk.Label(app, text="Start Port:").pack()
start_port_entry = tk.Entry(app, width=20)
start_port_entry.pack(pady=2)

# End Port input
tk.Label(app, text="End Port:").pack()
end_port_entry = tk.Entry(app, width=20)
end_port_entry.pack(pady=2)

# Start Scan button
scan_button = tk.Button(app, text="Start Scan", command=start_scan)
scan_button.pack(pady=10)

# Scrolled Text Box for output
output_box = scrolledtext.ScrolledText(app, width=60, height=15)
output_box.pack(padx=10, pady=10)

# Start the GUI loop
app.mainloop()
