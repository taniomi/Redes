import socket
import hashlib

def send_file(server, filepath, packet_size, client):
    print(f'[FILE] Requested file: {filepath}')
    server.sendto(f'FILE {filepath}'.encode('utf-8'), client)
    
    filetype = filepath.split('.')[1]       

    if filetype == 'jpg':
        mode = 'rb'
    elif filetype == 'txt':
        mode = 'r'

    try:
        with open(filepath, mode) as file:
            filedata = file.read(packet_size).encode('utf-8')

            while filedata:
                server.sendto(filedata, client)
                filedata = file.read(packet_size)

        # Signal the end of the file
        server.sendto(b'FILE_END', client)

    except FileNotFoundError:
        print(f'[ERROR] File not found: {filepath}')
        server.sendto(f'[ERROR] File not found: {filepath}'.encode('utf-8'), client)



def compute_hash(path):
    with open(path, 'rb') as file:
        # Compute a hash of the data
        hashed_data = hashlib.sha256(file.read()).hexdigest()
    print(f'[HASH] Hash of sent file: {hashed_data}')



def handle_request(server, request, client, packet_size):
    # Get method and path from request
    method, path = request.split()[:2]

    if method == 'FILE':
        send_file(server, path, packet_size, client)

        compute_hash(path)
    
    else:
        print('[DEBUG]') # debug
        pass



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
                data, client = server.recvfrom(packet_size)
                data = data.decode(format)
                print(f'[RECEIVE] Received data from {client[0]}:{client[1]}: \n    {data}')

                if len(data.split()) > 1:
                    handle_request(server, data, client, packet_size)
                elif data == 'exit':
                    break

        except KeyboardInterrupt:
            pass

        except Exception as e:
            print(f'[ERROR] Error: {e}')

        finally:
            print('[SHUTDOWN] Server is shutting down.')
            server.close()



if __name__ == '__main__':
    run_server()
