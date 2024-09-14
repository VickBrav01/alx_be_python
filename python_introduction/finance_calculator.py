monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

project_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(monthly_savings)
print(project_savings)

print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(project_savings)}.")




