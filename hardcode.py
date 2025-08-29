# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,   # Apple
    "TSLA": 250,   # Tesla
    "GOOG": 140,   # Google
    "MSFT": 300    # Microsoft
}

portfolio = {}  
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker 📈")
print("Available Stocks:", list(stock_prices.keys()))

while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    elif stock in stock_prices:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    else:
        print("❌ Invalid stock symbol. Try again!")

# Calculate total investment
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = qty * price
    total_investment += investment
    print(f"{stock}: {qty} shares × {price} = {investment}")

print("💰 Total Investment Value:", total_investment)

# Save result in text file
with open("portfolio.txt", "w") as f:
    f.write("Stock Portfolio Summary\n")
    for stock, qty in portfolio.items():
        f.write(f"{stock}: {qty} shares × {stock_prices[stock]} = {qty * stock_prices[stock]}\n")
    f.write(f"\nTotal Investment Value: {total_investment}")

print("📂 Portfolio saved in portfolio.txt file.")