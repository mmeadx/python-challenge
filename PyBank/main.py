#PyBank - Analyzing financial records

#Import add ons
import os 
import csv

#Define path to collect data from budget_data.csv
budget_data = os.path.join("Resources", "budget_data.csv")

#Define path to write data
budget_analysis = os.path.join("analysis","analysis.csv")

#Define Variables for Total and Total Months
TotalMonths = 0
Total = 0
old = 0

#Create List for Increase/Decrease
IncrDecr = []
                 
#read budget_data.csv
with open(budget_data, 'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(f'CSV Header: {header}')  -- check to see if it can read

    for line in csvreader:

        change = int(line[1]) - old #find increases and deacreases - put them in a list
        IncrDecr.append(change) # Adding to Increases/Decreases list
        TotalMonths = TotalMonths + 1 #Finding total number of months
        Total = Total + int(line[1]) #Finding Net Profit/Loss
        old = int(line[1]) #setting current to old
    
    del IncrDecr[0]

    #----Find the Average Change----
    total = sum(IncrDecr) #Add up all change values
    #print(total) - checking change total

    average_change = total / (TotalMonths - 1) #change total divided by Total Months minus one 
    #print(average_change) - checking average 
    
    #----Find Max and Min Increase in profits----
    prof_incr = max(IncrDecr)
    prof_decr = min(IncrDecr)
            

print('') #Spacing
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {TotalMonths}')
print(f'Total: ${Total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: $({prof_incr})')
print(f'Greatest Decrease in Profits: $({prof_decr})')
print('') #Spacing

with open(budget_analysis, 'w') as csvfile:

    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow([f'Total Months: {TotalMonths}'])
    csvwriter.writerow([f'Total: ${Total}'])
