


from socket import AF_INET, SOCK_STREAM
import socket
import threading
import pickle
from time import sleep




port = 9999
portdb = 9998

serv = "localhost"
address = (serv, port)
sock = socket.socket(AF_INET, SOCK_STREAM)
sock.bind((address))








def handler(conn, address, sockdb, portdb):



    
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
            game(conn)
            break

        elif answer == "2":
            # Dissconnect kode
            print("Connection closed with client")
            conn.close()
            connection = False
        
            

        elif answer == "3": #Faulty
            # Hente history fra db
            print("fetching match history")
            sockdb.send("send".encode())
            print("Command sent to Db")
            print(sockdb.recv(1024).decode())
            print ("History sent to client")
            # print(histo)
            # conn.send(histo.encode())

            
        elif answer == "4":
            # Dissconnect kode
            print("Erasing match history")
            sockdb.send("erase".encode())
            
    
        else:
            print ("Wrong input")
            handler(conn, address)


def starting():
    
    sock.listen()
    

    while True:
        conn, address = sock.accept()
        thread = threading.Thread(target=handler, args=(conn, address, sockdb, portdb))
        print("Server is connected to client and database")
        thread.start()
       
        



def game (conn):

    print("")


    resultpick = conn.recv(1025)
    result = pickle.loads(resultpick)

    if result == "draw" :
            print("Result recieved, draw")
            answer = conn.recv(1024).decode()
            if answer == "1":
                print("Starting game")
                game(conn)
            else: 
                print("Connection closed with client")
                conn.close()
                



            

    elif result == "red" :
            print("Result recieved, red win")
            sockdb.send("r".encode())
            answer = conn.recv(1024).decode()
            if answer == "1":
                print("Starting game")
                game(conn)
            else: 
                print("Connection closed with client")
                conn.close()
        
    elif result == "blue" :
            print("Result recieved, blue win")
            sockdb.send("b".encode())
            answer = conn.recv(1024).decode()
            if answer == "1":
                print("")
                print("Starting game")
                game(conn)
            else: 
                print("Connection closed with client")
                conn.close()
    else : 
        print("No Answer recieved")




print("Server is starting")
print(f"Server is running on {serv}")


# Connect to database 
print("Trying to connect to database")
sockdb = socket.socket(AF_INET, SOCK_STREAM)
sockdb.connect((serv, 9998))  
print(sockdb.recv(1024).decode())


starting()



