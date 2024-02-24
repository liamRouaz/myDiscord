from Database import Database
import socket
import threading 
from datetime import datetime
import mysql.connector

class ChatServeur:
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
        try:
            credentials_and_id = client_socket.recv(1024).decode()
            if ":" not in credentials_and_id:
                print("Invalid format for credentials and user ID")
                client_socket.close()
                return
            email, password, user_id = credentials_and_id.split(":")
            print("User connected:", user_id)
            self.clients.append((client_socket, user_id))

            while True:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if message == "/quit":
                    self.disconnect_client(client_socket)
                    break

                channel_id = self.get_channel_id(client_socket)
                user_id = self.get_user_id(client_socket)

                self.insert_message(user_id, message, current_time, channel_id)
                self.broadcast(message, client_socket)
        except Exception as e:
            print("Error:", e)
            self.disconnect_client(client_socket)

    def disconnect_client(self, client_socket):
        if client_socket in self.clients:
            client_socket.close()
            self.clients.remove(client_socket)

    def broadcast(self, message, client_socket):
        for client in self.clients:
            if client != client_socket and client[0].fileno() != -1:
                try:
                    client[0].send(message.encode())
                except socket.error:
                    print("Client disconnected")
                    self.clients.remove(client)

    def insert_message(self, author, content, timestamp, channel_id):
        query = "INSERT INTO messages (author, content, timestamp, channel_id) VALUES (%s, %s, %s, %s)"
        params = (author, content, timestamp, channel_id)
        self.execute_query(query, params)

    def insert_channel(self, name, is_public):
        query = "INSERT INTO channels (name, is_public) VALUES (%s, %s)"
        params = (name, is_public)
        self.execute_query(query, params)   

    def insert_user(self, first_name, last_name, email, password):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        params = (first_name, last_name, email, password)
        self.execute_query(query, params)    

    def execute_query(self, query, params):
        with self.db.get_connection() as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query, params)
                if query.strip().upper().startswith('INSERT'):
                    return cursor.lastrowid
                connection.commit()
            except mysql.connector.Error as err:
                print("Error executing query:", err)
                raise
            finally:
                cursor.close()

    def fetch_data(self, query, params=None):
        with self.db.get_connection() as connection:
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

    def authenticate_user(self, email, password):
        query = "SELECT first_name FROM users WHERE email = %s AND password = %s"
        params = (email, password)
        result = self.fetch_data(query, params)
        return result[0][0] if result else None           
 
    def get_channels(self):
        query = "SELECT * FROM channels"
        return self.fetch_data(query, params=None)

    def get_users(self):
        query = "SELECT * FROM users"
        return self.fetch_data(query, params=None)

    def get_messages_for_channel(self, channel_id):
        query = "SELECT * FROM messages WHERE channel_id = %s"
        params = (channel_id,)
        return self.fetch_data(query, params)

    def get_reactions_for_message(self, message_id):
        query = "SELECT * FROM reactions WHERE message_id = %s"
        params = (message_id,)
        return self.fetch_data(query, params)
    
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

    def register_user(self, first_name, last_name, email, password):
        return self.insert_user(first_name, last_name, email, password)

if __name__ == "__main__":
    HOST = 'localhost'
    PORT =  8585
    serveur = ChatServeur(HOST, PORT)
    serveur.start()
