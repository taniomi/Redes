# TCP server
import socket

# Server address = (host, port), port ∈ [1024, 65535]
server_address = ('localhost', 1024)

# Set up a TCP server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 

    s.bind(server_address)
    s.listen(1)
    print('Waiting for connection')

    # Create socket object to communicate with client
    connection, client = s.accept()

    with connection:
        print(f'Connected to client IP: {client}')

        # Receive and print data 32 bytes at a time, while the client is sends
        while True:
            recv = connection.recv(32)
            print(f'Received data: {recv}')

            if not recv:
                break
            connection.sendall(b'Message received')
        connection.close()
