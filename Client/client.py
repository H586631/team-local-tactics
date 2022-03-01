
from socket import AF_INET, SOCK_STREAM
import socket
import threading

servip =  "102.168.1.52"
port = 9999
address = (servip, port)

# client = socket.socket(AF_INET, SOCK_STREAM)
# client.connect(address)

def intro() : 
    print("               Welcome to TNT ")
    print("            You have three options: ")
    print("1:        Type start to start the game")
    print("2: Type disconnect to disconnect from the game")
    print("3:    Type history to view match history")
    ans = input()
    client.send(str.encode(ans))


intro()  





