from models.address import Address
from models.cart import Cart


class User:

    def __init__(self, user_id:str, user_name:str, address:Address):
        self.user_id = user_id
        self.user_name = user_name
        self.address = address
        self.order_ids = set() # ig we should contain order obj here instead of order id
        self.user_cart_details:Cart = Cart()

    def get_user_cart_details(self):
        return self.user_cart_details
    
    def add_orders(self, order_id):
        self.order_ids.add(order_id)