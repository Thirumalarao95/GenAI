def apply_discount(price,percent):
    result = price * (price / 100)
    return result

def flat_discount(price):
    result = price - 50
    return result