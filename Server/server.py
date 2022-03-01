
from ast import Break, While
from socket import AF_INET, SOCK_STREAM
import socket
from threading import Thread, activeCount
import threading


sock = socket.socket(AF_INET, SOCK_STREAM)
sock.bind(("localhost", 9999 ))
sock.listen()



def handler(conn, address):
    
    print(f"Server is connected with" '{address}')
    conn.send(str.encode("Connected to server"))
    
    connection = True
    while connection == True:
        inputs = conn.recv(9999).decode

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


def start():
    while True:
        conn, address = socket.socket.accept()
        thread = threading.Thread(target=handler, args=(conn, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")




