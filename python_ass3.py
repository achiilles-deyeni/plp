
def calculate_discount(price, discount_percent):
    """Takes the price of an item and applies a discount if the discount percent is greater than 20"""
    if discount_percent > 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price


discount_percent = float(input("Enter discount percent: "))

print(f"Amount to pay: {calculate_discount(2000, discount_percent)}")