
from socket import socket,AF_INET, SOCK_DGRAM
import champlistloader
import pickle


serv = "localhost"
port = 9999
address = (serv, port)

sock = socket(AF_INET,SOCK_DGRAM)
sock.connect((address))
data = champlistloader.load_some_champs()

while True:
    req = sock.recvfrom(2048).decode
    if req == "champs":
        sock.sendto(pickle.dumps(data),((address)))

