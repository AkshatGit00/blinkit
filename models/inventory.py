from models.product import Product
from models.productCategory import ProductCategory
from typing import Dict

class Inventory:

    def __init__(self):
        self.product_category_list:Dict[str, ProductCategory] = {}

    def add_category(self, category_id:str, category_name:str, price:float):
        product_category = ProductCategory(category_id, category_name, price)
        # we should check that this category is already exist in inventory or not
        self.product_category_list[category_id] = product_category

    def add_product(self, product:Product, category_id:str):
        product_category = self.product_category_list.get(category_id)
        if not product_category:
            return "This category doesn't exist."
        product_category.add_product(product)

    def get_product_category(self, category_id:str):
        if category_id not in self.product_category_list:
            return "This item is not present in the list."
        return self.product_category_list.get(category_id)
    
    def remove_items(self, product_category_and_count_map:Dict[str, int]):
        for category_id, count in product_category_and_count_map.items():
            if category_id not in self.product_category_list:
                continue
            category = self.product_category_list.get(category_id)
            category.remove_product(count)
