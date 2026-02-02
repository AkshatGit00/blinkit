from typing import Dict
from models.productCategory import ProductCategory


class Invoice:

    def __init__(self, order):
        self.order = order

    def generate_invoice(self):
        if not self.order or not self.order.product_category_count_map:
            raise ValueError("Invalid order, can't generate invoice.")
        product_category_count_map:Dict[str, int] = self.order.product_category_count_map
        total_price = 0
        total_tax = 0
        print("---------Product Category ID, Category, Quantity, Price Per Unit, Total Price, Tax--------")
        for category_id, count in product_category_count_map.items():
            category:ProductCategory = self.order.warehouse.inventory.get_product_category(category_id)
            price_per_unit:float = category.price
            total_item_price:float = count*price_per_unit
            tax = total_item_price*0.10 # assuming 10% tax 

            total_price+=total_item_price
            total_tax+=tax

            print(f"---------{category_id}, {category.category_name}, {count}, {price_per_unit}, {total_item_price}, {tax}")

        total_final_price = total_price+total_tax

        print("-------------Total Price, Total Tax, Grand Total---------------")
        print(f"------------{total_price}, {total_tax}, {total_final_price}")