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


import threading
from ChatServeur import ChatServeur
from Database import Database
from Interface import Interface_login
from ChatClient import ChatClient

def start_server(host, port):

    serveur = ChatServeur(host, port)
    serveur.start()

def start_interface():
    interface = Interface_login()
    interface.background_image()
    interface.enter_username()
    interface.enter_password()
    interface.btn_login()
    interface.btn_forgot_password()
    interface.screen.mainloop()

def start_client(host, port):
    client = ChatClient(host, port)
    client.start()
    
if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8585

    # Lancer le serveur dans un thread
    server_thread = threading.Thread(target=start_server, args=(HOST, PORT))
    server_thread.start()

    # Lancer l'interface dans un autre thread
    interface_thread = threading.Thread(target=start_interface)
    interface_thread.start()

    # Lancer le client dans le thread principal
    start_client(HOST, PORT)

    # Interface_login().screen.mainloop()



