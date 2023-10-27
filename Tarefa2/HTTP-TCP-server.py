
import socket
import os

def handle_http_request(client_socket):
    request = client_socket.recv(1024).decode('utf-8')

    if not request:
        return

    method, path = request.split('\n')[0].split()[:2]

    if method == 'GET' and path.startswith('/images/'):
        image_path = path[1:]  # Remove the leading '/'
        image_path = os.path.join(image_path)  # Combine with the images directory

        print(f"Requested image: {image_path}")  # Debugging line

        try:
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()
            content_type = 'image/jpeg'  # Adjust for other image types

            response = f'HTTP/1.1 200 OK\nContent-Type: {content_type}\n\n'.encode('utf-8') + image_data
            client_socket.send(response)
        except FileNotFoundError:
            print(f"Image not found: {image_path}")  # Debugging line
            response = 'HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n404 - Image Not Found'
            client_socket.send(response.encode('utf-8'))
    else:
        response = 'HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n404 - Page Not Found'
        client_socket.send(response.encode('utf-8'))

    client_socket.close()

def run_server():
    server_ip = '127.0.0.1'
    port = 8000

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, port))
    server.listen(5)

    print(f'Server is listening on {server_ip}:{port}')

    while True:
        client_socket, addr = server.accept()
        print(f'Accepted connection from {addr[0]}:{addr[1]}')
        handle_http_request(client_socket)

if __name__ == '__main__':
    run_server()
