import socket, threading

server_socket = socket.socket()
server_socket.bind(('', 3000))

server_socket.listen()

def handle_client(ss: socket):
    try:
        response = ss.recv(1024).decode()
        print(f'Received: {response}')
    except Exception as e:
        print(e)
        ss.close()
        
while True:
    conn, address = server_socket.accept()
    print(f'Connection from: {address}')

    thread = threading.Thread(target=handle_client, args=(conn,))
    thread.start()