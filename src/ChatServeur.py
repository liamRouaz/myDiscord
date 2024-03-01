from Database import Database
import socket
import threading
from datetime import datetime
import mysql.connector
from Channel import Channel

class ChatServeur:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}
        self.clients_lock = threading.Lock()
        self.db = Database()
        self.channels = Channel.get_channels()
        self.sessions = {}  # Dictionnaire pour stocker les sessions des clients
    
    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(20)
            print("Serveur started on {}:{}".format(self.host, self.port))

            while True:
                client_socket, client_address = self.server_socket.accept()
                client_ip = client_address[0]
                print("New connection from:", client_ip)
                client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
                client_handler.start()
        except OSError as os_err:
            print("Error starting server:", os_err)

    def handle_client(self, client_socket):
        try:
            credentials_and_id = client_socket.recv(1024).decode()
            if ":" not in credentials_and_id:
                print("Invalid format for credentials and user ID")
                client_socket.send("Invalid format".encode("utf-8"))
                client_socket.close()
                return
            email, password, user_id = credentials_and_id.split(":")
            email, password, user_id = self.authenticate_user(email, password)
            if not email or not password or not user_id:
                print("Authentication failed for user:", user_id)
                client_socket.send("Authentication failed".encode("utf-8"))
                client_socket.close()
                return
            print("User connected:", user_id)
            client_socket.send("AUTH_SUCCESS".encode("utf-8"))

            # Demander à l'utilisateur de choisir un canal
            client_socket.send("Choose a channel:".encode("utf-8"))
            # Attendre la réponse de l'utilisateur
            channel_choice = client_socket.recv(1024).decode().strip()

            # Associe le client au canal choisi
            channel_id = self.get_channel_id_by_name(channel_choice)
            self.clients[client_socket] = channel_id

            with self.clients_lock:
                self.sessions[user_id] = client_socket

            while True:
                message = client_socket.recv(1024).decode()
                if not message:
                    break

                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if message == "/quit":
                    self.disconnect_client(client_socket)
                    break

                # Récupérer l'ID utilisateur et l'ID du canal
                channel_id = self.clients[client_socket]
                user_id = user_id

                # Insérer le message dans la base de données
                message_id = self.insert_message(user_id, message, current_time, channel_id)

                if message_id:
                    formatted_message = f"{user_id}: {message}"
                    self.broadcast(formatted_message, client_socket)
                else:
                    print("Error inserting message into database")
                    client_socket.send("Error inserting message".encode("utf-8"))
        except Exception as e:
            print("Error:", e)
            client_socket.send("Internal server error".encode("utf-8"))
            client_socket.close()
            self.disconnect_client(client_socket)

    def disconnect_client(self, client_socket):
        if client_socket in self.clients:
            client_socket.close()
            del self.clients[client_socket]
            # Supprimer le client de la session s'il existe
            user_id = self.get_user_id(client_socket)
            if user_id in self.sessions:
                del self.sessions[user_id]

    def broadcast(self, message, client_socket):
        for client in list(self.clients.keys()):
            if client != client_socket and client.fileno() != -1:
                try:
                    client.send(message.encode())
                except socket.error:
                    print("Client disconnected")
                    del self.clients[client]

    def insert_message(self, author_id, content, timestamp, channel_id):
        user_first_name = self.get_user_first_name(author_id)
        if user_first_name is None:
            print("Error: User not found for ID:", author_id)
            return None

        query = "INSERT INTO messages (author, content, timestamp, channel_id) VALUES (%s, %s, %s, %s)"
        params = (user_first_name, content, timestamp, channel_id)
        try:
            with self.db.get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                message_id = cursor.lastrowid
                connection.commit()
                cursor.close()
                return message_id
        except mysql.connector.Error as err:
            print("Error inserting message into database:", err)
            return None

    def authenticate_user(self, email, password):
        query = "SELECT id FROM users WHERE email = %s AND password = %s"
        params = (email, password)
        result = self.db.fetch_data(query, params)
        
        # Récupére tous les user_id correspondant aux informations d'identification fournies
        user_ids = [row[0] for row in result] if result else []
        return email, password, user_ids[0] if user_ids else None

    def get_user_first_name(self, user_id):
        query = "SELECT first_name FROM users WHERE id = %s"
        params = (user_id,)
        result = self.db.fetch_data(query, params)
        return result[0][0] if result else None

    def get_channel_id_by_name(self, channel_name):
        for channel in self.channels:
            if channel.name == channel_name:
                return channel.id
        return None

if __name__ == "__main__":
    HOST = '10.10.100.103'
    PORT = 5000
    serveur = ChatServeur(HOST, PORT)
    serveur.start()