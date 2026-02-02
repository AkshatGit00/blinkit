from models.address import Address
from models.inventory import Inventory
from typing import Dict

from models.product import Product
from models.productCategory import ProductCategory

class WareHouse:

    def __init__(self, wareHouse_id:str, address:Address, inventory:Inventory):
        self.wareHouse_id = wareHouse_id
        self.address = address
        self.inventory = inventory

    def add_item_to_inventory(self, product_category_and_count_map:Dict[str, int]):
        for category_id, count in product_category_and_count_map.items():
            productCategory:ProductCategory = self.inventory.get_product_category(category_id)
            if productCategory.products:
                product_name = productCategory.products[-1].product_name
            else: product_name = productCategory.category_name
            self.inventory.add_product(Product(product_name), category_id)

    def remove_item_from_inventory(self, product_category_and_count_map:Dict[str, int]):
        self.inventory.remove_items(product_category_and_count_map)