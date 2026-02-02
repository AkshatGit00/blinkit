from typing import Dict
from models.order import Order
from models.user import User
from models.warehouse import WareHouse


class OrderService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OrderService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.orders:Dict[str, Order] = {}

    def create_order(self, order_id:str, user:User, wareHouse:WareHouse):
        if order_id in self.orders:
            return "This order id is already created."
        order:Order = Order(user, wareHouse)
        self.orders[order_id] = order
        user.add_orders(order_id)
        return order

    def remove_order(self, order_id:str):
        if order_id not in self.orders:
            return "This order is not placed yet."
        del self.orders[order_id]

    def get_order(self, order_id:str):
        if order_id not in self.orders:
            return "This order is not present."
        return self.orders.get(order_id)

