import socket

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 46673        # Port to listen on (non-privileged ports are > 1023)
ADDR = (SERVER , PORT)
ssFT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssFT.bind(ADDR)
ssFT.listen(1)

while True:
    (conn, address) = ssFT.accept()
    text_file = 'fileProj.txt'

    # Receive, output and save file
    with open(text_file, "wb") as fw:
        print("Receiving..")
        while True:
            print('receiving')
            data = conn.recv(32)
            if data == b'BEGIN':
                continue
            elif data == b'ENDED':
                print('Breaking from file write')
                break
            else:
                print('Received: ', data.decode('utf-8'))
                fw.write(data)
                print('Wrote to file', data.decode('utf-8'))
        fw.close()
        print("Received..")
    break
ssFT.close()


