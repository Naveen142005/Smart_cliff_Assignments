class Cart:
    def __init__(self, cart_list):
        self.cart_list = cart_list

    def add_product(self, product):

        self.cart_list.append(product)


    def remove_product(self, product_name):
        for product in self.cart_list:
            if product.name == product_name:
                self.cart_list.remove(product)
                break
        else:
            return False
        return True

    def calculate_total_price(self):
        total = 0
        for product in self.cart_list:
            total += product.get_price()
        return total

    def display(self):
        for product in self.cart_list:
            print(f"{product.get_name()} - ₹{product.get_price()}")
