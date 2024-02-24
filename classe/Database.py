import mysql.connector

class Database:
    def get_connection(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="soso",
            database="myDiscord"
        )
        return self.connection











































