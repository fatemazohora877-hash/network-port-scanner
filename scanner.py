import socket
import time
from concurrent.futures import ThreadPoolExecutor

# Get target from user
target = input("Enter IP Address or Hostname: ")

# Resolve hostname to IP
try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Error: Unable to resolve hostname.")
    exit()

print("-" * 50)
print(f"Scanning {target} ({ip})")
print("-" * 50)

start_time = time.time()

open_ports = []


def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((ip, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = "Unknown Service"

            print(f"[+] Port {port:<5} OPEN ({service})")
            open_ports.append((port, service))

    except Exception:
        pass

    finally:
        sock.close()


# Scan ports 1-1000
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1001))

end_time = time.time()

print("\n" + "-" * 50)
print(f"Open Ports Found: {len(open_ports)}")
print(f"Scan completed in {end_time - start_time:.2f} seconds")
print("-" * 50)

# Display summary
if open_ports:
    print("\nOpen Port Summary:")
    for port, service in sorted(open_ports):
        print(f"Port {port:<5} -> {service}")
else:
    print("No open ports found.")