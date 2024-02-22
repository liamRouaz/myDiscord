import mysql.connector

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "soso"
        self.database = "myDiscord"
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as err:
            print("Error connecting to the database:", err)

    def disconnect(self):
        if self.connection:
            self.connection.close()

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



































