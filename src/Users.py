from Database import Database

class Users:
    def __init__(self):
        self.db = Database()
        self.permis_channels = []

    def create_user(self, first_name, last_name, email, password):
        if first_name and last_name and email and password:
            self.register_user(first_name, last_name, email, password)
        else:
            print("Informations utilisateur incomplètes.")

    def add_permis_channel(self, channel):
        self.permis_channels.append(channel)

    def is_permis_channel(self, channel):
        return channel in self.permis_channels
    
    def register_user(self, first_name, last_name, email, password):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        params = (first_name, last_name, email, password)
        try:
            user_id = self.db.execute_query(query, params)
            if user_id:
                print("User inserted successfully with ID:", user_id)
            else:
                print("Failed to insert user into database.")
        except Exception as e:
            print("Error inserting user into database:", e)