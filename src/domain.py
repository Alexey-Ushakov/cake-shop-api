from __future__ import annotations
from dataclasses import dataclass
from typing import Self

@dataclass(frozen=True)
class Money:
    amount: int
    currency: str = 'RUB'

    def __post_init__(self) -> None:
        if self.amount < 0:
            raise ValueError("Amount cannot be negative")

    def __add__(self, other: Money) -> Self:
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: Money) -> Self:
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("Different currencies")
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, quantity: int) -> Self:
        if not isinstance(quantity, int):
            raise TypeError("Can only multiply Money by int")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        return Money(self.amount * quantity, self.currency)