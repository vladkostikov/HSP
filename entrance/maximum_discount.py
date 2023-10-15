def MaximumDiscount(_n: int, price: list) -> int:
    sorted_price = sorted(price, reverse=True)
    discounts = sorted_price[2::3]
    total_discount = sum(discounts)
    return total_discount
