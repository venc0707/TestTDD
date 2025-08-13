

def calculate_tax(price, tax_rate):
    if price <= 0:
        raise ValueError('Неверная цена')
    elif 0 < tax_rate <= 100:
        result = (price * tax_rate / 100) + price
        return result
    else:
        raise ValueError('Неверный налоговый процент')


if __name__ == "__main__":
    print(calculate_tax(100, 20))