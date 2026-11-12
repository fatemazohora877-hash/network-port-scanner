import socket
import csv
import time
from concurrent.futures import ThreadPoolExecutor

# Get target from user
target = input("Enter IP Address or Hostname: ")

# Resolve hostname
try:
    ip = socket.gethostbyname(target)
    print(f"\nHostname: {target}")
    print(f"Resolved IP: {ip}")
except socket.gaierror:
    print("Error: Could not resolve hostname.")
    exit()

print("-" * 60)
print(f"Scanning {target} ({ip})")
print("-" * 60)

open_ports = []

# Start timer
start_time = time.time()


def grab_banner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        sock.connect((ip, port))

        if port in [80, 8080, 8000]:
            sock.send(b"HEAD / HTTP/1.1\r\nHost: localhost\r\n\r\n")

        banner = sock.recv(1024)

        return banner.decode(errors="ignore").strip()

    except:
        return "No banner available"

    finally:
        sock.close()


def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    try:
        result = sock.connect_ex((ip, port))

        if result == 0:

            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown Service"

            banner = grab_banner(ip, port)

            print(f"\n[+] Port {port} OPEN")
            print(f"    Service: {service}")
            print(f"    Banner : {banner[:100]}")

            open_ports.append([port, service, banner[:100]])

    except:
        pass

    finally:
        sock.close()


# Scan ports 1-1000
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1001))

# Save results to CSV
with open("scan_results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Port", "Service", "Banner"])

    for result in sorted(open_ports):
        writer.writerow(result)

# End timer
end_time = time.time()
scan_duration = end_time - start_time

print("\n" + "-" * 60)
print("SCAN COMPLETE")
print("-" * 60)

print(f"Open Ports Found: {len(open_ports)}")
print(f"Scan Time: {scan_duration:.2f} seconds")
print("Results saved to scan_results.csv")

print("\nOpen Port Summary:")
for port, service, banner in sorted(open_ports):
    print(f"Port {port:<5} -> {service}")