from Database import Database
from ChatServeur import ChatServeur

class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_to_db(self):
        db = Database()
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        params = (self.first_name, self.last_name, self.email, self.password)
        db.execute_query(query, params)

    @staticmethod
    def get_all_users():
        db = Database()
        query = "SELECT * FROM users"
        return db.fetch_data(query)

# Modife 
if __name__ == "__main__":
    server = ChatServeur('localhost', 5555)

