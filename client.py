# client.py
import socket

HOST = '127.0.0.1'  # Server's hostname or IP address
PORT = 9999         # Port used by the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"[+] Connected to server at {HOST}:{PORT}")

while True:
    message = input("[You]: ")
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(f"[Server]: {data}")

client_socket.close()
