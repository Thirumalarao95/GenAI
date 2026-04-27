def calculate_total(prices):
    total = 0
    for i in prices:
        total = total + i
    return total

def apply_tax(amount):
    result = amount * 0.05
    return result