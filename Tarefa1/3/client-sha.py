# Client Chat and File Transfer
import socket
import hashlib

def run_client():
    server_ip = "127.0.0.1"  # Server IP address
    port = 8000  # Server port number
    format = "utf-8"
    size = 1024

    try:
        # Create a socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Establish a connection with the server
        client.connect((server_ip, port))

        while True:
            # Get input from the user
            message = input("Enter message (type 'file' to send a file, 'close' to exit): ")

            if message.lower() == "close":
                client.send(message.encode(format))
                response = client.recv(size).decode(format)
                print(response)
                break
            elif message.lower() == "file":
                client.send(message.encode(format))
                filename = input("Enter the filename to send: ")
                client.send(filename.encode(format))

                with open(filename, "r") as file:
                    data = file.read()
                    # Calculate SHA-256 hash for file's contents
                    sha_hash = hashlib.sha256(data.encode()).hexdigest()
                    client.send(sha_hash.encode(format))
                    client.send(data.encode(format))
                    client.send(data.encode(format))
                    print("File sent successfully.")

                response = client.recv(size).decode(format)
                print(response)
            else:
                client.send(message.encode(format))
                response = client.recv(size).decode(format)
                print(f"Server: {response}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the client socket
        client.close()

run_client()
