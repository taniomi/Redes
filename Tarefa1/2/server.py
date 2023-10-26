# Server Multithread Chat and File Exchange
import socket
import threading

# Multithread Server
def handle_client(client_socket, addr, format, size):
    try:
        while True:
            request = client_socket.recv(size).decode(format)
            if request.lower() == "help":
                response = "\n\n>help: shows commands\n"
                response+= ">close: closes connection\n"
                response+= ">file: send a file\n"
                response+= ">hello: starts chat\n"
                response+= ">bye: ends chat"
                client_socket.send(response.encode(format))
            elif request.lower() == "close":
                client_socket.send("closed".encode(format))
                break
            elif request.lower() == "file":
                client_socket.send("Send the file.".encode(format))
                filename = client_socket.recv(size).decode(format)
                receive_file(client_socket, filename, format, size)
            elif request.lower() == "hello":
                print("[HELLO] Starting chat")
                chat_with_client(client_socket, format, size)
            else:
                print(f"[RECEIVED] Client msg: {request}")
                response = "accepted"
                client_socket.send(response.encode(format))
    except Exception as e:
        print(f"[ERROR] Error when handling client {e}")
    finally:
        client_socket.close()
        print(f"[DISCONNECTED] Connection to client ({addr[0]}:{addr[1]}) closed")

def chat_with_client(client_socket, format, size):
    try:
        client_socket.send("hello 👋".encode(format))
        while True:
            request = client_socket.recv(size).decode(format)
            if request.lower() == "bye":
                print(f"[BYE] Ending chat with the client: {client_socket}")
                client_socket.send("bye 👋".encode(format))
                break
            else:
                print(f"[CHAT] Client msg: {request}")
                response = input("Speak: ")
                client_socket.send(response.encode(format))
    except Exception as e:
        print(f"[ERROR] Error when handling chat with the client: {e}")

def receive_file(client_socket, filename, format, size):
    data = client_socket.recv(size).decode(format)
    with open("server_data/" + filename, "w") as file:
        file.write(data)
    print(f"[FILE RECEIVED] Received file: {filename}")

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
