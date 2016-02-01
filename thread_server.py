import socket
from multiprocessing import Process

HOST = ''
PORT = 8005
BACKLOG = 5
SIZE = 1024

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket IP V4 using TCP
    server.bind((HOST,PORT))
    server.listen(BACKLOG)
    numClient = 0;
    while 1:
        client, address = server.accept()
        numClient = numClient + 1
        print numClient, 'Connection Established With:', address
        process = Process(target=worker, args=(client,))
        process.start()

def worker(client):
    data = client.recv(SIZE)
    if data:
        client.send(data)
    client.close()


if __name__ == "__main__":
    main()
