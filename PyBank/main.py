import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    month_count = 0
    profit = 0
    total_change = int(row[1])
    for row in csv_reader:
        month_count += 1
        profit += int(row[1])
        if int(row[1]) >= 0 and int(row[1]) >= total_change then:
            total_change = total_change 
        total_change = total_change - int(row[1])
        avg_change = total_change / 86
    print("Total Months: " + str(month_count))
    print("Total Profit: $" + str(profit))
    print(avg_change)
        

            