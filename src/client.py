
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
    print("3:       Type 3 to view match history  (Faulty)  ")
    print("4:       Type 4 to erase match history    ")
    print("")
    
    
    
    
    answer = input("Type here: ").lower()
    if answer == "1" :
        answer = answer.encode()
        client.send(answer)
        print("Starting game")
        main_game()

    elif answer == "2" :
        answer = answer.encode()
        client.send(answer)
        print("Disconnecting from the game")

    elif answer == "3" :
        answer = answer.encode()
        client.send(answer)
        print("Printing match history")
        print(client.recv(1024).decode())
        print("")
        intro()

    elif answer == "4" :
        answer = answer.encode()
        client.send(answer)
        print("Erasing match history")
        intro()
        
    else:
        print("Unknown input")
        intro()

def main_game() -> None:

     print('\n'
          'Welcome to [bold yellow]Team Local Tactics[/bold yellow]!'
          '\n'
          'Each player choose a champion each time.'
          '\n')

     champions = game.load_some_champs()
     game.print_available_champs(champions)
     print('\n')

     player1 = []
     player2 = []

    # Champion selection
     for _ in range(2):
        game.input_champion('Player 1', 'red', champions, player1, player2)
        game.input_champion('Player 2', 'blue', champions, player2, player1)

     print('\n')

    # Match
     match = game.Match(
        game.Team([champions[name] for name in player1]),
        game.Team([champions[name] for name in player2])
    )
     match.play()

     # Print a summary
     game.print_match_summary(match)

      #Send Result to Server
     result = game.print_match_summary(match)
     resultpick = pickle.dumps(result)
     client.send(resultpick)
     


     #Ask for replay
     for x in range (99) :
        replay = input("Type 1 to play again, Type 2 to stop playing: ")
        if replay == "1":
         client.send(replay.encode())
         main_game()
         break
        elif replay == "2":
         client.send(replay.encode())
         print("Thank you for playing TNT")
         break
        elif x == 98:
            print("You have tried too many times. The application will now close")
            client.send(replay.encode())
            break

        else: 
            print("Unkown input, try again ")


     
    

    


if new_command == "intro":
        intro()





