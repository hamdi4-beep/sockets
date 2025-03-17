import socket

PORT = 3000

s = socket.socket()
s.bind(('', PORT))

s.listen()

print(f'Listening in on port {PORT}')

while True:
    conn, address = s.accept()
    print(f'Connected to {address}')

    response = conn.recv(1024).decode()

    if response:
        data = b'This is the operation result.'
        conn.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: ' + f'{len(data)}\r\n\r\n'.encode() + data)

conn.close()