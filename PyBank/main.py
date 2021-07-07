import os

import csv


#variables

months = 0
net_total = 0
PL_change = []
average_change = []
min_date = []
max_date = []
previousmonth = 0



filepath = "/Users/williamplymouth/Desktop/Python_HW/PyBank/Resources/budget_data.csv"

with open (filepath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    
    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")

    for i in csvreader:
        months += 1
        net_total += int (i[1])
        PL_change.append(int(i[1]) - previousmonth)
        previousmonth = int(i[1])

print(f"CSV Header: {csv_header}")       
print(f"Months: {months}")
print(f"Net total is {net_total}")
print(f"Profit/Loss change: {PL_change}")


# sum
sum_PL_change = sum(PL_change)

# average change
average_change = sum(PL_change)/len(PL_change)
print(f"The average change is {average_change}")

# Greatest increase in profits

most_profit = max(PL_change)

print(f"the gratest increase in profits {most_profit}")





# Greatest decrease in profits

least_profit = min(PL_change)

print(f"The greatest decrease in profits is {least_profit}")







  



