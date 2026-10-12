def discount_price(original_price, dp):
    fp = float(original_price - ((dp / 100) * original_price))
    print(f"The final price is {fp}")


discount_price(100, 15)
