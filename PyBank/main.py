import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

# Need to ask for help on how to put these into functions and still have them loop correctly

    month_count = 0
    profit = 0
    next_profit_value = 867884
    difference_sum = 0
    change = []
    previous_value = 867884
    
    for row in csv_reader:
        
        #Increases month count by one per row looped through
        month_count += 1

        #Adds profit or loss to profit variable for each loop
        profit += int(row[1])

        #Finds the difference between two consecutive months, then sums these differences.
        #Resets the next_profit_value variable so in the NEXT loop it is equal to THIS loops profit
        #(Apparently you can just take the first and last values but I wasn't sure)
        difference = int(row[1]) - next_profit_value
        next_profit_value = int(row[1])
        difference_sum += difference

        #Subtracts the previous profit/loss value from current and appends it to our list
        change_value = int(row[1]) - previous_value
        previous_value = int(row[1])
        change.append(change_value)

    total_months = ("Total Months: " + str(month_count))
    total_profit = ("Total Profit: $" + str(profit))
    average_change = ("Average Change: $" + str(round(difference_sum / (month_count-1),2)))
    greatest_increase = ("Greatest Increase in Profits: $" + str(max(change)))
    greatest_decrease = ("Greatest Decrease in Profits: $" + str(min(change)))

    print(total_months)
    print(total_profit)
    print(average_change)
    print(greatest_increase)
    print(greatest_decrease)

output_path = os.path.join("output", "PyBankReport.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis------------'])
    csvwriter.writerow([total_months])
    csvwriter.writerow([total_profit])
    csvwriter.writerow([average_change])
    csvwriter.writerow([greatest_increase])
    csvwriter.writerow([greatest_decrease])
