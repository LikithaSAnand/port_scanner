# Port Scanner with GUI

A Python-based port scanner with a user-friendly Tkinter GUI that scans for open ports on a given IP address.  
It uses multithreading for faster scanning and displays the open ports in real-time.

---

## Features

- Scan ports within a user-specified range on any target IP  
- Multithreaded scanning for speed  
- Real-time results displayed in a scrollable window  
- Simple and lightweight with no external dependencies

---

## Theory

A **port scanner** is a tool used to probe a server or host for open ports. Ports are communication endpoints that allow different services and applications to communicate over a network. Open ports indicate that a service is listening and available on that port.

The port scanner works by attempting to establish a TCP connection to each port in the specified range on the target IP address. If the connection is successful (i.e., the port is open), the port number is reported as open.

This project uses Python’s `socket` module to create TCP connection attempts and `threading` to scan multiple ports concurrently, which speeds up the scanning process significantly.

The GUI built with Tkinter allows users to easily input the target IP and port range and view scanning results in real time, making the tool both practical and accessible for beginners in network security.

---

## Requirements

- Python 3.x (no external libraries needed)

---

## How to Run

1. Clone the repository or download the `port_scanner_gui.py` file.  
2. Run the script using the command:
   ```bash
   python port_scanner_gui.py
