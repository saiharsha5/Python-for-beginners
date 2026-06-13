class Employee:
    def __init__(self, emp_id, emp_name):
        self.emp_id = emp_id
        self.emp_name = emp_name
class FoodItem:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price
class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.order_items = []

    def add_items(self, food_item):
        self.order_items.append(food_item)

    def calculate_total(self):
        return sum(item.price for item in self.order_items)

    def generate_bill(self, employee):
        print("=" * 50)
        print("            CORPORATE CAFETERIA BILL")
        print("=" * 50)

        print(f"\nEmployee ID     : {employee.emp_id}")
        print(f"Employee Name   : {employee.emp_name}\n")

        print("-" * 50)
        print(f"{'Item':<30}{'Price'}")
        print("-" * 50)

        for item in self.order_items:
            print(f"{item.item_name:<30}₹{item.price}")
        print("-" * 50)
        print(f"\n{'Total Amount':<30}₹{self.calculate_total()}")
        print(f"\n{'Payment Status':<30}PAID")
        print("\n" + "=" * 50)

class Cafeteria:
    def __init__(self):
        self.menu = []

    def add_food_item(self, item):
        self.menu.append(item)

    def display_menu(self):
        print("MENU")
        print("-" * 30)
        for item in self.menu:
            print(f"{item.item_name:<20} ₹{item.price}")
        print("-" * 30)

cafeteria = Cafeteria()

cafeteria.add_food_item(FoodItem("Coffee", 40))
cafeteria.add_food_item(FoodItem("Sandwich", 80))
cafeteria.add_food_item(FoodItem("Brownie", 60))

employee = Employee("E101", "Ryan")

order = Order("O101")
order.add_items(cafeteria.menu[0])
order.add_items(cafeteria.menu[1])
order.add_items(cafeteria.menu[2])

order.generate_bill(employee)