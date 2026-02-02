from models.product import Product
from typing import List

class ProductCategory:

    def __init__(self, product_category_id:str, category_name:str, price:float):
        self.product_category_id = product_category_id
        self.category_name = category_name
        self.price = price
        self.products:List[Product] = []

    def add_product(self, product:Product):
        self.products.append(product)

    def remove_product(self, count):
        for i in range(count):
            self.products.pop()

    def get_stock(self):
        return len(self.products)
    
    def get_products(self):
        return self.products
    
    def get_product_count(self):
        return len(self.products)
