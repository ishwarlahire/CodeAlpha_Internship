# TASK 2: Stock Portfolio Tracker ● Goal: Build a simple stock tracker that calculates total investment based on manually defined stock prices. ● Simplified Scope: ○ User inputs stock names and quantity. ○ Use a hardcoded dictionary to define stock prices (e.g., {"AAPL": 180, "TSLA": 250}). ○ Display total investment value and optionally save the result in a .txt or .csv file. ● Key Concepts Used: dictionary, input/output, basic arithmetic, file handling (optional).
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