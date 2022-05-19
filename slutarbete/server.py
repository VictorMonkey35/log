import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="victorsdatabas"
)

mycursor = mydb.cursor()

print("Uppkopplad till databasen!")


import time as t
from socket import *

def start_server():
    s = socket()
    host = "localhost"
    port = 12345
    s.bind((host, port))
    s.listen()
    return s

def threaded_client(conn):
    a = conn.recv(1024)
    msg = a.decode("utf-16")
    print(msg)
    makesure = msg.split()

    if len(makesure) == 4:
        sql = 'INSERT INTO `users` (`UserName`, `Firstname`, `Surname`, `Password`) VALUES (%s, %s, %s, %s)'
        val = (makesure[0], makesure[1], makesure[2], makesure[3])
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        # Läsa från databasen
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

        msg = 'AccountCreated'
        for i in connections:
            i.send(msg.encode('utf-16'))

        threaded_client(conn)

from _thread import *
s = start_server()

ThreadCount = 0
connections = []

while True:
    print("Väntar på att en klient ska ansluta till servern...")
    conn, address = s.accept()
    print("En ny klient anslöt: " + address[0] + ':'
          + str(address[1]))
    start_new_thread(threaded_client, (conn, ))
    ThreadCount += 1
    connections.append(conn)
    print("Tråd nummer: " + str(ThreadCount))

input()