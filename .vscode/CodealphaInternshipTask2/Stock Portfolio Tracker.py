"""
Stock Portfolio Tracker
------------------------
Calculates total investment value based on manually defined stock prices.

Key Concepts Used: dictionary, input/output, basic arithmetic, file handling (optional)
"""
import csv
# Hardcoded dictionary of stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 410,
    "META": 480,
    "NFLX": 630
}

def get_portfolio_input():
    """Ask the user for stock names and quantities, return as a dictionary."""
    portfolio = {}
    print("Available stocks and prices:")
    for stock, price in STOCK_PRICES.items():
        print(f"  {stock}: ${price}")
    print("\nEnter stock name and quantity (type 'done' to finish)")

    while True:
        stock = input("\nStock symbol (e.g., AAPL): ").strip().upper()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print(f"⚠️  '{stock}' not found in price list. Please try again.")
            continue

        qty_input = input(f"Quantity of {stock}: ").strip()

        try:
            quantity = int(qty_input)
            if quantity <= 0:
                print("⚠️  Quantity must be a positive number.")
                continue
        except ValueError:
            print("⚠️  Please enter a valid whole number.")
            continue

        # Add to portfolio (accumulate if entered twice)
        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"✅ Added {quantity} share(s) of {stock}")

    return portfolio

def calculate_total_investment(portfolio):
    """Calculate total investment value and per-stock breakdown."""
    breakdown = {}
    total = 0

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * quantity
        breakdown[stock] = {
            "quantity": quantity,
            "price": price,
            "value": value
        }
        total += value

    return breakdown, total

def display_summary(breakdown, total):
    """Print a formatted summary of the portfolio."""
    print("\n" + "=" * 45)
    print("           PORTFOLIO SUMMARY")
    print("=" * 45)
    print(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 45)

    for stock, data in breakdown.items():
        print(f"{stock:<10}{data['quantity']:<8}${data['price']:<9}${data['value']:<9}")

    print("-" * 45)
    print(f"TOTAL INVESTMENT: ${total:,.2f}")
    print("=" * 45)

def save_to_file(breakdown, total):
    """Optionally save the results to a .txt or .csv file."""
    choice = input("\nSave results to a file? (y/n): ").strip().lower()

    if choice != "y":
        print("Skipping file save.")
        return

    file_format = input("Choose format - txt or csv: ").strip().lower()

    if file_format == "csv":
        filename = "portfolio_summary.csv"
        with open(filename, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, data in breakdown.items():
                writer.writerow([stock, data["quantity"], data["price"], data["value"]])
            writer.writerow([])
            writer.writerow(["Total Investment", "", "", total])
        print(f"✅ Saved to {filename}")

    elif file_format == "txt":
        filename = "portfolio_summary.txt"
        with open(filename, mode="w") as f:
            f.write("PORTFOLIO SUMMARY\n")
            f.write("=" * 30 + "\n")
            for stock, data in breakdown.items():
                f.write(f"{stock}: {data['quantity']} shares @ ${data['price']} = ${data['value']}\n")
            f.write("-" * 30 + "\n")
            f.write(f"TOTAL INVESTMENT: ${total:,.2f}\n")
        print(f"✅ Saved to {filename}")

    else:
        print("⚠️  Unknown format. File not saved.")


def main():
    print("📈 Welcome to the Stock Portfolio Tracker!\n")

    portfolio = get_portfolio_input()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    breakdown, total = calculate_total_investment(portfolio)
    display_summary(breakdown, total)
    save_to_file(breakdown, total)

    print("\n👋 Done. Thanks for using the Stock Portfolio Tracker!")
if __name__ == "__main__":
    main()