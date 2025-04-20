# server.py
import socket

HOST = '127.0.0.1'  # Localhost
PORT = 9999         # Port to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"[+] Server listening on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"[+] Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"[Client]: {data}")
    response = input("[You]: ")
    conn.send(response.encode())

conn.close()
