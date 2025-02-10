from data.SimpleDataBase import SimpleDataBase


class EmployeeRepository(SimpleDataBase):

    def employee(self, employee_id):
        query = "SELECT * FROM `employees` WHERE `employee_id` = %s;"
        return self._select_one(query, (employee_id,))

    def add_employee(self, employee_id, employee_name, employee_position):
        query = "INSERT INTO `users` (`employee_id`, `employee_name`, `employee_position`) VALUES (%s, %s, %s);"
        return self._insert(query, (employee_id, employee_name, employee_position))

    def employees(self):
        query = "SELECT * FROM `employees`;"
        return self._select(query)

    def delete_employee(self, employee_id):
        query = "DELETE * FROM `employees` WHERE `employee_id` = %s;"
        return self._delete(query, (employee_id,))
