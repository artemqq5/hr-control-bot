from data.SimpleDataBase import SimpleDataBase


class AccessRepository(SimpleDataBase):

    def generate_access(self, access_uuid, realname):
        query = "INSERT INTO `accesses` (`access_uuid`, `realname`) VALUES (%s, %s);"
        return self._insert(query, (access_uuid, realname))
