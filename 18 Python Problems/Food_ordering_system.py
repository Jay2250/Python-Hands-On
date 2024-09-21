# OOPs Assignment : Hands on
# online food ordering system

class FoodItem:
    def __init__(self, food_name, price, category):
        self.food_name = food_name
        self.price = price
        self.category = category

    def display_info(self):
        print(f"{self.name},{self.price},{self.category}")


class Customer:

    def __init__(self, cust_name, cust_id):
        self.cust_name = cust_name
        self.cust_id = cust_id
        self.order_history = []

    def place_order(self, food_item: FoodItem, quantity):
        total_price = food_item.price * quantity
        order = {
            'food_item': food_item.food_name,
            'quantity': quantity,
            'total_price': total_price
        }
        self.order_history.append(order)
        print(
            f"The Order History is as follow : Name = {food_item.food_name}, Quantity = {quantity}, Total Price : {total_price}")

    def view_order_history(self):
        print(self.order_history)


class Regular_Customer(Customer):

    def __init__(self, cust_name, cust_id, discount=0.05):
        super().__init__(cust_name, cust_id)
        self.discount = discount

    def place_order(self, food_item: FoodItem, quantity):
        discounted_price = (food_item.price * quantity) - \
            (food_item.price * quantity * self.discount)
        order = {
            'food_item': food_item.food_name,
            'quantity': quantity,
            'total_price': discounted_price
        }
        self.order_history.append(order)
        print(
            f"The Order History is as follow : Name = {food_item.food_name}, Quantity = {quantity}, Total Price : {discounted_price}")


class Premium_Customer(Customer):

    def __init__(self, cust_name, cust_id, discount=0.15, priority_delivery=True):
        super().__init__(cust_name, cust_id)
        self.discount = discount
        self.priority_delivery = priority_delivery

    def place_order(self, food_item: FoodItem, quantity):
        discounted_price = (food_item.price * quantity) - \
            (food_item.price * quantity * self.discount)
        order = {
            'food_item': food_item.food_name,
            'quantity': quantity,
            'total_price': discounted_price,
            'priority': self.priority_delivery
        }
        self.order_history.append(order)
        print(
            f"The Order History is as follow : Name = {food_item.food_name}, Quantity = {quantity}, Total Price : {discounted_price}")
        if self.priority_delivery:
            print("with Fast Delivery")
        else:
            print("Normal Delivery")


class Restaurant:

    def __init__(self):
        self.menu = []
        self.customers = []

    def add_food_item(self, food_item: FoodItem):
        self.menu.append(food_item)

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def display_menu(self):
        for i in self.menu:
            print(i.food_name)

    def display_customer(self):
        for i in self.customers:
            print(i.cust_name)


soup = FoodItem('soup', 10, 'starter')
pasta = FoodItem('pasta', 25, 'main course')
noodles = FoodItem('noodles', 30, 'main course')
regular_customer = Regular_Customer('Sammak', 1)
premium_customer = Premium_Customer('Bapat', 1, priority_delivery=False)
regular_customer.place_order(pasta, 4)
premium_customer.place_order(noodles, 20)
# regular_customer.view_order_history()
# premium_customer.view_order_history()

sneh = Restaurant()
sneh.add_food_item(soup)
sneh.add_food_item(pasta)
sneh.add_food_item(noodles)

sneh.add_customer(regular_customer)
sneh.add_customer(premium_customer)

sneh.display_customer()
sneh.display_menu()
