from pay.order import Order
from pay.processor import PaymentProcessor


def pay_order(order: Order):
    if order.total == 0:
        raise ValueError("Can't pay an empty order.")
    card = input("Please input your card number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the carde expiry year: "))
    payment_processor = PaymentProcessor("DUMMY_API_KEY")
    payment_processor.charge(card, month, year, amount=order.total)
    order.pay()