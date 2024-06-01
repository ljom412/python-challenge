import os
import csv

budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

# open the csv file and read header
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    profit = []
    months = []

    # read through each row
    for rows in csv_reader:
        profit.append(int(rows[1]))
        months.append(rows[0])
    
    # find revenue change
    revenue_change = []

    for x in range(1, len(profit)):
        revenue_change.append((int(profit[x]) - int(profit[x-1])))

    # find average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)

    # find total length of months
    total_months = len(months)

    # find greatest increase in revenue
    greatest_increase = max(revenue_change)

    #find greatest decrease in revenue
    greatest_decrease = min(revenue_change)

    # print analysis to terminal
    print("Financial Analysis")

    print("............................................................")

    print("Total Months: " + str(total_months))

    print("Total Amount of Profit/Losses: " + "$" + str(sum(profit)))

    # round average revenue change to two decimal places
    revenue_average = f'{revenue_average:.2f}'
    print("Average Change: " + "$" + str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

# print analysis to text file
    print("Financial Analysis", file=open('PyBank/PyBank.txt', 'a'))

    print("............................................................", file=open('PyBank/PyBank.txt', 'a'))

    print("Total Months: " + str(total_months), file=open('PyBank/PyBank.txt', 'a'))

    print("Total Amount of Profit/Losses: " + "$" + str(sum(profit)), file=open('Pybank/PyBank.txt', 'a'))

    print("Average Change: " + "$" + str(revenue_average), file=open('PyBank/PyBank.txt', 'a'))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase), file=open('PyBank/PyBank.txt', 'a'))
    
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease), file=open('PyBank/PyBank.txt', 'a'))
