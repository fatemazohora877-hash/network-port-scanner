import socket
import time
from concurrent.futures import ThreadPoolExecutor

target = input("Enter IP Address or Hostname: ")

# Resolve hostname
try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Error: Unable to resolve hostname.")
    exit()

print("-" * 60)
print(f"Scanning {target} ({ip})")
print("-" * 60)

open_ports = []
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

            open_ports.append((port, service))

    except:
        pass

    finally:
        sock.close()


with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1001))

end_time = time.time()

print("\n" + "-" * 60)
print("SCAN COMPLETE")
print("-" * 60)

if open_ports:
    print("\nOpen Ports Found:")

    for port, service in sorted(open_ports):
        print(f"Port {port:<5} -> {service}")

else:
    print("No open ports found.")

print(f"\nTotal Open Ports: {len(open_ports)}")
print(f"Scan Time: {end_time - start_time:.2f} seconds")