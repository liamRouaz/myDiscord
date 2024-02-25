import socket
import threading
from datetime import datetime
import mysql.connector
from Database import Database
#from Message import Message

class ChatServeur():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.db = Database()
        self.channels = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Serveur started on {}:{}".format(self.host, self.port))

        while True:
            client_socket, client_address = self.server_socket.accept()
            print("New connection from:", client_address)
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

    
    def handle_client(self, client_socket):
        self.clients.append(client_socket)
        message = ""

        while True:
            try:
                data = client_socket.recv(1024).decode()
                if not data:
                    print("Received:", data)
                    break

                # Ajoutez les données reçues à votre message
                message += data

                # Vérifiez si le message se termine par "/end"
                if message.endswith("/end"):
                    message = message.replace("/end", "")  # Supprimez l'indicateur de fin de message
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    channel_id = self.get_channel_id(client_socket)
                    user_id = self.get_user_id(client_socket)

                    # Créez un message avec les données reçues
                    message_instance = Message(self, user_id, message, current_time, channel_id)
                    message_instance.send_message()

                    for channel in self.channels:
                        if channel.id == channel_id and (channel.is_public or not channel.is_public and self.users.is_permis_channel(channel)):
                            channel.add_message(message_instance)

                    self.broadcast(message, client_socket)

                    # Réinitialisez le message pour les prochains messages
                    message = ""

            except Exception as e:
                print("Error:", e)
                break

        # Gérer la déconnexion du client
        self.disconnect_client(client_socket)


    # def authenticate_user(self, email, password):
    #     connection = self.db.get_connection()
    #     cursor = connection.cursor()
    #     query = "SELECT id FROM users WHERE email = %s AND password = %s"
    #     params = (email, password)
    #     cursor.execute(query, params)
    #     result = cursor.fetchone()
    #     cursor.close()
    #     return result[0] if result else None

    def authenticate_user(self, email, password):
        query = "SELECT id FROM users WHERE email = %s AND password = %s"
        params = (email, password)
        result = self.fetch_data(query, params)
        return result[0][0] if result else None
   
    
    def execute_query(self, query, params=None):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            if params is not None:
                connection.commit()
            if query.strip().upper().startswith('INSERT'):
                return cursor.lastrowid
        except mysql.connector.Error as err:
            print("Error executing query:", err)
            raise
        finally:
            cursor.close()

    def fetch_data(self, query, params=None):
        connection = self.db.get_connection()
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print("Error fetching data:", err)
            raise
        finally:
            cursor.close()

    def insert_message(self, user_id, content, timestamp, channel_id):
        query = "INSERT INTO messages (author, content, timestamp, channel_id) VALUES (%s, %s, %s, %s)"
        params = (user_id, content, timestamp, channel_id)
        self.execute_query(query, params)

    def insert_channel(self, name, is_public):
        query = "INSERT INTO channels (name, is_public) VALUES (%s, %s)"
        params = (name, is_public)
        self.execute_query(query, params)   

    def insert_user(self, first_name, last_name, email, password):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        params = (first_name, last_name, email, password)
        self.execute_query(query, params)

    def get_channels(self):
        query = "SELECT * FROM channels"
        return self.fetch_data(query)

    def get_users(self):
        query = "SELECT * FROM users"
        return self.fetch_data(query)

    def get_messages_for_channel(self, channel_id):
        query = "SELECT * FROM messages WHERE channel_id = %s"
        params = (channel_id,)
        return self.fetch_data(query, params)

    def get_reactions_for_message(self, message_id):
        query = "SELECT * FROM reactions WHERE message_id = %s"
        params = (message_id,)
        return self.fetch_data(query, params)

    def register_user(self, first_name, last_name, email, password):
        return self.register_user(first_name, last_name, email, password)        

    def broadcast(self, message, client_socket):
        for client in self.clients:
            if client != client_socket and client.fileno() != -1:
                try:
                    client.sendall(message.encode())
                except Exception as e:
                    print("Error:", e)

    def get_user_id(self, client_socket):
        user_id = None
        if hasattr(client_socket, 'user_id'):
            user_id = client_socket.user_id
        return user_id

    def get_channel_id(self, client_socket):
        channel_id = None
        if hasattr(client_socket, 'channel_id'):
            channel_id = client_socket.channel_id
        return channel_id

    def disconnect_client(self, client_socket):
        try:
            client_socket.close()
            print("Client disconnected.")
            if self.users and self.users.id == client_socket.user_id:
                self.users = None
        except Exception as e:
            print("Error occurred while disconnecting client:", e)


    # Retirez le client de la liste des clients
        self.clients.remove(client_socket)





