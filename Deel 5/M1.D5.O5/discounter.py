month_discount_brands = 'vespa,kymco,yamaha'
MONTH_DISCOUNT_PERC = 10

merk = input("Welk merk? ").lower()
price = 2500


def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    if merk in month_discount_brands:
        korting = price * MONTH_DISCOUNT_PERC / 100
    else:
        korting = 0

    korting = "{:.2f}".format(korting)
    return korting
    
print(f"Uw korting is: {calc_discount(price, merk, month_discount_brands)}")
    

