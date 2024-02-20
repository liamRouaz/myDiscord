from Database import Database
from Users import Users
from Channel import Channel
from Message import Message
import socket
from threading import Thread
from datetime import datetime
import mysql.connector

class ChatServeur:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.db = Database()
        self.user = Users('db', 'first_name', 'last_name', 'email', 'password')
        self.channels = []

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Serveur started on {}:{}".format(self.host, self.port))
        # self.create_channels()

        while True:
            client_socket, client_address = self.server_socket.accept()
            print("New connection from:", client_address)
            client_handler = Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

    def create_channels(self):
        # Créer des canaux
        self.channels.append(Channel("sport", is_public=True))
        self.channels.append(Channel("cinéma", is_public=True))
        self.channels.append(Channel("manga", is_public=True))

    def handle_client(self, client_socket):
        self.clients.append(client_socket)
        # channel_id = self.get_channel_id(client_socket)

        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    print("Received:", message)
                    break
                
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if message == "/quit":
                    self.disconnect_client(client_socket)
                    break

                channel_id = self.get_channel_id(client_socket)
                user_id = self.get_user_id(client_socket)
                self.db.insert_message(user_id, message, current_time, channel_id)
                print(self.channels)
                for channel in self.channels:
                    print(channel)
                    if channel.id == channel_id and (channel.is_public or not channel.is_public and self.user.is_permis_channel(channel)):
                        channel.add_message(Message(user_id, message, current_time))

                self.broadcast(message, client_socket)
            except Exception as e:
                print("Error:", e)
                break

        client_socket.close()
        self.clients.remove(client_socket)

    def create_user(self, user_info):
        last_name = user_info.get("last_name")
        email = user_info.get("email")
        password = user_info.get("password")
        if last_name and email and password:
            self.users = Users(self.db, last_name, email, password)
        else:
            print("Informations utilisateur incomplètes.")


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

    def create_channel(self, channel_id, name, is_public):
        channel = Channel(channel_id, name, is_public)
        self.channels.append(channel)  

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            if params is not None:
                self.connection.commit()
            if query.strip().upper().startswith('INSERT'):
                return cursor.lastrowid   
        except mysql.connector.Error as err:
            print("Error executing query:", err)
            raise
        finally:
            if cursor:
                cursor.close()

    def fetch_data(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print("Error fetching data:", err)
            raise
        finally:
            if cursor:
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

    def broadcast(self, message, client_socket):
        for client in self.clients:
            if client != client_socket:
                try:
                    client.sendall(message.encode())
                except Exception as e:
                    print(f"Error broadcasting message: {e}")

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



# if __name__ == "__main__":
#     HOST = 'localhost'
#     PORT = 8585
#     serveur = ChatServeur(HOST, PORT)
#     serveur.handle_client()
#     serveur.start()
  



# import socket
# from threading import Thread

# class ChatServer:
#     MAX_MESSAGE_LENGTH = 1024

#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#         self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.clients = []

#     def start(self):
#         try:
#             self.server_socket.bind((self.host, self.port))
#             self.server_socket.listen(5)
#             print(f"Server started on {self.host}:{self.port}")
#             self.accept_clients()
#         except Exception as e:
#             print("Error starting server:", e)

#     def accept_clients(self):
#         while True:
#             client_socket, client_address = self.server_socket.accept()
#             print("New connection from:", client_address)
#             client_handler = Thread(target=self.handle_client, args=(client_socket,))
#             client_handler.start()

#     def handle_client(self, client_socket):
#         try:
#             self.clients.append(client_socket)
#             while True:
#                 message = client_socket.recv(ChatServer.MAX_MESSAGE_LENGTH).decode()
#                 if not message:
#                     print("Received empty message, closing connection.")
#                     break
#                 self.broadcast(message, client_socket)
#         except Exception as e:
#             print("Error handling client:", e)
#         finally:
#             self.disconnect_client(client_socket)

#     def broadcast(self, message, sender_socket):
#         for client_socket in self.clients:
#             if client_socket != sender_socket:
#                 try:
#                     client_socket.sendall(message.encode())
#                 except Exception as e:
#                     print("Error sending message to client:", e)

#     def disconnect_client(self, client_socket):
#         try:
#             client_socket.close()
#             print("Client disconnected.")
#             self.clients.remove(client_socket)
#         except Exception as e:
#             print("Error disconnecting client:", e)

# if __name__ == "__main__":
#     HOST = 'localhost'
#     PORT = 8585
#     server = ChatServer(HOST, PORT)
#     server.start()
