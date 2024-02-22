from Database import Database

class Users:
    
    def __init__(self, first_name, last_name, email, password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.permis_channels = []

    def add_permis_channel(self, channel):
        self.permis_channels.append(channel)

    def is_permis_channel(self, channel):
        return channel in self.permis_channels  

    def save_to_db(self):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        params = (self.first_name, self.last_name, self.email, self.password)
        self.db.execute_query(query, params)

    def register_user(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.save_to_db()

    def authenticate_user(self, email, password):
        query = "SELECT id FROM users WHERE email = %s AND password = %s"
        params = (email, password)
        result = self.db.fetch_data(query, params)
        return result[0][0] if result else None