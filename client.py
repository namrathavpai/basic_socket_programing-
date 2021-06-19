import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 46673
ADDR = (SERVER , PORT)

csFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
csFT.connect(ADDR)

text_file = 'send.txt'

# Send file
with open(text_file, 'rb') as fs:
    # Using with, no file close is necessary,
    # with automatically handles file close
    csFT.send(b'BEGIN')
    while True:
        data = fs.read(1024)
        print('Sending data', data.decode('utf-8'))
        csFT.send(data)
        print('Sent data', data.decode('utf-8'))
        if not data:
            print('Breaking from sending data')
            break
    csFT.send(b'ENDED')
    fs.close()
csFT.close()