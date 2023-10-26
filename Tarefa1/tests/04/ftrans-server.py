# File transfer server
import socket


IP = socket.gethostbyname(socket.gethostname())
PORT = 1024
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():
	print("[STARTING] Server is starting.")
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(ADDR)
	server.listen()
	print("[LISTENING] Server is listening.")

	while True:
		conn, addr = server.accept()
		print(f"[NEW CONNECTION] {addr} connected.")

		filename = conn.recv(SIZE).decode(FORMAT)
		print(f"[RECV] Receiving the filename.")
		file = open(filename, "w")
		conn.send("Filename received.".encode(FORMAT))

		data = conn.recv(SIZE).decode(FORMAT)
		print(f"[RECV] Receiving the file data.")
		file.write(data)
		conn.send("File data received".encode(FORMAT))

		file.close()
		conn.close()
		print(f"[DISCONNECTED] {addr} disconnected.")


if __name__ == "__main__":main()
