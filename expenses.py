#expeses = [10.50, 8, 5, 15, 20, 5, 3]
#sum = 0

#for x in expeses:
    #sum = sum + x

#print("You spent $", sum," on lunch this week.", sep='')


total = 0
expenses = []

for i in range(7):
    expenses.append(float(input("Enter an expense:")))

    total = sum(expenses)

    print("Ypu spent $", total, sep='')