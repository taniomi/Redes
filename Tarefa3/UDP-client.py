import socket

def receive_file(client_socket, filename, packet_size):
    try:
        with open(filename, 'wb') as file:
            while True:
                data, server_address = client_socket.recvfrom(packet_size)
                if not data:
                    break
                file.write(data)
    except Exception as e:
        print(f'[ERROR] Error while receiving file: {e}')

def run_client():
    server_ip = '127.0.0.1'
    port = 5005

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind(('0.0.0.0', 0))  # Bind to any available port on the client side

    try:
        while True:
            message = input("[SEND] Enter message to send (or 'exit' to quit): ")
            
            if message.lower() == 'exit':
                break
            
            client.sendto(message.encode('utf-8'), (server_ip, port))

            # Receive data from the server
            data, server_address = client.recvfrom(1024)

            # Check if the received data is a file
            if data.startswith(b'FILE'):
                _, filename = data.split(b'\n', 1)
                filename = filename.decode('utf-8').strip()
                print(f"[RECEIVE] Receiving file: {filename}")
                receive_file(client, filename, 1024)
                print(f"[RECEIVE] File received: {filename}")
            else:
                print(f"[RECEIVE] Received data from server: {data.decode('utf-8')}")

    except Exception as e:
        print(f'[ERROR] Error: {e}')

    finally:
        client.close()

if __name__ == '__main__':
    run_client()
