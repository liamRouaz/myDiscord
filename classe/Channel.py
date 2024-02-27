from ChatServeur import ChatServeur

class Channel:
    def __init__(self,host, port, id, name, is_public):
        self.id = id
        self.name = name
        self.is_public = is_public
        self.messages = []
        self.server = ChatServeur(host, port)
        
    def create_channel(self):
        self.server.insert_channel(self.name, self.is_public)

    # def create_channel(self, channel_id, name, is_public):
    #     channel = Channel(channel_id, name, is_public)
    #     self.channels.append(channel) 

    @staticmethod
    def create_channels():
        # Créer des canaux
        ChatServeur().insert_channel("sport", "public") # Si sa marche pas remétre is_public=True
        ChatServeur().insert_channel("cinéma", "public")
        ChatServeur().insert_channel("manga", "public")

    @staticmethod
    def get_channels():
        return ChatServeur().get_channels()
    
    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

    def save_to_server(self): 
        query = "INSERT INTO channels (name, is_public) VALUES (%s, %s)"
        params = (self.name, self.is_public)
        self.server.execute_query(query, params)




