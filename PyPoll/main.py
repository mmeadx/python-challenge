#PyPoll - Vote Counting

#Import add ons
import os 
import csv

#Define path to collect data from election_data.csv
election_data = os.path.join("Resources", "election_data.csv")

TotalVotes = 0

#read budget_data.csv
with open(election_data, 'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(f'CSV Header: {header}')  # check to see if it can read

    for line in csvreader:

        TotalVotes = TotalVotes + 1 #Finding total number of votes

print(f'Total Votes: {TotalVotes}')