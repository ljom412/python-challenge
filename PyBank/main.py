import os
import csv

budget_data = os.path.join("PyBank/Resources/budget_data.csv")

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    profit = []
    months = []

    for rows in csv_reader:
        profit.append(int(rows[1]))
        months.append(rows[0])
    
    revenue_change = []

    for x in range(1, len(profit)):
        revenue_change.append((int(profit[x]) - int(profit[x-1])))

    revenue_average = sum(revenue_change) / len(revenue_change)

    total_months = len(months)
   
    total_profit = sum(profit)

    greatest_increase = max(revenue_change)

    greatest_decrease = min(revenue_change)

    print("Financial Analysis")

    print(".................................................................")

    print("Total Months: " + str(total_months))

    print("Total Amount of Profit/Losses: " + "$" + str(sum(profit)))

    revenue_average = f'{revenue_average:.2f}'
    print("Average Change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))