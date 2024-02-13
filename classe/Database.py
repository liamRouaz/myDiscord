import mysql.connector
# import datetime

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
            print("Error:", err)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        self.connect()
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            cursor.close()
            self.disconnect()

    def fetch_data(self, query, params=None):
        self.connect()
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            print("Error:", err)
        finally:
            cursor.close()
            self.disconnect()

    def insert_message(self, user_id, content, timestamp, channel_id):
        query = "INSERT INTO messages (user_id, content, timestamp, channel_id) VALUES (%s, %s, %s, %s)"
        params = (user_id, content, timestamp, channel_id)
        self.execute_query(query, params)        

    def get_unread_messages(self, user_id):
        query = "SELECT * FROM messages WHERE is_read = 0 AND user_id = %s"
        params = (user_id,)
        return self.fetch_data(query, params)









































