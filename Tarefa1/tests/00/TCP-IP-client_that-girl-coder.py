# TCP client
import socket

# Server address = (host, port), port ∈ [1024, 65535]
server_address = ('localhost', 1024)

# Set up a TCP client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect(server_address)

    send = str.encode('Hi. I am a TCP client sending data to a TCP server!')
    s.sendall(send)

    recv = s.recv(32)

    print('Closing socket')
    s.close()

print(f"Received {recv!r}")
