import socket, json

PORT = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))

s.listen()

print(f'Listening in on port: {PORT}')

while True:
    conn, address = s.accept()
    print(f'Connection address: {address}')

    response = conn.recv(1024).decode()

    if response:
        data = response.split('\r\n').pop()
        print(json.loads(data))

        conn.send(b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 2\r\n\r\nOK')

        conn.close()