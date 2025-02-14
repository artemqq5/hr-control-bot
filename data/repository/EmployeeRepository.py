from data.SimpleDataBase import SimpleDataBase


class EmployeeRepository(SimpleDataBase):

    def employee(self, employee_id):
        query = "SELECT * FROM `employees` WHERE `employee_id` = %s;"
        return self._select_one(query, (employee_id,))

    def add_employee(self, employee_name):
        query = "INSERT INTO `employees` (`employee_name`) VALUES (%s);"
        return self._insert(query, (employee_name,))

    def employees(self):
        query = "SELECT * FROM `employees` ORDER BY `employee_id` DESC;"
        return self._select(query)

    def delete_employee(self, employee_id):
        query = "DELETE FROM `employees` WHERE `employee_id` = %s;"
        return self._delete(query, (employee_id,))
