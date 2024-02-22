# import mysql.connector

# class Database:
#     def __init__(self):
#         self.host = "localhost"
#         self.user = "root"
#         self.password = "soso"
#         self.database = "myDiscord"
#         self.connection = None
#         self.connect()

#     def connect(self):
#         try:
#             self.connection = mysql.connector.connect(
#                 host=self.host,
#                 user=self.user,
#                 password=self.password,
#                 database=self.database
#             )
#         except mysql.connector.Error as err:
#             print("Error connecting to the database:", err)

#     def disconnect(self):
#         if self.connection:
#             self.connection.close()

#     def execute_query(self, query, params=None):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(query, params)
#             if params is not None:
#                 self.connection.commit()
#             if query.strip().upper().startswith('INSERT'):
#                 return cursor.lastrowid   
#         except mysql.connector.Error as err:
#             print("Error executing query:", err)
#             raise
#         finally:
#             if cursor:
#                 cursor.close()

#     def fetch_data(self, query, params=None):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(query, params)
#             result = cursor.fetchall()
#             return result
#         except mysql.connector.Error as err:
#             print("Error fetching data:", err)
#             raise
#         finally:
#             if cursor:
#                 cursor.close()





import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="soso",
            database="myDiscord"
        )

    def get_connection(self):
        return self.connection











































