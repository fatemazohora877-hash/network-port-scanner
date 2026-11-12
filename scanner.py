import socket

target = input("Target IP: ")

print("-" * 40)
print(f"Scanning {target}")
print("-" * 40)

for port in range(1, 101):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[+] Port {port} OPEN")

    sock.close()