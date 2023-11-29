import socket

def receive_file(client, data, packet_size):
    _, filename = data.split(b'/', 1)
    filename = filename.decode('utf-8').strip()
    print(f'[FILE] Receiving file: {filename}')

    try:
        with open('client/' + filename, 'w') as file:
            while True:
                filedata, server = client.recvfrom(packet_size)
                if not filedata or filedata == b'FILE_END':
                    break
                file.write(filedata.decode('utf-8'))
            print(f'[FILE] File received: {filename}')

    except Exception as e:
        print(f'[ERROR] Error while receiving file: {e}')



def run_client():
    server_ip = '127.0.0.1'
    port = 5005
    packet_size = 1024

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.bind(('0.0.0.0', 0))  # Bind to any available port on the client side

    try:
        while True:
            message = input('[SEND] Enter message to send (or "exit" to quit): ')
            
            client.sendto(message.encode('utf-8'), (server_ip, port))

            if message.lower() == 'exit':
                print('[SHUTDOWN] Client is shutting down.')
                break
            
            # Receive data from the server
            data, server = client.recvfrom(packet_size)

            # Check if the received data is a file
            if data.decode('utf-8').startswith('FILE'):
                receive_file(client, data, packet_size)

            else:
                print(f'[MESSAGE] Received msg from server: {data.decode("utf-8", "ignore")}')
                
    except KeyboardInterrupt:
        print('[SHUTDOWN] Client is shutting down.')

    except Exception as e:
        print(f'[ERROR] Error: {e}')

    finally:
        client.close()



if __name__ == '__main__':
    run_client()
