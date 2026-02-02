from abc import ABC, abstractmethod

class PaymentMode(ABC):

    @abstractmethod
    def make_payment(self)->bool:
        pass