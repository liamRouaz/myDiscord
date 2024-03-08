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
            channels = {}
            for row in result:
                id, name, is_public = row
                channel = Channel(id, name, is_public)
                channels[name] = channel
            return channels
        except Exception as e:
            print("Error fetching channels:", e)

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        try:
            db = Database()
            query = "SELECT content FROM messages WHERE channel_id = %s"
            result = db.fetch_data(query, (self.id,))
            messages = [row[0] for row in result]  # Fetching only content from database
            return messages
        except Exception as e:
            print("Error fetching messages for channel:", e)
            return []