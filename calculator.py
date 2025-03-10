def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        discounted_price = price - discount_amount
        return discounted_price
    else:
        return price

# Example usage
original_price = 100
discount_percentage = 25

final_price = calculate_discount(original_price, discount_percentage)
print(f"The final price after applying a {discount_percentage}% discount is: ${final_price:.2f}")