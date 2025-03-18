# Simple Port Scanner
# Author: ACL
# Description: Scans open ports on a given target.
# Date: 2025

import socket

def scan_port(target, port):
    """Scans a single port on a target machine. (ACL)"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))  # Returns 0 if port is open
            if result == 0:
                print(f"[+] Port {port} is open on {target}")
            else:
                print(f"[-] Port {port} is closed on {target}")
    except Exception as e:
        print(f"[!] Error scanning port {port}: {e}")

def main():
    target = input("Enter target IP or domain: ")  # Fixed input prompt
    ports = [22, 80, 443, 8080]  # Common ports
    for port in ports:
        scan_port(target, port)  # Fixed function call

if __name__ == "__main__":
    main()
