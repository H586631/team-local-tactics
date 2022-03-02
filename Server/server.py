


from socket import AF_INET, SOCK_STREAM
import socket
import threading


serv = socket.gethostbyname(socket.gethostname())

port = 9999
sock = socket.socket(AF_INET, SOCK_STREAM)
sock.bind(("localhost", 9999 ))
address = ("localhost", port)



def handler( conn, address):

    
    #Send intro message
    connection = True
    introsend = "intro"
    conn.send(introsend.encode())
    print("Intro sent")
    print("")




    while connection == True:


        answer = conn.recv(1024).decode()
        

        if answer == "1":
            #Spillkode
            print("Starting game")
            game()
            break

        elif answer == "3":
            # Hente history fra db
            print("fetching match history")
            hist()
            break

        elif answer == "2":
            # Dissconnect kode
            print("Connection closed with {address}")
            conn.close()
            connection = False
            break
        else:
            print ("Wrong input")
            handler(conn, address)


def starting():
    sock.listen()
    while True:
        conn, address = sock.accept()
        thread = threading.Thread(target=handler, args=(conn, address))
        print("Server is connected")
        thread.start()
        
        



def game ():
    #Here i will implement the game code
    print("Game")






def hist():
    #Here the retrieve history code
    print("History")


















print("Server is starting")
print(f"Server is running on {serv}")
starting()


