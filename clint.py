import socket

CLIENT = socket.gethostbyname(socket.gethostname())
PORT = 46673
ADDR = (CLIENT , PORT)

for i in range(2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
        msg = f'Hello from client:{i}'
        c.connect(ADDR)
        c.sendall(msg.encode())
        data = c.recv(1024)