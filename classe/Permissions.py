from Database import Database

class Permissions:
    def __init__(self):
        self.db = Database()

    def grant_permission(self, user_id, channel_id, permission_level):
        query = "INSERT INTO permission (user_id, channel_id, permission_level) VALUES (%s, %s, %s)"
        params = (user_id, channel_id, permission_level)
        try:
            permission_id = self.db.execute_query(query, params)
            return permission_id
        except Exception as e:
            print("Error granting permission:", e)
            return None

    def revoke_permission(self, user_id, channel_id):
        query = "DELETE FROM permission WHERE user_id = %s AND channel_id = %s"
        params = (user_id, channel_id)
        try:
            self.db.execute_query(query, params)
            print("Permission revoked successfully.")
        except Exception as e:
            print("Error revoking permission:", e)

    def check_permission(self, user_id, channel_id):
        query = "SELECT permission_level FROM permission WHERE user_id = %s AND channel_id = %s"
        params = (user_id, channel_id)
        try:
            result = self.db.fetch_data(query, params)
            return result[0][0] if result else None
        except Exception as e:
            print("Error checking permission:", e)
            return None



