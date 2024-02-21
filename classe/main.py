# if __name__ == "__main__":
#     from ChatServeur import ChatServeur
#     from Database import Database
#     from Interface import Interface_login

#     HOST = "localhost"
#     PORT = 5555

#     # Interface = 'chat_app.db'
#     serveur = ChatServeur(HOST, PORT)
#     # Interface = Interface_login()
#     # database = Database()   
#     serveur.start()


# import threading
# from ChatServeur import ChatServeur
# from Database import Database
# from Interface import InterfaceLogin
# from ChatClient import ChatClient

# def start_server(host, port):
#     serveur = ChatServeur(host, port)
#     serveur.start()

# def start_interface():
#     interface = InterfaceLogin()  # Initialiser l'interface
#     interface.background_image()
#     interface.enter_email()  # Ajouter les champs email et mot de passe
#     interface.enter_password()
#     interface.btn_login()  # Ajouter le bouton de connexion
#     interface.btn_forgot_password()
#     interface.screen.mainloop()

# def start_client(host, port):
#     client = ChatClient(host, port)
#     client.start()

# if __name__ == "__main__":
#     HOST = "localhost"
#     PORT = 8585

#     # Lancer le serveur dans un thread
#     server_thread = threading.Thread(target=start_server, args=(HOST, PORT))
#     server_thread.start()

#     # Lancer l'interface dans un autre thread
#     interface_thread = threading.Thread(target=start_interface)
#     interface_thread.start()

#     # Lancer le client dans le thread principal
#     start_client(HOST, PORT)


#     # Interface_login().screen.mainloop()



import threading
from ChatServeur import ChatServeur
from ChatClient import ChatClient
from Interface import InterfaceLogin

def start_server(host, port):
    serveur = ChatServeur(host, port)
    serveur.start()

def start_interface(chat_server, chat_client):
    interface = InterfaceLogin(chat_server, chat_client)
    interface.screen.mainloop()

def start_client_after_login(email, password, host, port):
    client = ChatClient(host, port)
    client.connect_to_server(email, password)

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8585

    # Créer une instance du serveur
    server = ChatServeur(HOST, PORT)

    # Lancer le serveur dans un thread
    server_thread = threading.Thread(target=start_server, args=(HOST, PORT))
    server_thread.start()

    # Créer une instance du client
    client = ChatClient(HOST, PORT)

    # Lancer l'interface dans un autre thread
    interface_thread = threading.Thread(target=start_interface, args=(server, client))
    interface_thread.start()



# import threading
# from ChatServeur import ChatServeur
# from ChatClient import ChatClient
# from Interface import InterfaceLogin

# def main():
#     HOST = "localhost"
#     PORT = 8585

#     # Créer une instance du serveur
#     server = ChatServeur(HOST, PORT)

#     # Créer une instance du client
#     client = ChatClient(HOST, PORT)

#     # Créer une instance de l'interface
#     interface = InterfaceLogin(server, client)

#     # Démarrer le serveur dans un thread
#     server_thread = threading.Thread(target=server.start)
#     server_thread.start()

#     # Démarrer le client
#     client.start()

#     # Démarrer l'interface en boucle
#     interface.screen.mainloop()

# if __name__ == "__main__":
#     main()
