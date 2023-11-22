import socket
import hashlib

def send_file(server, filename, packet_size, client_address):
    try:
        with open(filename, 'rb') as file:
            data = file.read(packet_size)
            while data:
                client_socket.sendto(data, client_address)
                data = file.read(packet_size)
    except FileNotFoundError:
        print(f'[ERROR] ¯\_(ツ)_/¯ File not found: {filename}')



def handle_request(server, request, client_address, packet_size):
    # Get requested filename from request
    filename = request.split()[1]

    # Send file to client
    send_file(server, filename, packet_size, client_address)

    # Compute a hash of the data
    hashed_data = hashlib.sha256(data).hexdigest()
    print(f'[HASH] Hash of received data: {hashed_data}')



def run_server():
    server_ip = '127.0.0.1'
    port = 5005
    format = 'utf-8' 
    packet_size = 1024

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
        print('[START] Server starting')
        server.bind((server_ip, port))
        print(f'[WAIT] Server waiting on {server_ip}:{port}')

        try:
            while True:
                data, client_address = server.recvfrom(packet_size)
                request = data.decode(format)
                print(f'[RECEIVE] Received data from {client_address[0]}:{client_address[1]}: \n{request}')

                # Process the received data
                handle_request(server, request, client_address, packet_size)

        except KeyboardInterrupt:
            print('[SHUTDOWN] Server is shutting down.')
            server.close()

        except Exception as e:
            print(f'[ERROR] Error: {e}')

        # finally:
            # server.close()



if __name__ == '__main__':
    run_server()
