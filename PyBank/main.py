import os
import csv



budgetpath = os.path.join("..","..","Downloads","budget_data.csv")
TM = 0
Total = 0
Aveg = 0.0
MaxProfit = 0
MaxProfitDate = ""
MinProfit = 0
MinProfitDate = ""


with open(budgetpath, newline ='') as csvfile:
    budgetdata = csv.reader(csvfile, delimiter =',')
    csv_header = next(budgetdata)
    print(csv_header)    
    for row in budgetdata:
        TM = 1 + TM
        Total = Total + int(row[1])
        Aveg = Total/TM

        if (int(row[1]) > MaxProfit):
            MaxProfit = int(row[1])
            MaxProfitDate = row[0]

        if (int(row[1]) < MinProfit):
            MinProfit = int(row[1])
            MinProfitDate = row[0]




print("Total Months: " + str(TM))
print("Total: " + str(Total))
print("Average Change: " + str(Aveg))
print("Greatest Increase in Profits occured on Date: " + MaxProfitDate + " with an amount of " + str(MaxProfit))
print("Greatest Decrease in Profits occured on Date: " + MinProfitDate + " with an amount of " + str(MinProfit))