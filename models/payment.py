from strategy.paymentMode import PaymentMode


class Payment:

    def __init__(self, payment_mode:PaymentMode):
        self.payment_mode = payment_mode

    def make_payment(self)->bool:
        return self.payment_mode.make_payment()