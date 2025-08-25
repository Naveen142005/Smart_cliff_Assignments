class Product:
    def __init__(self, id_, name, price):
        self.id = id_
        self.name = name
        self.price = price
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price