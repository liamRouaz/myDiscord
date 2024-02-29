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
#                 if not message:  # Vérifier si aucun message n'est reçu
#                     print("Server closed the connection.")
#                     break
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

#     def connect_to_server(self, email, password, user_id):
#         try:
#             self.client_socket.connect((self.host, self.port))
#             print("Connected to server.")
            
#             # Envoyer les informations d'identification et l'identifiant de l'utilisateur au serveur
#             credentials_and_id = f"{email}:{password}:{user_id}"
#             self.client_socket.sendall(credentials_and_id.encode())
#             print("User ID sent to server.")

#             # Démarrer le thread pour recevoir les messages
#             receive_thread = threading.Thread(target=self.receive_messages)
#             receive_thread.start()

#             # Démarrer la boucle pour l'envoi de messages
#             self.send_messages()
#             # self.start()
#         except Exception as e:
#             print("Error:", e)

#     def close_connection(self):
#         try:
#             self.client_socket.close()
#             print("Connection closed.")
#         except Exception as e:
#             print("Error:", e)

# if __name__ == "__main__":
#     HOST = '10.10.94.117'
#     PORT = 5000
#     client = ChatClient(HOST, PORT)
#     client.connect_to_server()





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

    # Méthode connect_to_server
    def connect_to_server(self, email, password, user_id):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Connected to server.")

            # Envoyer les informations d'identification au serveur
            credentials = f"{email}:{password}:{user_id}"
            self.client_socket.sendall(credentials.encode())
            print("Credentials sent to server.")

            # Attendre la réponse du serveur
            response = self.client_socket.recv(1024).decode()
            if response == "AUTH_SUCCESS":
                print("Authentication successful.")
            else:
                print("Authentication failed.")
                self.client_socket.close()
                return

            # Démarrer le thread pour recevoir les messages
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.start()

            # Démarrer la boucle pour l'envoi de messages
            self.send_messages()
        except Exception as e:
            print("Error:", e)
            self.client_socket.close()

    # Méthode receive_messages
    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:  # Vérifier si aucun message n'est reçu
                    print("Server closed the connection.")
                    self.client_socket.close()  # Fermer la connexion du client
                    break
                print("\nReceived:", message)
            except Exception as e:
                print("Error:", e)
                self.client_socket.close()  # Fermer la connexion du client
                break

    # Méthode send_messages
    def send_messages(self):
        while True:
            message = input("Enter message: ")
            if message:
                try:
                    # Vérifier si le client est connecté avant d'envoyer le message
                    if self.client_socket.fileno() != -1:
                        self.client_socket.sendall(message.encode())
                    else:
                        print("Client is not connected.")
                        break
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

if __name__ == "__main__":
    # HOST = '10.10.94.117'
    HOST = "10.10.98.90"
    PORT = 5000
    client = ChatClient(HOST, PORT)
    client.connect_to_server()



    