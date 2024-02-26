# import mysql.connector

# class Database:
#     def get_connection(self):
#         self.connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="soso",
#             database="myDiscord"
#         )
#         return self.connection


import mysql.connector

class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = "soso"
        self.database = "myDiscord"

    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return connection
        except mysql.connector.Error as err:
            print(f"Erreur de connexion à MySQL: {err}")
            return None









































