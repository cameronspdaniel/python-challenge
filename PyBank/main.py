import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    month_count = 0
    profit = 0
    next_profit_value = 867884
    difference_sum = 0
    for row in csv_reader:
        
        month_count += 1

        profit += int(row[1])

        
        difference = int(row[1]) - next_profit_value
        next_profit_value = int(row[1])
        difference_sum += difference

    print("Total Months: " + str(month_count))
    print("Total Profit: $" + str(profit))
    print("Average Change: $" + str(difference_sum / 85)) 