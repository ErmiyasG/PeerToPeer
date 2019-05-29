import sys
import socket
import threading
import time
from random import randint

class Server:
    connections = []
    peers = []
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind('0.0.0.0', 10000)
        sock.listen(1)
        print("Server Running........")
        
        while True:
                c, a = sock.accept()
                cThread = threading.Thread(target=self.handler, args=(c,a))
                cThread.deamon = True
                cThread.start()
                self.connections.append(c)
                self.peers.append(a[0])
                print(str(a[0] + ':' + str(a[1])), 'Connected')
                self.sendPeers()


        def handler(self, c, a):
            while True:
                data = c.recv(1024)
                for connection in connections:
                    connection.send(data)
                    if not data:
                        print(str(a[0] + ':' + str(a[1])), 'Disconnected')
                        self.conections.remove(c)
                        self.peers.remove(a[0])
                        c.close()
                        self.sendPeers()
                        break

        def sendPeers(self):
            p = ""
            for peer in self.peers:
                p = p + ","
            for connection in connections:
                    connection.send(b'\x11' + bytes(p, 'utf-8'))
class Client:

    def sendMsg(self, sock):
        while True:
            sock.send(bytes(input(""), 'utf-8'))

        def __init__(self, address):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((address, 10000))
            
            iThread = threading.Thread(target=self.sendMsg, args=(sock,))
            Thread.deamon = True
            iThread.start()

            while True:
                data = sock.recv(1024)
                if not data:
                    break
                if data[0:1] == b'\x11':
                    self.updatePeers(data[1:])
                else:
                    print(str(data, 'utf-8'))

        def updatePeers(self, peerData):
            p2p.peers = str(peerData, 'utf-8').split(",")[:-1]

class p2p:
    peers = ['127.0.0.1']


while True:
    try:
        print("Trying To connect......")
        time.sleep(randint(1,5))
        for peer in p2p.peers:
            try:
                client = Client(peer)
            except keyboadInterrupt:
                sys.exit(0)
            except:
                pass
            try:
                server = Server()
            except keyboadInterrupt:
                sys.exit(0)
                print("Couldn't  start the server")
                
    except keyboadInterrupt:
        sys.exit(0)
