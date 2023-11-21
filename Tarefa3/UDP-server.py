import socket

def run_server():
    server_ip = '127.0.0.1'
    port = 8080

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('[START] Server starting')
    server.bind((server_ip, port))
    server.listen(5)
    print(f'[LISTEN] Server listening on {server_ip}:{port}')

    while True:
        client_socket, addr = server.accept()
        print(f'[CONNECT] Accepted connection from {addr[0]}:{addr[1]}')

        # Create a new thread for each client connection
        client_thread = threading.Thread(target=handle_http_request, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    run_server()
