from data.SimpleDataBase import SimpleDataBase


class UserRepository(SimpleDataBase):

    def user(self, user_id):
        query = "SELECT * FROM `users` WHERE `user_id` = %s;"
        return self._select_one(query, (user_id,))

    def add_user(self, user_id, firstname, username, lang):
        query = "INSERT INTO `users` (`user_id`, `firstname`, `username`, `lang`) VALUES (%s, %s, %s, %s);"
        return self._insert(query, (user_id, firstname, username, lang))

    def registered_users(self):
        query = "SELECT * FROM `users` WHERE `user_role` = 'head' ORDER BY `join` DESC;"
        return self._select(query)

    def delete_user_role(self, user_id):
        query = "UPDATE `users` SET `user_role` = NULL WHERE `user_id` = %s;"
        return self._update(query, (user_id,))

    def admins(self):
        query = "SELECT * FROM `users` WHERE `user_role` = 'admin';"
        return self._select(query)
