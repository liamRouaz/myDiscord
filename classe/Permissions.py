from Database import Database

class Permissions:
    def __init__(self):
        self.db = Database()

    def grant_permission(self, user_id, channel_id, permission_level):
        query = "INSERT INTO permissions (user_id, channel_id, permission_level) VALUES (%s, %s, %s)"
        params = (user_id, channel_id, permission_level)
        try:
            permission_id = self.db.execute_query(query, params)
            return permission_id
        except Exception as e:
            print("Error granting permission:", e)
            return None

    def revoke_permission(self, user_id, channel_id):
        query = "DELETE FROM permissions WHERE user_id = %s AND channel_id = %s"
        params = (user_id, channel_id)
        try:
            self.db.execute_query(query, params)
            print("Permission revoked successfully.")
        except Exception as e:
            print("Error revoking permission:", e)

    def check_permission(self, user_id, channel_id):
        query = "SELECT permission_level FROM permissions WHERE user_id = %s AND channel_id = %s"
        params = (user_id, channel_id)
        result = self.db.fetch_data(query, params)
        return result[0][0] if result else None


# import mysql.connector
# from Database import Database

# class Permissions:
#     def __init__(self):
#         self.db = Database()

#     def grant_remote_access(self):
#         try:
#             connection = mysql.connector.connect(
#                 host="10.10.94.117",  
#                 user="root",       
#                 password="soso",  
#                 database="myDiscord"   
#             )

#             # Commande pour accorder les privilèges à distance à l'utilisateur
#             cursor = connection.cursor()
#             cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'soso' WITH GRANT OPTION;")
#             cursor.execute("FLUSH PRIVILEGES;")
#             print("Remote access granted successfully.")
            
#             cursor.close()
#             connection.close()
#         except mysql.connector.Error as err:
#             print("Error granting remote access:", err)

# # Exemple d'utilisation
# if __name__ == "__main__":
#     permissions = Permissions()
#     permissions.grant_remote_access()

