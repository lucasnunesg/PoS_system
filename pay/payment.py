from typing import Protocol

from pay.order import Order


class PaymentProcessor(Protocol):
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        """Charges the card with the amount"""


def pay_order(order: Order, processor: PaymentProcessor):
    if order.total == 0:
        raise ValueError("Can't pay an empty order.")
    card = input("Please input your card number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the carde expiry year: "))
    processor.charge(card, month, year, amount=order.total)
    order.pay()
