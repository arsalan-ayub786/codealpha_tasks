# Stock Portfolio Tracker - CodeAlpha Python Internship (Task 2)

# Hardcoded stock prices (price per share in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = {}  # stores stock name -> quantity


def show_available_stocks():
    print("\nAvailable stocks and prices:")
    for stock, price in stock_prices.items():
        print(f"  {stock}: ${price}")


def get_portfolio_from_user():
    print("\nEnter your stocks one by one. Type 'done' when finished.")
    while True:
        name = input("\nStock name (or 'done'): ").strip().upper()

        if name == "DONE":
            break

        if name not in stock_prices:
            print("Stock not found. Please choose from the available stocks.")
            continue

        qty_text = input("Quantity: ").strip()

        if not qty_text.isdigit() or int(qty_text) <= 0:
            print("Please enter a valid whole number greater than 0.")
            continue

        quantity = int(qty_text)

        # If the stock was already added, increase its quantity
        if name in portfolio:
            portfolio[name] += quantity
        else:
            portfolio[name] = quantity

        print(f"Added {quantity} share(s) of {name}.")


def calculate_and_display():
    total = 0
    lines = []

    lines.append("----- Portfolio Summary -----")
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total += value
        lines.append(f"{stock}: {quantity} x ${stock_prices[stock]} = ${value}")
    lines.append("-----------------------------")
    lines.append(f"Total Investment Value: ${total}")

    print()
    for line in lines:
        print(line)

    return lines


def save_to_file(lines):
    choice = input("\nDo you want to save the result to a file? (yes/no): ").strip().lower()
    if choice == "yes":
        with open("portfolio_result.txt", "w") as file:
            for line in lines:
                file.write(line + "\n")
        print("Result saved to portfolio_result.txt")


def main():
    print("Welcome to the Stock Portfolio Tracker!")
    show_available_stocks()
    get_portfolio_from_user()

    if not portfolio:
        print("\nNo stocks were added. Exiting.")
        return

    lines = calculate_and_display()
    save_to_file(lines)


main()