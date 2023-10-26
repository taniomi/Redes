# echo-server
import socket

HOST = "127.0.0.1" # Same as 'localhost'
PORT = 1025 # Port to listen on, port ∈ [1024, 65535]
server_address = (HOST, PORT)
n = 1024 # byte receive rate

# Create server socket(address family IPv4, socket type TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(server_address)
    s.listen()
    print('Listening...')

    # Create new socket object c to communicate with client
    c, client_address = s.accept()
    with c:
        print(f'Connected by {client_address}')
        while True:
            recv = c.recv(n) # .recv(n bytes)
            print(f"Received from client: {recv!r}")
            c.sendall(recv)
            c.sendall(b'Some message received')
            if not recv:
                break
        print('Closing socket')
        c.close()
