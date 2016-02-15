import socket
from multiprocessing import Process

HOST = ''
PORT = 7000
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
    while True:
        try:
            data = client.recv(SIZE)
            if data:
                client.send(data)
            else:
                client.close()
                return
        except:
            client.close()
            return


if __name__ == "__main__":
    main()
