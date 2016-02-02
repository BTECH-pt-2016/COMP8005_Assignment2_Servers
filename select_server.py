import socket
import select
import sys
import cProfile


HOST = ''
PORT = 8005
BACKLOG = 5
SIZE = 1024

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket IP V4 using TCP
    server.bind((HOST,PORT))
    server.listen(BACKLOG)
    input = [server,sys.stdin]
    numClient = 0
    running = 1
    while running:
        inputready,outputready,exceptready = select.select(input,[],[])
        for s in inputready:
            print i
            if s == server:
                client, address = server.accept()
                numClient = numClient + 1
                print numClient, 'Connection Established With:', address
                client.setblocking(0)
                input.append(client)
        
            elif s == sys.stdin:
                # ENDS LOOP
                junk = sys.stdin.readline()
                running = 0
        
            else:# hundle sockets all other sockets
                data = s.recv(SIZE)
                if data:
                    s.send(data)
                    print 'removing socket'
                    s.close()
                    input.remove(s)
    server.close()


if __name__ == "__main__":
    main()
