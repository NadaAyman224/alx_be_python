monthely_income = int( input("Enter your monthly income: "))
monthely_expenses = int(input("Enter your total monthly expenses: "))

monthely_savings = monthely_income - monthely_expenses
str_savings = str(monthely_savings)
print("Your monthly savings are", "$" + str_savings + ".")

Projected_Savings =  int(monthely_savings * 12 + ( monthely_savings * 12 * 0.05))
str_pro_savings = str(Projected_Savings)
print("Projected savings after one year, with interest, is:", "$" + str_pro_savings + ".")

