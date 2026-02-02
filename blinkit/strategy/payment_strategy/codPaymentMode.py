from strategy.paymentMode import PaymentMode


class CODPayemntMode(PaymentMode):

    def make_payment(self):
        return True