# import socket
# import threading

# class ChatClient:
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#         self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#     def start(self):
#         try:
#             self.client_socket.connect((self.host, self.port))
#             print("Connected to server.")

#             # Démarrer le thread pour recevoir les messages
#             receive_thread = threading.Thread(target=self.receive_messages)
#             receive_thread.start()

#             # Démarrer la boucle pour l'envoi de messages
#             self.send_messages()
#         except Exception as e:
#             print("Error:", e)

#     def receive_messages(self):
#         while True:
#             try:
#                 message = self.client_socket.recv(1024).decode()
#                 print("\nReceived:", message)
#             except Exception as e:
#                 print("Error:", e)
#                 break

#     def send_messages(self):
#         while True:
#             message = input("Enter message: ")
#             if message:
#                 try:
#                     self.client_socket.sendall(message.encode())
#                 except Exception as e:
#                     print("Error:", e)
#                     break
#             else:
#                 print("Empty message. Please enter a valid message.")

#     def close_connection(self):
#         try:
#             self.client_socket.close()
#             print("Connection closed.")
#         except Exception as e:
#             print("Error:", e)

# if __name__ == "__main__":
#     HOST = 'localhost'
#     PORT = 8585
#     client = ChatClient(HOST, PORT)
#     client.start()



import socket
import threading

class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Connected to server.")

            # Démarrer le thread pour recevoir les messages
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()

            # Démarrer la boucle pour l'envoi de messages
            self.send_messages()
        except Exception as e:
            print("Error:", e)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                print("\nReceived:", message)
            except Exception as e:
                print("Error:", e)
                break

    def send_messages(self):
        while True:
            message = input("Enter message: ")
            if message:
                try:
                    self.client_socket.sendall(message.encode())
                except Exception as e:
                    print("Error:", e)
                    break
            else:
                print("Empty message. Please enter a valid message.")

    def close_connection(self):
        try:
            self.client_socket.close()
            print("Connection closed.")
        except Exception as e:
            print("Error:", e)

    def connect_to_server(self, email, password):
        try:
            # Envoyer les informations d'identification au serveur
            credentials = f"{email}:{password}"
            self.client_socket.sendall(credentials.encode())
            print("Credentials sent to server.")
        except Exception as e:
            print("Error sending credentials to server:", e)

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 8585
    client = ChatClient(HOST, PORT)
    client.start()

