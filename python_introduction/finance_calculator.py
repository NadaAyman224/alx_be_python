income = int( input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

savings = income - expenses
str_savings = str(savings)
print("Your monthly savings are", "$" + str_savings + ".")

Projected_Savings =  int(savings * 12 + ( savings * 12 * 0.05))
str_pro_savings = str(Projected_Savings)
print("Projected savings after one year, with interest, is:", "$" + str_pro_savings + ".")

