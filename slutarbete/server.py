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
    try:
        msg = ''
        a = conn.recv(1024)
        msg = a.decode("utf-16")
        print(msg)
        makesure = msg.split()
        
        #tar bort flight från databasen
        if len(makesure) == 1:
            sql = 'DELETE FROM `flights` WHERE `flights`.`ID` = %s'
            val = []
            val.append(makesure[0])
            mycursor.execute(sql, val)
            mydb.commit()
        
        #loggar in
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
                conn.send(msg.encode('utf-16'))

            else:
                msg = 'NotLoggedIn'
                conn.send(msg.encode('utf-16'))

        #ger flight info
        if len(makesure) == 3:
            print(makesure)
            msg = ''
            sql = "SELECT * FROM flights WHERE user = %s"
            val = []
            val.append(makesure[1])
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
                msg += (' ' + str(x))
            msg = msg.replace(')','')
            msg = msg.replace(',','')
            conn.send(msg.encode('utf-16'))

        #skapar nytt konto på databasen
        if len(makesure) == 4:
            sql = 'INSERT INTO `users` (`UserName`, `Firstname`, `Surname`, `Password`) VALUES (%s, %s, %s, %s)'
            val = (makesure[0], makesure[1], makesure[2], makesure[3])
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            msg = 'AccountCreated'
            conn.send(msg.encode('utf-16'))
            
        #ger flight info till admin
        if len(makesure) == 5:
            msg = ''
            mycursor.execute("SELECT * FROM flights")
            myresult = mycursor.fetchall()
            for x in myresult:
                msg += (' ' + str(x))
            msg = msg.replace(')','')
            msg = msg.replace(',','')
            conn.send(msg.encode('utf-16'))
        
        #ger profli info
        if len(makesure) == 6:
            msg = ''
            sql = "SELECT * FROM users WHERE ID = %s"
            val = []
            val.append(makesure[5])
            mycursor.execute(sql, val)
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
                msg += (' ' + str(x))
            msg = msg.replace(')','')
            msg = msg.replace(',','')
            conn.send(msg.encode('utf-16'))

        #ger profil info till admin
        if len(makesure) == 7:
            msg = ''
            mycursor.execute("SELECT * FROM users")
            myresult = mycursor.fetchall()
            for x in myresult:
                msg += (' ' + str(x))
            msg = msg.replace(')','')
            msg = msg.replace(',','')
            conn.send(msg.encode('utf-16'))

        #bokar ny flight till databasen
        if len(makesure) == 8:
            sql = 'INSERT INTO `flights` (`user`, `toCity`, `fromCity`, `time`, `month`, `date`, `klass`, `price`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            val = (makesure[0], makesure[1], makesure[2], makesure[3],makesure[4], makesure[5], makesure[6], makesure[7])
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            # Läsa från databasen
            mycursor.execute("SELECT * FROM flights")
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
        
        #Tar bort specificerad användare från databasen
        if len(makesure) == 9:
            print(makesure[0])
            if makesure[0] == 16:
                pass
            else:
                sql = 'DELETE FROM `users` WHERE `users`.`ID` = %s'
                val = []
                val.append(makesure[0])
                print(val)
                mycursor.execute(sql, val)
                mydb.commit()
                print(makesure[0])

                #om användaren försvinner bör även dess bokningar försvinna. Vilket sker nedan.
                sql = 'DELETE FROM `flights` WHERE `flights`.`user` = %s'
                val = []
                val.append(makesure[0])
                mycursor.execute(sql, val)
                mydb.commit()

        threaded_client(conn)
    except:
        pass

ThreadCount = 0
connections = []

from _thread import *
s = start_server()

while True:
    print("Väntar på att en klient ska ansluta till servern...")
    conn, address = s.accept()
    print("En ny klient anslöt: " + address[0] + ':'
    + str(address[1]))
    ThreadCount += 1
    connections.append(conn)
    start_new_thread(threaded_client, (conn, ))
    print("Tråd nummer: " + str(ThreadCount))

input()