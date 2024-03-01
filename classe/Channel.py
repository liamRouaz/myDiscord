# from ChatServeur import ChatServeur
# from Database import Database

# class Channel:
#     def __init__(self,host, port, id, name, is_public):
#         self.id = id
#         self.name = name
#         self.is_public = is_public
#         self.messages = []
#         self.server = ChatServeur(host, port)
#         self.db = Database()
        
#     def create_channel(self):
#         self.server.insert_channel(self.name, self.is_public)

#     # def create_channel(self, channel_id, name, is_public):
#     #     channel = Channel(channel_id, name, is_public)
#     #     self.channels.append(channel) 

#     @staticmethod
#     def create_channels():
#         # Créer des canaux
#         ChatServeur().insert_channel("sport", "public") # Si sa marche pas remétre is_public=True
#         ChatServeur().insert_channel("cinéma", "public")
#         ChatServeur().insert_channel("manga", "public")

#     @staticmethod
#     def get_channels():
#         return ChatServeur().get_channels()
    
#     def add_message(self, message):
#         self.messages.append(message)

#     def get_messages(self):
#         return self.messages

#     def save_to_server(self): 
#         query = "INSERT INTO channels (name, is_public) VALUES (%s, %s)"
#         params = (self.name, self.is_public)
#         self.server.db.execute_query(query, params)



from Database import Database

class Channel:
    def __init__(self, id, name, is_public):
        self.id = id
        self.name = name
        self.is_public = is_public
        self.messages = []

    @staticmethod
    def get_channels():
        db = Database()
        query = "SELECT * FROM channels"
        try:
            result = db.fetch_data(query, ())
            channels = []
            for row in result:
                id, name, is_public = row
                channel = Channel(id, name, is_public)
                channels.append(channel)
            return channels
        except Exception as e:
            print("Error fetching channels:", e)

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

