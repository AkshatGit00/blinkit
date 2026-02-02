from models.address import Address
from models.invoice import Invoice
from models.orderStatus import OrderStatus
from models.payment import Payment
from models.user import User
from models.warehouse import WareHouse
from strategy.paymentMode import PaymentMode
from strategy.payment_strategy.upiPaymentMode import UPIPayemntMode


class Order:

    def __init__(self, user:User, warehouse:WareHouse):
        self.user:User = user
        self.warehouse:WareHouse = warehouse
        self.invoice:Invoice = Invoice(self)
        # self.payment:Payment = Payment()
        self.delivery_address:Address = user.address
        self.product_category_count_map = user.get_user_cart_details().get_cart_items()
        self.order_status = OrderStatus.PENDING

    def check_out(self):

        # update inventory
        self.order_status = OrderStatus.PROCESSING
        self.warehouse.remove_item_from_inventory(self.product_category_count_map)

        #payment
        is_payment_success:bool = self.make_payment(UPIPayemntMode())

        #handle order -> success/failed
        if is_payment_success:
            self.order_status = OrderStatus.COMPLETED
            self.user.get_user_cart_details().empty_cart()
        else:
            self.order_status = OrderStatus.FAILED
            self.warehouse.add_item_to_inventory(self.product_category_count_map)

        return f"Order status: {self.order_status}"
    
    def make_payment(self, payment_mode:PaymentMode):
        return payment_mode.make_payment()

    def generate_invoice(self):
        self.invoice.generate_invoice()

    def get_order_status(self):
        return self.order_status
    
    def cancel_order(self):
        if self.order_status == OrderStatus.COMPLETED:
            return "Can't be cancelled a completed order."
        self.order_status = OrderStatus.CANCELLED
        # make refund for cancel order
