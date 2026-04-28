stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 200,
    "AMZN": 150
}

total = 0

print(" Stock Portfolio Tracker")

while True:
    stock = input("Enter stock name (or exit): ").upper()

    if stock == "EXIT":
        break

    if stock in stocks:
        qty = int(input("Enter quantity: "))
        price = stocks[stock]
        value = price * qty
        total += value

        print("Added:", stock)
        print("Price:", price)
        print("Value:", value)

    else:
        print(" Stock not found")

print("\n Total Investment =", total)