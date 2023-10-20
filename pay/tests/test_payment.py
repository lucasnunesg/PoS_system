import pytest
from pytest import MonkeyPatch

from pay.order import LineItem, Order
from pay.payment import pay_order


class PaymentProcessorMock:
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        print(f"Charging {card} with amount ${amount/100:.2f}.")


def test_pay_order(monkeypatch: MonkeyPatch) -> None:
    def charge_mock(self, card: int, month: int, year: int, amount: int):
        pass

    inputs = ["1249190007575069", "12", "2024"]
    monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    pay_order(order, PaymentProcessorMock())


def test_pay_order_invalid(monkeypatch: MonkeyPatch) -> None:
    with pytest.raises(ValueError):
        inputs = ["1249190007575069", 12, 2024]
        monkeypatch.setattr("builtins.input", lambda _: inputs.pop(0))
        order = Order()
        pay_order(order, PaymentProcessorMock())
