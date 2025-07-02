class Classey:
    varia = 2

    def method(self):
        print(self.varia)

object_one = Classey()
object_two = Classey()
object_one.varia = 3
object_two.varia = 5
print(object_one.varia)
print(object_two.varia)

class Transport:
    def __init__(self, air, water):
        self.air = air
        self.water = water

obj_transport = Transport("Emirates", "Konda")
obj2 = Transport("Jet", "Ship")
print(obj_transport.air, obj_transport.water)
print(obj2.air, obj2.water)

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x = Person("Jane", "Wamui")
y = Person("Dake", "Bouy")
x.printname()
y.printname()

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break

    def calculate_Total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return total

cart = ShoppingCart()
cart.add_item("Kiwi", 15)
cart.add_item("Orange", 10)
cart.add_item("Mango", 20)

print("Current items in cart")
for item in cart.items:
    print(item[0], "-", item[1])

total_qty = cart.calculate_Total()
print("Total Quantity:", total_qty)