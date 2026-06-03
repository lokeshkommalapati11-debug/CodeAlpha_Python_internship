# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

print("Welcome to Stock Portfolio Tracker")

stock_name = input("Enter stock name (AAPL/TSLA/GOOGL/MSFT): ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    total_value = stocks[stock_name] * quantity
    print("\nStock:", stock_name)
    print("Price per share:", stocks[stock_name])
    print("Quantity:", quantity)
    print("Total Investment Value:", total_value)
else:
    print("Stock not found!")