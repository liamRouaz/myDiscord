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
            # self.send_messages()
        except Exception as e:
            print("Error:", e)

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
            # self.start()
            # Démarrer la boucle pour l'envoi de messages
            # self.send_messages()
        except Exception as e:
            print("Error:", e)
            self.client_socket.close()

    def send_messages(self, message):
        try:
            # Vérifier si le client est connecté avant d'envoyer le message
            if self.client_socket.fileno() != -1:
                self.client_socket.sendall(message.encode())
            else:
                print("Client is not connected.")
        except Exception as e:
            print("Error:", e)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:  # Vérifier si aucun message n'est reçu
                    print("Server closed the connection.")
                    break
                    # self.client_socket.close()  # Fermer la connexion du client
                print("\nReceived:", message)
            except Exception as e:
                print("Error:", e)
                break
        self.client_socket.close()  # Fermer la connexion du client
                
    def insert_message(self, message, channel_id):
        try:
            if self.client_socket.fileno() != -1:
                # Envoyer le message au serveur avec une commande spéciale pour l'insertion dans la base de données
                insert_command = f"{message}:{channel_id}"
                self.client_socket.sendall(insert_command.encode())
            else:
                print("Client is not connected.")
        except Exception as e:
            print("Error:", e)

    def close_connection(self):
        try:
            self.client_socket.close()
            print("Connection closed.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    # HOST = '10.10.94.117'
    HOST = "10.10.0.38"
    PORT = 5000
    client = ChatClient(HOST, PORT)
    client.connect_to_server()
