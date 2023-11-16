import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def run_server():
    server_ip = '127.0.0.1'
    port = 5050

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, port))
    server.listen(5)

    print(f'Server is listening on {server_ip}:{port}')

    while True:
        client_socket, addr = server.accept()
        print(f'Accepted connection from {addr[0]}:{addr[1]}')

        # Create a new thread for each client connection
        client_thread = threading.Thread(target=handle_http_request, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    run_server()
