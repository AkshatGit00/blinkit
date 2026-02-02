from typing import Dict

from models.inventory import Inventory
from models.productCategory import ProductCategory

class Cart:

    def __init__(self):
        self.product_category_id_count_map:Dict[str, int] = {}

    def add_item_in_cart(self, product_category_id:str, count:int, inventory:Inventory):
        product_category_count:int = inventory.get_product_category(product_category_id).get_product_count()
        if product_category_count < count:
            raise ValueError("You can't add more than available count.")
        if product_category_id in self.product_category_id_count_map:
            self.product_category_id_count_map[product_category_id] = self.product_category_id_count_map.get(product_category_id) + count
        else:
            self.product_category_id_count_map[product_category_id] = count
        return "Added Successfully."
    
    def remove_items_from_cart(self, product_category_id:str, count:int):
        if product_category_id not in self.product_category_id_count_map:
            return "This item is not exist in cart."
        existing_item_quantity = self.product_category_id_count_map.get(product_category_id)
        if existing_item_quantity < count:
            return "Item quantity can't be more than existing cart quantity."
        if existing_item_quantity-count==0:
            self.product_category_id_count_map.erase(product_category_id)
        self.product_category_id_count_map[product_category_id] = existing_item_quantity - count
        return "Remove Successfully."
    
    def get_cart_items(self):
        return self.product_category_id_count_map
    
    def empty_cart(self):
        self.product_category_id_count_map = {}

    
        