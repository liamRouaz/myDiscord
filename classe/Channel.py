# from Database import Database

# class Channel:
#     def __init__(self, id, name, is_public):
#         self.id = id
#         self.name = name
#         self.is_public = is_public
#         self.messages = []
#         self.db = Database()

#     def add_message(self, message):
#         self.messages.append(message)

#     def get_messages(self):
#         return self.messages

#     def save_to_db(self):
#         query = "INSERT INTO channels (name, is_public) VALUES (%s, %s)"
#         params = (self.name, self.is_public)
#         self.db.execute_query(query, params)






    # @staticmethod
    # def get_all_channels(db):
    #     db = Database
    #     query = "SELECT * FROM channels"
    #     return db.fetch_data(query)




from Database import Database

class Channel:
    def __init__(self, id, name, is_public):
        self.id = id
        self.name = name
        self.is_public = is_public
        self.messages = []
        self.db = Database()  # Initialisez l'attribut db en appelant le constructeur

    def create_channel(self):
        self.db.insert_channel(self.name, self.is_public)

    @staticmethod
    def get_channels():
        db = Database()
        return db.get_channels()

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def save_to_db(self):  # Assurez-vous d'appeler la méthode execute_query de la classe Database
        query = "INSERT INTO channels (name, is_public) VALUES (%s, %s)"
        params = (self.name, self.is_public)
        self.db.execute_query(query, params)




