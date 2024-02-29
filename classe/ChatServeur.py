# from Database import Database
# import socket
# import threading 
# from datetime import datetime
# import mysql.connector

# class ChatServeur:
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#         self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.clients = []
#         self.db = Database()
#         self.channels = []

#     def start(self):
#         self.server_socket.bind((self.host, self.port))
#         self.server_socket.listen(5)
#         print("Serveur started on {}:{}".format(self.host, self.port))   

#         while True:
#             client_socket, client_address = self.server_socket.accept()
#             print("New connection from:", client_address)
#             client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
#             client_handler.start()

#     def handle_client(self, client_socket):
#         try:
#             credentials_and_id = client_socket.recv(1024).decode()
#             if ":" not in credentials_and_id:
#                 print("Invalid format for credentials and user ID")
#                 client_socket.close()
#                 return
#             email, password, user_id = credentials_and_id.split(":")
#             print("User connected:", user_id)
#             self.clients.append((client_socket, user_id))

#             while True:
#                 message = client_socket.recv(1024).decode()
#                 if not message:
#                     break
                
#                 current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#                 if message == "/quit":
#                     self.disconnect_client(client_socket)
#                     break

#                 channel_id = self.get_channel_id(client_socket)
#                 user_id = self.get_user_id(client_socket)

#                 # Insérer le message dans la base de données
#                 message_id = self.insert_message(user_id, message, current_time, channel_id)

#                 # Si l'insertion dans la base de données est réussie, diffuser le message
#                 if message_id:
#                     formatted_message = f"{user_id}: {message}" # Formatage du message avec l'ID de l'utilisateur
#                     self.broadcast(formatted_message, client_socket)
#                 else:
#                     print("Error inserting message into database")    
#                 # self.insert_message(user_id, message, current_time, channel_id)
#                 # self.broadcast(message, client_socket)
#         except Exception as e:
#             print("Error:", e)
#             self.disconnect_client(client_socket)

#     def disconnect_client(self, client_socket):
#         if client_socket in self.clients:
#             client_socket.close()
#             self.clients.remove(client_socket)

#     def broadcast(self, message, client_socket):
#         for client in self.clients:
#             if client[0] != client_socket and client[0].fileno() != -1:# modif du if client a la place de if client[0] pour ne pas voir c message
#                 try:
#                     client[0].send(message.encode())
#                 except socket.error:
#                     print("Client disconnected")
#                     self.clients.remove(client)

#     # def insert_message(self, author, content, timestamp, channel_id):
#     #     query = "INSERT INTO messages (author, content, timestamp, channel_id) VALUES (%s, %s, %s, %s)"
#     #     params = (author, content, timestamp, channel_id)
#     #     self.execute_query(query, params)
                    
#     def insert_message(self, author, content, timestamp, channel_id):
#         query = "INSERT INTO messages (author, content, timestamp, channel_id) VALUES (%s, %s, %s, %s)"
#         params = (author, content, timestamp, channel_id)
#         try:
#             with self.db.get_connection() as connection:
#                 cursor = connection.cursor()
#                 cursor.execute(query, params)
#                 message_id = cursor.lastrowid
#                 connection.commit()
#                 cursor.close()
#                 return message_id
#         except mysql.connector.Error as err:
#             print("Error inserting message into database:", err)
#             return None


#     def insert_channel(self, name, is_public):
#         query = "INSERT INTO channels (name, is_public) VALUES (%s, %s)"
#         params = (name, is_public)
#         self.execute_query(query, params)   

#     def insert_user(self, first_name, last_name, email, password):
#         query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
#         params = (first_name, last_name, email, password)
#         self.execute_query(query, params)    

#     def execute_query(self, query, params):
#         with self.db.get_connection() as connection:
#             cursor = connection.cursor()
#             try:
#                 cursor.execute(query, params)
#                 if query.strip().upper().startswith('INSERT'):
#                     return cursor.lastrowid
#                 connection.commit()
#             except mysql.connector.Error as err:
#                 print("Error executing query:", err)
#                 raise
#             finally:
#                 cursor.close()

#     def fetch_data(self, query, params=None):
#         with self.db.get_connection() as connection:
#             cursor = connection.cursor()
#             try:
#                 cursor.execute(query, params)
#                 result = cursor.fetchall()
#                 return result
#             except mysql.connector.Error as err:
#                 print("Error fetching data:", err)
#                 raise
#             finally:
#                 cursor.close()

#     def authenticate_user(self, email, password):
#         query = "SELECT first_name FROM users WHERE email = %s AND password = %s"
#         params = (email, password)
#         result = self.fetch_data(query, params)
#         return result[0][0] if result else None           
 
