import csv
from datetime import datetime

def get_stock_data(symbol):
    prices = {
        "AAPL": 280.5,
        "MSFT": 425.0,
        "NVDA": 185.2,
    }
    return prices.get(symbol.upper(), 100.0)

def analyze_option(symbol, price, strike_price):
    if price > strike_price:
        status = "IN-THE-MONEY"
        profit = round(price - strike_price, 2)
    else:
        status = "OUT-OF-THE-MONEY"
        profit = round(price - strike_price, 2)
    return status, profit

def save_to_csv(symbol, price, strike, status, profit):
    with open("results.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d"), symbol, price, strike, status, profit])
    print(f"Saved: {symbol} - {status}")

def main():
    symbol = input("Enter stock symbol (e.g. AAPL): ")
    strike = float(input("Enter strike price: "))

    price = get_stock_data(symbol)
    status, profit = analyze_option(symbol, price, strike)

    print(f"\n{symbol} Current Price: ${price}")
    print(f"Strike: ${strike} -> {status} | Profit: ${profit}")

    save_to_csv(symbol, price, strike, status, profit)

if __name__ == "__main__":
    main()
