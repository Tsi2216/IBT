# Transaction Log Reader

customer_totals = {}

try:
    # Open the transaction file
    with open("transactions.txt", "r") as file:

        # Read each line
        for line in file:

            # Remove spaces/new line and split by comma
            name, amount = line.strip().split(",")

            # Convert amount to number
            amount = float(amount)

            # Add amount to existing customer
            if name in customer_totals:
                customer_totals[name] += amount

            # Add new customer
            else:
                customer_totals[name] = amount

    # Sort from highest total to lowest
    sorted_customers = sorted(
        customer_totals.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("Transaction Report")
    print("-" * 25)

    # Create report.txt
    with open("report.txt", "w") as report:

        report.write("Transaction Report\n")
        report.write("-" * 25 + "\n")

        # Print and write each customer
        for name, total in sorted_customers:
            print(f"{name}: {total:.2f}")
            report.write(f"{name}: {total:.2f}\n")

    print("\nReport saved to report.txt")

except FileNotFoundError:
    print("Error: transactions.txt was not found.")