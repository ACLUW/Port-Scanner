# Port Scanner

A simple Python-based port scanner that helps you check open ports on a given target. This tool is great for basic network security assessments.

## Features:
- Scans common ports: 22 (SSH), 80 (HTTP), 443 (HTTPS), 8080 (HTTP Proxy)
- Checks if the port is open or closed
- Easy to use with input for target IP or domain

## Requirements:
- Python 3.x
- `socket` module (included with Python)

## Installation:
1. Clone this repository:
    ```bash
    git clone https://github.com/ACLUW/Port-Scanner.git
    ```

2. Navigate to the project directory:
    ```bash
    cd Port-Scanner
    ```

3. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - Windows:  
      ```bash
      venv\Scripts\activate
      ```

5. Run the `port_scanner.py` script:
    ```bash
    python port_scanner.py
    ```

6. Enter the target IP or domain when prompted.

## Usage:
The script will prompt you to enter the target IP or domain. It will then scan common ports (22, 80, 443, 8080) and display whether each port is open or closed.

## License:
This project is open-source. You can freely use and modify it under the terms of the MIT License.

## Author:
ACL (Chidera Louis Andy)
