from socket import *
from threading import Thread
from time import ctime

# To hold clients
mydict={}
class ClientHandler(Thread):

    def __init__(self,client,address):
        global sockets
        global addresses
        Thread.__init__(self)
        self._client = client
        self._address = address
        sockets.append(self._client)
        addresses.append(self._address)

    def run(self):
        self._client.send(str.encode("Waiting for Clients : "))
        clientname = self._client.recv(BUFSIZE)
        clientname = clientname.decode()
        mydict[clientname] = self._address
        self._client.send(str.encode("Hi"))
        print(mydict)
        message =self._client.recv(BUFSIZE) # Wait for ONLINE message
        message = message.decode()
        if not message:
            print ("Client disconnected.")
            addIndex=sockets.index(self._client)
            del sockets[addIndex]
            del addresses[addIndex]
            self._client.close()
        else:
            if "ONLINE#" in message: # if client online
                while True:
                    data = self._client.recv(BUFSIZE)
                    for x in sockets:
                        if (x!=self._client):
                             # Send data from one client to other
                            if data:
                                x.send(data)
                                print("Sending ... ")
                else:
                    self._client.close()
                                

HOST = '127.0.0.1'
PORT = 1233

ADDRESS = (HOST,PORT)
BUFSIZE = 1024
server = socket(AF_INET,SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)
sockets=[]
addresses=[]

while True:
    print ("Waiting for connection...")
    client, address = server.accept()
    print('...client connected from: ',address)
    handler = ClientHandler(client,address)
    handler.start()
server.close()
