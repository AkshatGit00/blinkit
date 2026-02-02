from strategy.paymentMode import PaymentMode


class CardPayemntMode(PaymentMode):

    def make_payment(self):
        return True