

def calculate_tax(price: float, tax_rate: float, *, discount: float = 0, round_to: int = 2) -> float:
    if price <= 0:
        raise ValueError('Неверная цена')
    elif 0 < tax_rate <= 100:
        result = (price * tax_rate / 100) + price - (price * discount / 100)
        return round(result, round_to)
    else:
        raise ValueError('Неверный налоговый процент')


if __name__ == "__main__":
    print(calculate_tax(100, 31.4141, round_to=5))