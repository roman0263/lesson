class User():
    def __init__(self, user_id, name, level='user'):
        self.__id = user_id
        self.__name = name
        self.__level = level

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__level

    def set_name(self, name):
        self.__name = name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.__level = "admin"

    def add_user(self, user_list, user):
        user_list.append(user)
        print(f"пользователь добавлен")

    def remove_user(self, user_list, user):
        user_list.remove(user)
        print(f"пользователь удален")

user_list = []
admin = Admin("99", "Roman")
user1 = User("1", "Igor")
user2 = User("2", "Oleg")

print(user1.get_name())
print(user2.get_name())
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)
