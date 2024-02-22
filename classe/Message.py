# from ChatServeur import ChatServeur

class Message:
    TEXT_MESSAGE = "text"
    EMOJI_MESSAGE = "emoji"
    VOCAL_MESSAGE = "vocal"

    def __init__(self, server, user_id, content, timestamp, channel_id, message_type=TEXT_MESSAGE):
        self.server = server
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp
        self.channel_id = channel_id
        self.message_type = message_type  # Attribut pour indiquer le type de message

    def send_message(self):
        self.server.insert_message(self.user_id, self.content, self.timestamp, self.channel_id, self.message_type)

    def get_reactions(self, message_id):
        return self.server.get_reactions_for_message(message_id)

    def to_dict(self):
        return {
            "author": self.user_id,
            "content": self.content,
            "timestamp": self.timestamp,
            "channel_id": self.channel_id,
            "message_type": self.message_type
        }

    def set_message_type(self, message_type):
        if message_type in {self.TEXT_MESSAGE, self.EMOJI_MESSAGE, self.VOCAL_MESSAGE}:
            self.message_type = message_type
        else:
            raise ValueError("Invalid message type")

    @staticmethod
    def from_dict(server, data):
        user_id = data["author"]
        content = data["content"]
        timestamp = data["timestamp"]
        channel_id = data["channel_id"]
        message_type = data.get("message_type", Message.TEXT_MESSAGE)
        return Message(server, user_id, content, timestamp, channel_id, message_type)
    
    def save_to_server(self):
        query = "INSERT INTO messages (user_id, content, timestamp, channel_id, message_type) VALUES (%s, %s, %s, %s, %s)"
        params = (self.user_id, self.content, self.timestamp, self.channel_id, self.message_type)
        self.server.execute_query(query, params)





    # @staticmethod
    # def get_messages_for_channel(channel_id):
    #     db = Database()
    #     query = "SELECT * FROM messages WHERE channel_id = %s"
    #     params = (channel_id,)
    #     return db.fetch_data(query, params)


# def display(self):
#         return f"[{self.timestamp}] {self.user.username}: {self.content}"