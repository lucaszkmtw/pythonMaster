import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.100.4"
ADDR = (SERVER, PORT)

client = socket.socket()
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
  

send("Hello World!")

send("Hello Everyone!")

send("Hello Tim!")
send(DISCONNECT_MESSAGE)