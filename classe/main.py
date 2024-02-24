import threading
from ChatClient import ChatClient
from Interface import InterfaceLogin

def start_interface():
    interface = InterfaceLogin()
    interface.screen.mainloop()

def start_client_after_login(email, password, host, port):
    client = ChatClient(host, port)
    client.connect_to_server(email, password)

if __name__ == "__main__":
    HOST = "localhost"
    PORT = 8585

    # Créer une instance du client
    chat_client = ChatClient(HOST, PORT)

    # Lancer l'interface dans un autre thread
    interface_thread = threading.Thread(target=start_interface)
    interface_thread.start()
    interface_thread.join()  # Attend que le thread de l'interface se termine





