class User():
    def __init__(self, id, name, access):
        self.id = id
        self.name = name
        self.access = access

class Admin(User):
    def __init__(self, id, name, access, admin):
        super().__init__(id, name, access)
        self.__private_admin = admin