import pytest

from pay.processor import PaymentProcessor

API_KEY = "DUMMY_API_KEY" # Preliminary version, never expose the API Key.


def test_api_key_invalid() -> None:
    with pytest.raises(ValueError):
        processor = PaymentProcessor(1)
        processor.charge("1249190007575069", 12, 2024, 100)


def test_card_valid_date() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.validate_card("1249190007575069", 12, 2024)


def test_card_invalid_date() -> None:
    processor = PaymentProcessor(API_KEY)
    assert not processor.validate_card("1249190007575069", 12, 1900)


def test_invalid_luhn() -> None:
    processor = PaymentProcessor(API_KEY)
    assert not processor.luhn_checksum("1249190007575000")


def test_valid_luhn() -> None:
    processor = PaymentProcessor(API_KEY)
    assert processor.luhn_checksum("1249190007575069")


def test_charge_card_valid() -> None:
    processor = PaymentProcessor(API_KEY)
    processor.charge("1249190007575069", 12, 2025, 100)


def test_charge_card_invalid() -> None:
    processor = PaymentProcessor(API_KEY)
    with pytest.raises(ValueError):
        processor = PaymentProcessor(API_KEY)
        assert processor.charge("1249190007575068", 12, 2025, 100)