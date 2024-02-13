class Product:
    def __init__(self, name_product, price, amount):
        self.name_product= name_product
        self.price= price
        self.amount= amount
class Basket():
    def __init__(self):
        self.list_product= []
    def add_product(self, name_product):
        return self.list_product.append(name_product)
    def remove_product(self, name_product):
        return self.list_product.remove(name_product)
    def calculate_value(self):
        total_value= 0
        for product in self.list_product:
            total_value += product.price * product.amount
        return total_value


product1 = Product("Laptop", 1500, 1)
product2 = Product("Smartphone", 800, 2)

basket = Basket()
basket.add_product(product1)
basket.add_product(product2)

print("Total value of the basket:", basket.calculate_value())