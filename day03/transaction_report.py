totals = {}

try:
    with open("transactions.txt", "r") as file:
        for line in file:
            name, amount = line.strip().split(",")
            amount = float(amount)

            if name in totals:
                totals[name] += amount
            else:
                totals[name] = amount

    sorted_totals = sorted(
        totals.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for name, total in sorted_totals:
        print(f"{name}: {total}")

    with open("report.txt", "w") as report:
        for name, total in sorted_totals:
            report.write(f"{name}: {total}\n")

except FileNotFoundError:
    print("transactions.txt not found.")