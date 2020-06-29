#PyBank - Analyzing financial records

#Import add ons
import os 
import csv

#Define path to collect data from budget_data.csv
budget_data = os.path.join("Resources", "budget_data.csv")

#Define Variables for Total and Total Months
TotalMonths = 0
Total = 0
old = 0

#Create List for Increase/Decrease and dates
IncrDecr = []
date_list = []
                 
#read budget_data.csv
with open(budget_data, 'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(f'CSV Header: {header}')  -- check to see if it can read

    for line in csvreader:

        date = line[0] # Set date 
        date_list.append(date) # Add date to list to check later
        change = int(line[1]) - old #find increases and deacreases - put them in a list
        IncrDecr.append(change) # Adding to Increases/Decreases list
        TotalMonths = TotalMonths + 1 #Finding total number of months
        Total = Total + int(line[1]) #Finding Net Profit/Loss
        old = int(line[1]) #setting current to old
    
    del IncrDecr[0] #removing first index 
    #print(IncrDecr) #test the list

    #----Find the Average Change----
    total = sum(IncrDecr) #Add up all change values
    #print(total) - checking change total

    average_change = total / (TotalMonths - 1) #change total divided by Total Months minus one 
    avg_change = round(average_change, 2) #Round to 2 decimal spots
    #print(average_change) - checking average 
    
    #----Find Max and Min Increase in profits----
    prof_incr = max(IncrDecr)
    prof_decr = min(IncrDecr)

    #----Find where the Max and Min Increase are on the list to compare to dates and add one to get date
    index_incr = IncrDecr.index(prof_incr) + 1
    #print('index increase is', index_incr) #- checking increase index value
    index_decr = IncrDecr.index(prof_decr) + 1
    #print('index decrease is', index_decr) #- checking decrease index value

    #-----Find dates on date_list by index number-----
    date_max_incr = date_list[index_incr]
    #print(date_max_incr) #Check date
    date_max_decr = date_list[index_decr]
    #print(date_max_decr) #Check date


print('') #Spacing
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {TotalMonths}')
print(f'Total: ${Total}')
print(f'Average Change: ${avg_change}')
print(f'Greatest Increase in Profits: {date_max_incr} (${prof_incr})')
print(f'Greatest Decrease in Profits: {date_max_decr} (${prof_decr})')
print('') #Spacing

#-----Write to analysis file-----

f = open("analysis/budget_analysis.txt", 'w')

f.write('Financial Analysis\n')
f.write('----------------------------\n')
f.write(f'Total Months: {TotalMonths}\n')
f.write(f'Total: ${Total}\n')
f.write(f'Average Change: ${avg_change}\n')
f.write(f'Greatest Increase in Profits: {date_max_incr} (${prof_incr})\n')
f.write(f'Greatest Decrease in Profits: {date_max_decr} (${prof_decr})\n')
f.close()

