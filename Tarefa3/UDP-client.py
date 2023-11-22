import socket

def run_client():
    server_ip = '127.0.0.1'
    port = 5005

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            message = input("[SEND] Enter message to send (or 'exit' to quit): ")
            
            if message.lower() == 'exit':
                break
            
            client.sendto(message.encode('utf-8'), (server_ip, port))
            
    except Exception as e:
        print(f'[ERROR] Error: {e}')

    finally:
        client.close()

if __name__ == '__main__':
    run_client()
