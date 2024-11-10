BONUS_1 = 50.00
BONUS_2 = 75.00
BONUS_3 = 100.00
BONUS_4 = 200.00

employeeName =  input("Please Enter Employee's Name: ")
numShifts = input("Please Enter Number of Shifts: ")
inputnumTransactions = input("Please Enter Number of Transactions: ")
inputdollarValue = input("Please Enter Transctions Dollar Value: ")

numShiftsworked = float(numShifts)
numTransactions = float(inputnumTransactions)
dollarValue = float(inputdollarValue)

productivityScore = (dollarValue/numTransactions)/numShiftsworked

if productivityScore <=30:
    bonus = BONUS_1
elif productivityScore >= 31 and productivityScore <= 69:
    bonus = BONUS_2
elif productivityScore >= 70 and productivityScore <=199:
    bonus =  BONUS_3
elif productivityScore >= 200:
    bonus = BONUS_4


#Output
print("Employee Name: " + employeeName) 
print("Employee Bonus:$" + str(bonus))
