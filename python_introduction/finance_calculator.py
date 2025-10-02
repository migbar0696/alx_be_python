monthly_income = float(input("Enter your monthly income: "))
monthly_expense = float(input("Enter your total monthly expense: "))
monthly_saving = monthly_income - monthly_expense
print(f"Your monthly savings are ${monthly_saving}.")
print(f"Projected saving after one year , with interest, is: {monthly_saving * 12 + (monthly_saving * 12 * 0.05)}.")