from concurrent.futures import thread
import socket as so
import _thread as th


def start_server():
    s = so.socket()
    host = "10.32.38.230"
    port = 12345
    s.bind((host, port))
    s.listen()
    return s

def threaded_client(conn):

    try:
        a = conn.recv(1024)
        msg = a.decode("utf-32")
        print(msg)
        for i in connections:
            if i  == conn:
                pass
            else:
                i.send(msg.encode('utf-32'))

    except:
        pass

    threaded_client(conn)

s = start_server()
ThreadCount = 0
connections = []

while ThreadCount < 2:
    print("Väntar på att en klient ska ansluta till servern...")
    conn, address = s.accept()
    print("En ny klient anslöt: " + address[0] + ':'
          + str(address[1]))
    th.start_new_thread(threaded_client, (conn, ))
    ThreadCount += 1
    connections.append(conn)
    print(connections)
    print("Tråd nummer: " + str(ThreadCount))

input()