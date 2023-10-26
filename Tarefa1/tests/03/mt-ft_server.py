# Server
import os
import socket
import threading

IP = "127.0.0.1"
PORT = 4456
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
SERVER_DATA_PATH = "server_data"

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("OK@Welcome to the File Server.".encode(FORMAT))

    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split("@")
        cmd = data[0]

        if cmd == "LIST":
            files = os.listdir(SERVER_DATA_PATH)
            send_data = "OK@"

            if len(files) == 0:
                send_data += "The server directory is empty"
            else:
                send_data += "\n".join(f for f in files)
            conn.send(send_data.encode(FORMAT))

        elif cmd =="FILE":
            filename = conn.recv(SIZE).decode(FORMAT)
            print(f"[RECV] Receiving filename.")
            file = open(filename, "w")
            conn.send("OK@Filename received".encode(FORMAT))

            recv = conn.recv(SIZE).decode(FORMAT)
            print(f"[RECV] Receiving file data.")
            file.write(recv)
            conn.send("OK@File data received.".encode(FORMAT))

            file.close()

        elif cmd == "CHAT":
            conn.send("OK@Let's chat.".encode(FORMAT))

            while True:
                # receive and print client messages
                request = conn.recv(SIZE).decode(FORMAT)
                if request.lower() == "close":
                    conn.send("OK@closed".encode(FORMAT))
                    break
                print(f"[RECEIVED] Received: {request}")
                # convert and send accept response to the client
                response = "OK@accepted"
                conn.send(response.encode(FORMAT))

        elif cmd == "LOGOUT":
            break

        elif cmd == "HELP":
            data = "OK@"
            data += "LIST: List all the files from the server.\n"
            data += "FILE: Send file to server.\n"
            data += "CHAT: Chat with server.\n"
            data += "LOGOUT: Disconnect from the server.\n"
            data += "HELP: List all the commands."

            conn.send(data.encode(FORMAT))

    print(f"[DISCONNECTED] {addr} disconnected")
    conn.close()

def run_server():
    try:
        print("[STARTING] Server is starting")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(ADDR)
        server.listen()
        print(f"[LISTENING] Server is listening on {IP}:{PORT}.")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    except Exception as e:
        print(f"[ERROR] Error: {e}")
    finally:
        server.close()

run_server()
