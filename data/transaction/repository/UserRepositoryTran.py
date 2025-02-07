from data.TransactionDataBase import TransactionDataBase


class UserRepositoryTransaction(TransactionDataBase):

    def _update_user_status(self, user_role, realname, user_id):
        query = "UPDATE `users` SET `user_role` = %s, `realname` = %s WHERE `user_id` = %s;"
        return self._update(query, (user_role, realname, user_id))

    def _update_access(self, user_id, username, access_uuid):
        query = ("UPDATE `accesses` "
                 "SET `user_id` = %s, `username` = %s, `activated` = CURRENT_TIMESTAMP "
                 "WHERE `access_uuid` = %s AND `activated` is NULL;")
        return self._update(query, (user_id, username, access_uuid))

    # block access for this field in database until transaction end
    def _access(self, access_uuid):
        query = "SELECT * FROM `accesses` WHERE `access_uuid` = %s FOR UPDATE;"
        return self._select_one(query, (access_uuid,))
