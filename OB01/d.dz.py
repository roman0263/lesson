class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_item_price(self, item_name):
        return self.items.get(item_name)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price


store1 = Store("Три семерки", "Люберцы")
store2 = Store("Бухло Лэнд", "Выхино")
store3 = Store("Мир Жрачки", "Жулебино")

store1.add_item("портвейн 777", 350)
store1.add_item("водяра сносная", 370)

store2.add_item("вискарь 0,5 ", 750)
store2.add_item("коньяк 5 звезд", 800)

store3.add_item("джин", 1200)
store3.add_item("вино красное ", 2500)

store1.add_item("чипсы", 100)
print("Цена чипсов:", store1.get_item_price("чипсы"))

store1.update_item_price("чипсы", 120)
print("Новая цена чипсов:", store1.get_item_price("чипсы"))

store1.remove_item("чипсы")
print("Цена чипсов после удаления:", store1.get_item_price("чипсы"))

for item_name, price in store1.items.items():
    print(f"{item_name}: {price} руб.")


