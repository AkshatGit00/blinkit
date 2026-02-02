from strategy.paymentMode import PaymentMode


class UPIPayemntMode(PaymentMode):

    def make_payment(self):
        return True