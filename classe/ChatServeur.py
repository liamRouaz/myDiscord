from Database import Database
import socket
from threading import Thread
import datetime

class ChatServeur:
    def __init__(self, host, port, channel_id, user_id):
        self.host = host
        self.port = port
        self.serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.db = Database()
        self.channel_id = channel_id
        self.user_id = user_id

    def start(self):
        self.serveur_socket.bind((self.host, self.port))
        self.serveur_socket.listen(5)
        print("Serveur started on {}:{}".format(self.host, self.port))

        while True:
            client_socket, client_address = self.serveur_socket.accept()
            print("New connection from:", client_address)
            client_handler = Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

    def handle_client(self, client_socket):
        self.clients.append(client_socket)
        channel_id = self.get_channel_id(client_socket)

        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                print("Received:", message)

                # Obtenir la date et l'heure actuelles
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # exemple pour quiter
                if message == "/quit":
                    self.disconnect_client(client_socket)
                    break

                # Déterminer l'identifiant du canal en fonction des données reçues du client
                # Channel ID needs to be obtained from client data
                channel_id = self.get_channel_id(client_socket)  # Pass client_socket
                user_id = self.get_user_id(client_socket)
                self.db.insert_message(user_id, message, current_time, channel_id)

                self.broadcast(message, client_socket)
            except Exception as e:
                print("Error:", e)
                break

        client_socket.close()
        self.clients.remove(client_socket)

    def broadcast(self, message, client_socket):
        for client in self.clients:
            if client != client_socket:
                try:
                    client.sendall(message.encode())
                except Exception as e:
                    print("Error:", e)

    def get_user_id(self, client_socket):
        user_id = None
        if hasattr(client_socket, 'user_id'):
            user_id = client_socket.user_id
        return user_id               


    def authenticate_user(self, email, password):
        user_id = None
        try:
            query = "SELECT id FROM users WHERE email = %s AND password = %s"
            params = (email, password)
            result = self.db.fetch_data(query, params)
            if result:
                user_id = result[0][0]
        except Exception as e:
            print("Error during user authentication:", e)
            return user_id

    def register_user(self, first_name, last_name, email, password):
        success = False
        try:
            query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
            params = (first_name, last_name, email, password)
            self.db.execute_query(query, params)
            success = True
        except Exception as e:
            print("Error during user registration:", e)
        return success
    
    def get_channel_id(self, client_socket):
        channel_id = None
        if hasattr(client_socket, 'channel_id'):
            channel_id = client_socket.channel_id
        return channel_id


    def disconnect_client(self, client_socket):
        try:
            client_socket.close()
            print("Client disconnected.")
        except Exception as e:
            print("Error occurred while disconnecting client:", e)

if __name__ == "__main__":
    HOST = 'localhost'
    PORT = 5555
    # serveur = ChatServeur(HOST, PORT)
    serveur = ChatServeur(HOST, PORT, channel_id=None, user_id=None)
    serveur.start()


