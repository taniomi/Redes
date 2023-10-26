# Server SHA
import socket
import threading
import hashlib

# Multithread Server
def handle_client(client_socket, addr, format, size):
    try:
        while True:
            request = client_socket.recv(size).decode(format)
            if request.lower() == "close":
                client_socket.send("closed".encode(format))
                break
            elif request.lower() == "file":
                client_socket.send("Send the file.".encode(format))
                filename = client_socket.recv(size).decode(format)

                # Receive the SHA hash from the client
                sha_hash = client_socket.recv(size).decode(format)

                if receive_file(client_socket, filename, sha_hash, format, size):
                    print(f"[FILE RECEIVED] Received file: {filename}")
                else:
                    print(f"[ERROR] File integrity check failed for {filename}")
            else:
                print(f"[RECEIVED] Client msg: {request}")
                response = "accepted"
                client_socket.send(response.encode(format))
    except Exception as e:
        print(f"[ERROR] Error when handling client {e}")
    finally:
        client_socket.close()
        print(f"[DISCONNECTED] Connection to client ({addr[0]}:{addr[1]}) closed")

def receive_file(client_socket, filename, expected_sha_hash, format, size):
    data = client_socket.recv(size).decode(format)
    
    # Calculate the SHA-256 hash of the received file data
    sha = hashlib.sha256(data.encode(format))
    calculated_sha_hash = sha.hexdigest()

    # Compare the calculated hash with the expected hash
    if calculated_sha_hash == expected_sha_hash:
        # If the hashes match, write the file data to disk
        with open("server_data/" + filename, "w") as file:
            file.write(data)
        return True
    else:
        return False

def run_server():
    server_ip = "127.0.0.1"
    port = 8000
    format = "utf-8"
    size = 1024

    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[START] Server starting")
        server.bind((server_ip, port))
        server.listen()
        print(f"[LISTENING] Server listening on {server_ip}:{port}")

        while True:
            client_socket, addr = server.accept()
            print(f"[NEW CONN] Accepted connection from {addr[0]}:{addr[1]}")
            thread = threading.Thread(target=handle_client, args=(client_socket, addr, format, size))
            thread.start()
    except Exception as e:
        print(f"[ERROR] Error: {e}")
    finally:
        server.close()

run_server()
