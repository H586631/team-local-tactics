


from socket import AF_INET, SOCK_STREAM
import socket
import threading
import pickle


serv = socket.gethostbyname(socket.gethostname())

port = 9999

serv = "localhost"
address = (serv, port)


sock = socket.socket(AF_INET, SOCK_STREAM)
sockdb = socket.socket(AF_INET, SOCK_STREAM)
sock.bind((address))
sockdb.bind((serv, 9998 ))




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
            

        elif answer == "3":
            # Hente history fra db
            print("fetching match history")
            hist()
            

        elif answer == "2":
            # Dissconnect kode
            print("Connection closed with {address}")
            conn.close()
            connection = False
            
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

def startdb():
    sockdb.listen
    while True:
        conn, address = sockdb.accept()
        thread = threading.Thread()
        print("Server connected with DB")
        thread.start
    
        
        



def game ():
    #Here i will implement the game code from serverside
    print("Game")








def hist():
    #Here the retrieve history code from serverside
    print("History")





print("Server is starting")
print(f"Server is running on {serv}")
print("Connect server with db")
startdb()



