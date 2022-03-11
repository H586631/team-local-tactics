
from multiprocessing import connection
from socket import SOCK_STREAM, socket,AF_INET, SOCK_DGRAM
import os

from time import sleep


serv = "localhost"
port = 9998
address = (serv, port)

sockdb = socket(AF_INET,SOCK_STREAM)
sockdb.bind((serv, port))
sockdb.listen()
conn, address = sockdb.accept()

connect = "Connected to db"
conn.send(connect.encode())

red = 0
blue = 0


while True:
    db_start = open("match_history.txt", "w")
    db_start.close()
    with open("match_history.txt", "r+") as f:
     
     
     new_command = conn.recv(1024).decode()

     if new_command == "b":
        #Add code for adding 1 to blue in history
        print ("Adding 1 to blue history")
        blue += 1
        f.write (str("Red: " + red + " Blue: " + blue))


     elif new_command == "r":
        #Add code for adding 1 to red in history
        print("Adding 1 to red history")
        red += 1
        f.write (str("Red: " + red + " Blue: " + blue))
    
     elif new_command == "send":
        #Add code for sending history
        print("Send history")
        histo = f.read()
        conn.send(histo.encode())
        print("History sent")
       
    
     elif new_command == "erase":
        #Add code to delete history
        print ("Erasing history")
        f.close()
        os.remove("match_history.txt")
        red = 0
        blue = 0




