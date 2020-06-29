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
    #print(IncrDecr) #test the list

    #----Find the Average Change----
    total = sum(IncrDecr) #Add up all change values
    #print(total) - checking change total

    average_change = total / (TotalMonths - 1) #change total divided by Total Months minus one 
    #print(average_change) - checking average 
    
    #----Find Max and Min Increase in profits----
    prof_incr = max(IncrDecr)
    prof_decr = min(IncrDecr)

    #----Find where the Max and Min Increase are on the list to compare to dates
    index_incr = IncrDecr.index(prof_incr)
    #print('index increase is', index_incr) - checking increase index value
    index_decr = IncrDecr.index(prof_decr)
    #print('index decrease is', index_decr) - checking decrease index value

print('') #Spacing
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {TotalMonths}')
print(f'Total: ${Total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: (${prof_incr})')
print(f'Greatest Decrease in Profits: (${prof_decr})')
print('') #Spacing

#-----Write to analysis file-----

f = open("budget_analysis.txt", 'w')

f.write('Financial Analysis\n')
f.write('----------------------------\n')
f.write(f'Total Months: {TotalMonths}\n')
f.write(f'Total: ${Total}\n')
f.write(f'Average Change: ${average_change}\n')
f.write(f'Greatest Increase in Profits: (${prof_incr})\n')
f.write(f'Greatest Decrease in Profits: (${prof_decr})\n')
f.close()

