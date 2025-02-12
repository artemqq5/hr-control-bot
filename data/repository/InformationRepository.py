from data.SimpleDataBase import SimpleDataBase


class InformationRepository(SimpleDataBase):

    def create(self, employee_id, employee_name, desc, user_id, username, realname):
        query = "INSERT INTO `informations` (`employee_id`, `employee_name`, `desc`, `user_id`, `username`, `realname`) VALUES (%s, %s, %s, %s, %s, %s);"
        return self._insert(query, (employee_id, employee_name, desc, user_id, username, realname))

    def informations(self):
        query = "SELECT * FROM `informations`;"
        return self._select(query)

    def information(self, _id):
        query = "SELECT * FROM `informations` WHERE `id` = %s;"
        return self._select_one(query, (_id,))
