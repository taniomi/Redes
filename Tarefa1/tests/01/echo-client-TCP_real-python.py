# echo-client
import socket

HOST = '127.0.0.1' # Same as 'localhost'
PORT = 1025  # Port used by the server, port ∈ [1024, 65535]
server_address = (HOST, PORT)
n = 1024 # byte receive rate

# Set up TCP socket for client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(server_address)

    send = b'Hello, world!'
    s.sendall(send)
   
    while True:
        recv = s.recv(n) # .recv(n bytes)
        print(f'Received from server: {recv!r}')
        if not recv:
            break
    print('Closing socket')
    s.close()
