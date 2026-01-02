import pytest
from src.domain import Money

# 1. Создание — успешное и с валидацией
def test_create_money_success():
    money = Money(10000, 'RUB')
    assert money.amount == 10000
    assert money.currency == 'RUB'

def test_create_money_with_default_currency():
    money = Money(5000)
    assert money.currency == 'RUB'

def test_create_money_negative_amount_raises():
    with pytest.raises(ValueError, match="Amount cannot be negative"):
        Money(-100)


# 2. Иммутабельность — попытка изменить поле
def test_money_is_immutable():
    money = Money(10000)
    with pytest.raises(AttributeError):  # dataclass frozen raises FrozenInstanceError, но часто как AttributeError
        money.amount = 20000
    with pytest.raises(AttributeError):
        money.currency = 'USD'


# 3. Равенство и хэш (очень важно для VO!)
def test_equal_money_objects_are_equal():
    a = Money(10000, 'RUB')
    b = Money(10000, 'RUB')
    assert a == b
    assert hash(a) == hash(b)  # критично для использования в set/dict

def test_different_amount_not_equal():
    a = Money(10000)
    b = Money(20000)
    assert a != b

def test_different_currency_not_equal():
    a = Money(10000, 'RUB')
    b = Money(10000, 'USD')
    assert a != b


# 4. Сложение
def test_add_same_currency():
    a = Money(10000)
    b = Money(2500)
    result = a + b
    assert result == Money(12500)
    assert result.currency == 'RUB'

def test_add_different_currency_raises():
    a = Money(10000, 'RUB')
    b = Money(100, 'USD')
    with pytest.raises(ValueError, match="Different currencies"):
        a + b

# 5. Вычитание
def test_subtract_same_currency():
    a = Money(10000)
    b = Money(3000)
    result = a - b
    assert result == Money(7000)

def test_subtract_different_currency_raises():
    a = Money(10000, 'RUB')
    b = Money(100, 'USD')
    with pytest.raises(ValueError):
        a - b


# 6. Умножение на количество
def test_multiply_by_positive_int():
    price = Money(10000)
    result = price * 3
    assert result == Money(30000)

def test_multiply_by_zero():
    price = Money(10000)
    result = price * 0
    assert result == Money(0)

def test_multiply_by_negative_int_raises():
    price = Money(10000)
    with pytest.raises(ValueError, match="Quantity cannot be negative"):
        price * -2

def test_multiply_by_non_int_raises():
    price = Money(10000)
    with pytest.raises(TypeError):
        price * 3.5
    with pytest.raises(TypeError):
        price * "2"


# 7. Строковое представление (опционально, но полезно)
def test_repr():
    money = Money(10000, 'RUB')
    assert repr(money) == "Money(amount=10000, currency='RUB')"