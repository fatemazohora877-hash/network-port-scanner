import socket

# Get target from user
target = input("Enter IP Address or Hostname: ")

# Resolve hostname to IP address
try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Error: Unable to resolve hostname.")
    exit()

print("-" * 50)
print(f"Scanning {target} ({ip})")
print("-" * 50)

# Scan ports 1-100
for port in range(1, 101):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((ip, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "Unknown Service"

        print(f"[+] Port {port} OPEN ({service})")

    sock.close()

print("-" * 50)
print("Scan Complete!")