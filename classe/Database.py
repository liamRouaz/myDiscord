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


# import mysql.connector

# class Database:
#     def __init__(self):
#         self.host = "10.10.98.90"                          #"10.10.94.117"
#         self.user = "test"
#         self.password = "test"
#         self.database = "myDiscord"

#     def get_connection(self):
#         try:
#             connection = mysql.connector.connect(
#                 host=self.host,
#                 user=self.user,
#                 password=self.password,
#                 database=self.database
#             )
#             return connection
#         except mysql.connector.Error as err:
#             raise  # Propagez l'exception en cas d'erreur de connexion

#     def execute_query(self, query, params):
#         with self.get_connection() as connection:
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

#     def fetch_data(self, query, params):
#         with self.get_connection() as connection:
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



import mysql.connector

class Database:
    def __init__(self):
        self.host = "10.10.100.103"
        self.user = "test"
        self.password = "test"
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
            raise  # Propagez l'exception en cas d'erreur de connexion

    def execute_query(self, query, params):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(query, params)
                connection.commit()
                if query.strip().upper().startswith('INSERT'):
                    return cursor.lastrowid
            except mysql.connector.Error as err:
                print("Error executing query:", err)
                raise
            finally:
                cursor.close()

    def fetch_data(self, query, params):
        with self.get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()







































