import socket
from threading import Thread

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.client_socket.connect((self.host, self.port))
        print("Connected to server.")

        receive_thread = Thread(target=self.receive_messages)
        receive_thread.start()

        while True:
            message = input()
            self.client_socket.sendall(message.encode())

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                print("\nReceived:", message)
            except Exception as e:
                print("Error:", e)
                break

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 5555
    client = ChatClient(HOST, PORT)
    client.start()


