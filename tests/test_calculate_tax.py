from src.calculate_tax import calculate_tax
import pytest


def test_calculate_tax():
    assert calculate_tax(100.0, 20.0) == 120.0

def test_calcelate_tax_discount():
    assert  calculate_tax(100.0, 20.0, discount=10) == 110
    
def test_calcelate_tax_discount_round():
    assert calculate_tax(100.0, 11.1111) == 111.11

@pytest.mark.parametrize('price, tax_rate, expection, message', [
    (-100, 10, ValueError, "Неверная цена"),
    (100, -1, ValueError, "Неверный налоговый процент"),
    (100, 110, ValueError, "Неверный налоговый процент")
])
def test_calculate_tax_expection(price, tax_rate, expection, message):
    with pytest.raises(expection) as exc_info:
        calculate_tax(price, tax_rate)
    assert message in str(exc_info.value)
