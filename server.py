import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 46673        # Port to listen on (non-privileged ports are > 1023)
ADDR = (SERVER , PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(ADDR)
    s.listen()

    while True:
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('Received', repr(data))
                conn.sendall(data)