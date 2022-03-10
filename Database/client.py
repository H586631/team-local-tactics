
from copyreg import pickle
from socket import AF_INET, SOCK_STREAM
import socket
import pickle
import game


servip =  "localhost"
port = 9999
address = (servip, port)

client = socket.socket(AF_INET, SOCK_STREAM)
client.connect(address)
print("Starting up")


new_command = client.recv(1024).decode()







def intro() : 
    print("               Welcome to TNT "           )
    print("            You have three options: "     )
    print("1:        Type 1 to start the game"       )
    print("2:     Type 2 to disconnect from the game")
    print("3:       Type 3 to view match history    ")
    print("")
    
    
    
    
    answer = input("Type here: ").lower()
    if answer == "1" :
        answer = answer.encode()
        client.send(answer)
        print("Starting game")
        game.main()

    elif answer == "2" :
        answer = answer.encode()
        client.send(answer)
        print("Disconnecting from the game")

    elif answer == "3" :
        answer = answer.encode()
        client.send(answer)
        print("Printing match history")
        
    else:
        print("Unknown input")
        intro()


if new_command == "intro":
        intro()





