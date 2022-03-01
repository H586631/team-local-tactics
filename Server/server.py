

from socket import AF_INET, SOCK_STREAM
import socket
import threading

serv = socket.gethostbyname(socket.gethostname())

port = 9999
sock = socket.socket(AF_INET, SOCK_STREAM)
sock.bind(("localhost", 9999 ))
address = (serv, port)



def handler(conn, address):

    conn.send(str.encode("Connected to server")) #Fucker denne opp??
    
    connection = True
    while connection == True:
        inputs = conn.recv(5015)
        inputs = inputs.decode

        if inputs == "start":
            #Spillkode
            print("blabla")

        elif inputs == "history":
            # Hente history fra db
            print("fetching match history")

        elif inputs == "disconnect":
            # Dissconnect kode
            print("Connection closing")
            conn.close()
            connection = False
            break
        else:
            print ("Wrong input")


def start():
    sock.listen()
    while True:
        conn, address = sock.accept()
        thread = threading.Thread(target=handler, args=(conn, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("Server is starting")
print(f"Server is running on {serv}")
start()




