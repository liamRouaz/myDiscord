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
            raise  # Propagez l'exception en cas d'erreur de connexion

    def execute_query(self, query, params):
        with self.get_connection() as connection:
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
        with self.get_connection() as connection:
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










































