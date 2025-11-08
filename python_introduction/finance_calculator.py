monthly_income = int( input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
str_savings = str(monthly_savings)
print("Your monthly savings are", "$" + str_savings + ".")

Projected_Savings =  int(monthly_savings * 12 + ( monthly_savings * 12 * 0.05))
str_pro_savings = str(Projected_Savings)
print("Projected savings after one year, with interest, is:", "$" + str_pro_savings + ".")

