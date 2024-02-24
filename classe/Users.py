from ChatServeur import ChatServeur

class Users:
    def __init__(self, first_name, last_name, email, password, host, port):
        self.server = ChatServeur(host, port)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.permis_channels = []

    
    def create_user(self, user_info):
        last_name = user_info.get("last_name")
        email = user_info.get("email")
        password = user_info.get("password")
        if last_name and email and password:
            self.register_user(last_name, email, password)
        else:
            print("Informations utilisateur incomplètes.")

    def add_permis_channel(self, channel):
        self.permis_channels.append(channel)

    def is_permis_channel(self, channel):
        return channel in self.permis_channels  

    def save_to_server(self):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
        params = (self.first_name, self.last_name, self.email, self.password)
        self.server.execute_query(query, params)

    def register_user(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.save_to_server()




