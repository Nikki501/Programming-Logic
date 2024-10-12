salary = 0
numDependents = 0
federalTax = 0
dependentDeduction = 0
totalWithholding = 0
takeHomePay = 0     


# input statements
salary = float(input("Please Enter Your Salary Amount: "))
numDependents = float(input("Please Enter Your Number of Dependents: "))

# calculate taxes here
stateTax = salary * .065
print("State Tax: $" + str(stateTax))

federalTax = salary * .28
print("Federal Tax: $" + str(federalTax))

dependentDeduction = (salary * .025) * numDependents
print("Dependents: $" + str(dependentDeduction))

totalWithholding = stateTax + federalTax + dependentDeduction

takeHomePay = salary - totalWithholding


# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
