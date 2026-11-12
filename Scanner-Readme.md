Advanced Network Port Scanner
A Python-based multithreaded network port scanner designed to identify open TCP ports, detect running services, perform banner grabbing, and export results to CSV files. This project demonstrates practical cybersecurity, networking, and Python automation skills commonly used in Security Analyst and SOC Analyst roles.

Features
TCP Port Scanning
Multi-threaded Scanning
Hostname Resolution
Service Detection
Banner Grabbing
CSV Report Generation
Scan Performance Timing
Error Handling
Custom Port Range Selection
Command-Line Interface (CLI)
Technologies Used
Python 3
Socket Programming
ThreadPoolExecutor
CSV Module
Argparse
Installation
Clone the repository:

git clone https://github.com/yourusername/network-port-scanner.git
cd network-port-scanner
Usage
Scan a target using the default port range:

python scanner.py scanme.nmap.org
Scan a custom port range:

python scanner.py scanme.nmap.org --start 1 --end 5000
Scan an IP address:

python scanner.py 192.168.1.1
Example Output
------------------------------------------------------------
Scanning scanme.nmap.org (45.33.32.156)
Port Range: 1-1000
------------------------------------------------------------

[+] Port 22 OPEN
    Service: ssh

[+] Port 80 OPEN
    Service: http

------------------------------------------------------------
SCAN COMPLETE
------------------------------------------------------------

Open Ports Found: 2
Scan Time: 1.84 seconds
Results saved to scan_results.csv
CSV Report Example
Port,Service,Banner
22,ssh,No banner available
80,http,Apache/2.4.57
Project Structure
network-port-scanner/
│
├── scanner.py
├── scan_results.csv
├── README.md
└── screenshots/
Skills Demonstrated
Network Reconnaissance
TCP/IP Fundamentals
DNS Resolution
Python Automation
Security Assessment
Service Enumeration
Multithreading
Secure Coding Practices
Data Reporting
Future Improvements
UDP Port Scanning
Nmap Integration
GUI Interface
JSON Report Generation
Vulnerability Detection
Logging Support
Real-Time Progress Bar
Disclaimer
This tool is intended for educational purposes and authorized security testing only. Do not scan systems, networks, or services without explicit permission from the owner.

Author
Fatema Tuz Zohora
Cyber Security Student
University of Lancashire