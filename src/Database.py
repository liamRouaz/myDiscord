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














