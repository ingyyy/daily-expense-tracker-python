expenses = []

print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

while True:
    choice = input("Enter your choice (1-5): ")

    if choice == "5":  # حطينا علامات تنصيص هنا
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

    elif choice == "1": # وهنا كمان
        try:
            expense = float(input("Enter the expense amount: "))
            expenses.append(expense)
            print("Expense added successfully!")
        except ValueError:
            print("Invalid input! Please enter a number for the expense.")

    elif choice == "2": # وكل الباقي بنفس الطريقة
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for index, expense in enumerate(expenses, 1):
                print(f"{index}. {expense}")

    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses recorded yet.")
        else:
            total = sum(expenses)
            average = total / len(expenses)
            print("Total expense:", total)
            print("Average expense:", average)

    elif choice == "4":
        expenses.clear()
        print("All expenses cleared.")

    else:
        print("Invalid choice. Please try again.")
