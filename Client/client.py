
from socket import AF_INET, SOCK_STREAM
import socket


servip =  "localhost"
port = 9999
address = (servip, port)

client = socket.socket(AF_INET, SOCK_STREAM)
client.connect(address)
print("Starting up")
new_command = client.recv(1024).decode()






def intro() : 
    print("               Welcome to TNT ")
    print("            You have three options: ")
    print("1:        Type start to start the game")
    print("2: Type disconnect to disconnect from the game")
    print("3:    Type history to view match history")
    answer = input().lower()
    answer = answer.encode()
    client.send(answer, address)


if new_command == "intro":
        intro()
else: 
    print("Unknown sentence")





