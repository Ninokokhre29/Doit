class cart:
    def __init__(self):
        self.shop_cart = {}

    def add_item(self, item_name, qty, price):
        if item_name in self.shop_cart:
            self.shop_cart[item_name]["quantity"] += qty
        else:
            self.shop_cart[item_name] = {"price": price, "quantity": qty}

    def remove_item(self, item_name):
        if item_name in self.shop_cart:
            del self.shop_cart[item_name]
        else:
            return f"{item_name} is not in the cart"

    def calculate_total(self):
        if not self.shop_cart:
            return "The cart is empty"
        else:
            total_quantity = sum(item["quantity"] for item in self.shop_cart.values())
            return f"Current items in the cart: {total_quantity}"

    def current_items(self):
        return f"Right now in the cart we have: {self.shop_cart}"


cart = cart()
cart.add_item("პური", 2, 5)
cart.add_item("კარაქი", 1, 5)
cart.add_item("წყალი", 6, 5)
cart.add_item("ზეთი", 2, 5)
print(cart.shop_cart)
print(cart.current_items())
print(cart.calculate_total())
cart.remove_item("ზეთი")
print(cart.current_items())
print(cart.calculate_total())