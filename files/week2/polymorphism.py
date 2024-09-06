class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("This method should be overridden by subclasses")


class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")


class BitcoinPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Processing Bitcoin payment of ${amount}")


def process_transaction(payment_method, amount):
    payment_method.process_payment(amount)


# Examples
payment1 = CreditCardPayment()
payment2 = PayPalPayment()
payment3 = BitcoinPayment()

# Processing payments
process_transaction(payment1, 100)
process_transaction(payment2, 200)
process_transaction(payment3, 300)
