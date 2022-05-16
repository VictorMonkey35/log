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
    """sql = 'INSERT INTO `users` (`UserName`, `Firstname`, `Surname`, `Password`) VALUES (%s, %s, %s, %s)'
        val = (username.get(), fname.get(), lname.get(), password.get())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        # Läsa från databasen
        mycursor.execute("SELECT * FROM users")
        myresult = mycursor.fetchall()
        loginscreen()
        for x in myresult:
            print(x)"""
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