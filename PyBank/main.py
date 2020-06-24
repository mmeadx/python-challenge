#PyBank - Analyzing financial records

#Import add ons
import os 
import csv

#Define path to collect data from budget_data.csv
budget_data = os.path.join("Resources", "budget_data.csv")

#read budget_data.csv
with open(budget_data, 'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(f'CSV Header: {header}')  -- check to see if it can read
