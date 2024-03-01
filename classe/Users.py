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







# from ChatServeur import ChatServeur
# from Database import Database

# class Users:
#     def __init__(self, host, port):
#         self.server = ChatServeur(host, port)
#         self.db = Database()
#         self.permis_channels = []

#     def create_user(self, first_name, last_name, email, password):
#         if first_name and last_name and email and password:
#             self.register_user(first_name, last_name, email, password)
#         else:
#             print("Informations utilisateur incomplètes.")

#     def add_permis_channel(self, channel):
#         self.permis_channels.append(channel)

#     def is_permis_channel(self, channel):
#         return channel in self.permis_channels
    
#     def register_user(self, first_name, last_name, email, password):
#         query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
#         params = (first_name, last_name, email, password)
#         try:
#             user_id = self.db.execute_query(query, params)
#             if user_id:
#                 print("User inserted successfully with ID:", user_id)
#             else:
#                 print("Failed to insert user into database.")
#         except Exception as e:
#             print("Error inserting user into database:", e)

    
    # def save_to_server(self):
    #     query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
    #     params = (self.first_name, self.last_name, self.email, self.password)
    #     self.server.db.execute_query(query, params)

    # def register_user(self, first_name, last_name, email, password):
    #     self.first_name = first_name
    #     self.last_name = last_name
    #     self.email = email
    #     self.password = password
    #     self.save_to_server()


# from Database import Database

# class Users:
#     def __init__(self):
#         self.db = Database()

#     def register_user(self, user_info):
#         first_name = user_info.get("first_name")
#         last_name = user_info.get("last_name")
#         email = user_info.get("email")
#         password = user_info.get("password")
        
#         if not (first_name and last_name and email and password):
#             print("Incomplete user information.")
#             return

#         query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
#         params = (first_name, last_name, email, password)

#         try:
#             self.db.execute_query(query, params)
#             print("User registered successfully.")
#         except Exception as e:
#             print("Error registering user:", e)


