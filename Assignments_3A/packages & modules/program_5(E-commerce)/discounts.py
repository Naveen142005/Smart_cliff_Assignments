import math


def apply_discount(total_price, coupon_code):
    num = ""
    for code in coupon_code:
        if code.isdigit():
            num += code
    num = int(num)

    discount_price = math.floor(total_price * (num / 100))

    return discount_price
