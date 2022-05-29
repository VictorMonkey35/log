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
    
    if len(makesure) == 2:
        query = ("SELECT ID FROM users WHERE UserName = %s and Password = %s")
        mycursor.execute(query,(makesure[0], makesure[1],))
        account = mycursor.fetchone()
        if account:
            msg = str(account)
            msg = msg.replace('(','')
            msg = msg.replace(',','')
            msg = msg.replace(')','')
            print(msg)
            for i in connections:
                i.send(msg.encode('utf-16'))
        else:
            msg = 'NotLoggedIn'
            for i in connections:
                i.send(msg.encode('utf-16'))
        
    if len(makesure) == 8:
        sql = 'INSERT INTO `flights` (`ID`, `toCity`, `fromCity`, `time`, `month`, `date`, `klass`, `price`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        val = (makesure[0], makesure[1], makesure[2], makesure[3],makesure[4], makesure[5], makesure[6], makesure[7])
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        # Läsa från databasen
        mycursor.execute("SELECT * FROM flights")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        

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