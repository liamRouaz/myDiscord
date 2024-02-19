import socket

# Adresse IP et port du serveur
HOST = 'localhost'
PORT = 5555

# Créer un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Se connecter au serveur
client_socket.connect((HOST, PORT))

# Définir les attributs channel_id et user_id sur le client_socket
client_socket.channel_id = 'votre_channel_id'
client_socket.user_id = 'votre_user_id'

# Envoyer des données au serveur
message = "Bonjour, serveur!"
client_socket.sendall(message.encode())

# Attendre la réponse du serveur
response = client_socket.recv(1024).decode()
print("Réponse du serveur:", response)

# Fermer la connexion
client_socket.close()


