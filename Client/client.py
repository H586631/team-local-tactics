
import 
from copyreg import pickle
from socket import AF_INET, SOCK_STREAM
import socket
import pickle


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
        game_start()
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
else: 
    print("Unknown sentence")


def game_start() :

    while True: 

        data,_ = client.recvfrom()
        champs = pickle.loads(data)
        Database.game.print_available_champs(pickle.loads(data))
        player=[]


        champ = input("Choose your Champion:"  )
        if champ in player:
            print ("You have already chosen that champion")
        elif champ not in champs:
            print ("Not a valid champion")
        else:
            player.append(champ)
            if len(player)==2:
                break




    for i in range(2):
        client.sendto(player[i].encode(),(("Localhost",5555)))


