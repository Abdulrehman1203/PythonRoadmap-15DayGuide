from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def complete(self):
        pass


class CreditCardPayment(PaymentMethod):
    def authorize(self):
        print("Authorizing Credit Card Payment")

    def process(self):
        print("Processing Credit Card Payment")

    def complete(self):
        print("Completing Credit Card Payment")


class PayPalPayment(PaymentMethod):
    def authorize(self):
        print("Authorizing PayPal Payment")

    def process(self):
        print("Processing PayPal Payment")

    def complete(self):
        print("Completing PayPal Payment")


credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

# Using the CreditCardPayment method
print("Using Credit Card Payment:")
credit_card_payment.authorize()
credit_card_payment.process()
credit_card_payment.complete()

print("\nUsing PayPal Payment:")
# Using the PayPalPayment method
paypal_payment.authorize()
paypal_payment.process()
paypal_payment.complete()
