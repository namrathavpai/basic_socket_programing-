import socket

CLIENT = socket.gethostbyname(socket.gethostname())
PORT = 46673
ADDR = (CLIENT , PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.connect(ADDR)
    c.send(f'hello'.encode())
    data = c.recv(1024)
    print(f'Client  Received {repr(data)}')