#     def get_channels(self):
#         query = "SELECT * FROM channels"
#         return self.fetch_data(query, params=None)

#     def get_users(self):
#         query = "SELECT * FROM users"
#         return self.fetch_data(query, params=None)

#     def get_messages_for_channel(self, channel_id):
#         query = "SELECT * FROM messages WHERE channel_id = %s"
#         params = (channel_id,)
#         return self.fetch_data(query, params)

#     def get_reactions_for_message(self, message_id):
#         query = "SELECT * FROM reactions WHERE message_id = %s"
#         params = (message_id,)
#         return self.fetch_data(query, params)
    
#     def get_user_id(self, client_socket):
#         user_id = None
#         if hasattr(client_socket, 'user_id'):
#             user_id = client_socket.user_id
#         return user_id

#     def get_channel_id(self, client_socket):
#         channel_id = None
#         if hasattr(client_socket, 'channel_id'):
#             channel_id = client_socket.channel_id
#         return channel_id

#     def register_user(self, first_name, last_name, email, password):
#         return self.insert_user(first_name, last_name, email, password)

# if __name__ == "__main__":
#     HOST = 'localhost'
#     PORT =  8585
#     serveur = ChatServeur(HOST, PORT)
#     serveur.start()




from Database import Database
import socket
import threading
from datetime import datetime
import mysql.connector
from Permissions import Permissions

class ChatServeur:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.clients_lock = threading.Lock()
        self.db = Database()
        self.channels = []
        self.sessions = {}  # Dictionnaire pour stocker les sessions des clients
        self.permissions_manager = Permissions()

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            print("Serveur started on {}:{}".format(self.host, self.port))

            while True:
                client_socket, client_address = self.server_socket.accept()
                client_ip = client_address[0]  # IP du client
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
            client_socket.send("AUTH_SUCCESS".encode("utf-8"))  # Envoyer une réponse de succès
            with self.clients_lock:
                self.clients.append((client_socket, user_id))
                if user_id not in self.sessions:
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
                channel_id = self.get_channel_id(client_socket)
                user_id = self.get_user_id(client_socket)

                # Vérifier si l'utilisateur a la permission d'envoyer un message dans ce canal
                # if not self.permissions_manager.check_permission(user_id, channel_id):
                #     print("User does not have permission to send messages in this channel")
                #     continue

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
        with self.clients_lock:
            if client_socket in self.clients:
                client_socket.close()
                self.clients.remove(client_socket)
                # Supprimer le client de la session s'il existe
                user_id = self.get_user_id(client_socket)
                if user_id in self.sessions:
                    del self.sessions[user_id]

    def broadcast(self, message, client_socket):
        with self.clients_lock:
            for client in self.clients:
                if client[0] != client_socket and client[0].fileno() != -1:
                    try:
                        client[0].send(message.encode())
                    except socket.error:
                        print("Client disconnected")
                        self.clients.remove(client)

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

    def insert_channel(self, name, is_public):
        query = "INSERT INTO channels (name, is_public) VALUES (%s, %s)"
        params = (name, is_public)
        self.db.execute_query(query, params)   

    def insert_user(self, first_name, last_name, email, password):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        params = (first_name, last_name, email, password)
        connection = self.db.get_connection()
        if connection is not None:
            try:
                cursor = connection.cursor()
                cursor.execute(query, params)
                connection.commit()
                cursor.close()
                connection.close()  # Fermer la connexion après usage
                print("User inserted successfully")
            except mysql.connector.Error as err:
                print("Error inserting user into database:", err)
        else:
            print("Error: Unable to establish database connection")
 

    def get_user_first_name(self, user_id):
        query = "SELECT first_name FROM users WHERE id = %s"
        params = (user_id,)
        result = self.db.fetch_data(query, params)
        return result[0][0] if result else None

    def authenticate_user(self, email, password):
        query = "SELECT id FROM users WHERE email = %s AND password = %s"
        params = (email, password)
        result = self.db.fetch_data(query, params)
        
        # Récupére tous les user_id correspondant aux informations d'identification fournies
        user_ids = [row[0] for row in result] if result else []
        return email, password, user_ids[0] if user_ids else None

    def get_user_id(self, client_socket):
        for client in self.clients:
            if client[0] == client_socket:
                return client[1]  # Renvoie le user_id associé au client_socket
        return None  # Renvoie Aucun si client_socket n'est pas trouvé

    def get_channel_id(self, client_socket):
        return None

if __name__ == "__main__":
    HOST = '10.10.98.90'
    PORT = 5000
    serveur = ChatServeur(HOST, PORT)
    serveur.start()


