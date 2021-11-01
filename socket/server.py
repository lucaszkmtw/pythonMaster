import socket
import threading
import time 

PORT = 5050
HEADER = 64
SERVER = socket.gethostbyname(socket.gethostname( ))
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "usuario desconectado"

server = socket.socket()
server.bind(ADDR)
print(server)
#print(socket.gethostname())   DESKTOP-IQ0UUS5

def handle_client(conn,addr):
    print(f"[NUEVA CONECCION] {addr} connected ")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length= int(msg_length)
            msg =  conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
    conn.close()



def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        t = threading.Thread(target = handle_client, args=(conn,addr))
        t.start()
        print(f"[ACTIVE CONECCIONS] {threading.active_count()-1}")
       

print("[STARTING] server is starting.... ")
start()
