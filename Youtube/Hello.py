from datetime import datetime
expenses = []
budget = float(input("Enter your monthly budget: $"))
while True:
    print("\n" + "=" * 50)
    print("         EXPENSE TRACKER")
    print("=" * 50)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Summary")
    print("4. Exit")
    choice = input("\nChoose an option: ")
    if choice == "1":
        name = input("Expense Name: ")
        category = input("Category (Food, Transport, Shopping, etc): ")
        amount = float(input("Amount: $"))
        expense = {
            "name": name,
            "category": category,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        expenses.append(expense)
        print("\n✓ Expense added successfully!")
    elif choice == "2":
        if not expenses:
            print("\nNo expenses recorded.")
            continue
        print("\n{:<15} {:<15} {:<10} {:<15}".format(
            "NAME", "CATEGORY", "AMOUNT", "DATE"))
        print("-" * 60)
        for expense in expenses:
            print("{:<15} {:<15} ${:<9.2f} {:<15}".format(
                expense["name"],
                expense["category"],
                expense["amount"],
                expense["date"]
            ))
    elif choice == "3":
        if not expenses:
            print("\nNo expenses to summarize.")
            continue
        total = sum(expense["amount"] for expense in expenses)
        remaining = budget - total
        print("\n" + "=" * 30)
        print("SUMMARY")
        print("=" * 30)
        print(f"Total Expenses: ${total:.2f}")
        print(f"Budget:         ${budget:.2f}")
        print(f"Remaining:      ${remaining:.2f}")
        print("\nExpenses by Category:")
        categories = {}
        for expense in expenses:
            cat = expense["category"]
            categories[cat] = categories.get(cat, 0) + expense["amount"]
        for category, amount in categories.items():
            print(f"{category:<15} ${amount:.2f}")
        if remaining < 0:
            print("\n⚠ WARNING: Budget exceeded!")
        else:
            print("\n✓ Budget is under control.")
    elif choice == "4":
        print("\nThank you for using Expense Tracker!")
        break
    else:
        print("\nInvalid option.")
