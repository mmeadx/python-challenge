#PyBank - Analyzing financial records

#Import add ons
import os 
import csv

#Define path to collect data from budget_data.csv
budget_data = os.path.join("Resources", "budget_data.csv")

TotalMonths = 0
Total = 0

#read budget_data.csv
with open(budget_data, 'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(f'CSV Header: {header}')  -- check to see if it can read

    for line in csvreader:

        TotalMonths = TotalMonths + 1 #Finding total number of months
        Total = Total + int(line[1]) #Finding Net Profit/Loss

print('') #Spacing
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {TotalMonths}')
print(f'Total: ${Total}')
print('') #Spacing
