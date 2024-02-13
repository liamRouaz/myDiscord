class Message:
    TEXT_MESSAGE = "text"
    EMOJI_MESSAGE = "emoji"
    VOCAL_MESSAGE = "vocal"

    def __init__(self, user_id, content, timestamp, channel_id, message_type=TEXT_MESSAGE):
        self.user_id = user_id
        self.content = content
        self.timestamp = timestamp
        self.channel_id = channel_id
        self.message_type = message_type  # Attribut pour indiquer le type de message

    def to_dict(self):
        return {
            "user_id": self.user_id,
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

    @classmethod
    def from_dict(cls, data):
        user_id = data["user_id"]
        content = data["content"]
        timestamp = data["timestamp"]
        channel_id = data["channel_id"]
        message_type = data.get("message_type", cls.TEXT_MESSAGE)  # Si aucun type de message n'est spécifié
        return cls(user_id, content, timestamp, channel_id, message_type)


