import threading
from ChatServeur import ChatServeur
from ChatClient import ChatClient
from Interface import InterfaceLogin
from Message import Message
from Users import Users

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
    # server_thread.join()  # Attend que le thread du serveur se termine

    # Créer une instance du client
    client = ChatClient(HOST, PORT)

    # Lancer l'interface dans un autre thread
    interface_thread = threading.Thread(target=start_interface, args=(server, client))
    interface_thread.start()
    interface_thread.join()  # Attend que le thread de l'interface se termine

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
