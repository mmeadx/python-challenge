#PyPoll - Vote Counting
#Thanks to Allan Hunt for the help!

#Import add ons
import os 
import csv

#Define path to collect data from election_data.csv
election_data = os.path.join("Resources", "election_data.csv")

#Define Values
TotalVotes = 0

#Create Lists & Dictionaries
candidate_votes = {} #This will hold unique candidates and their vote count
percentages = {} #This will hold unique candidates and the percentages
percentages_compare = [] #This is a list of the percentages to compare for winner
compare_lib = {} #Created dictionary to get candidate as output value
winning_candidate = "This will be replaced by the winning candidate" #placeholder value


#read budget_data.csv
with open(election_data, 'r') as csvfile:

    #split data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    #print(f'CSV Header: {header}')  # check to see if it can read

    #read through csv file
    for line in csvreader:

        # Count the number of votes
        TotalVotes = TotalVotes + 1 #Finding total number of votes

        #Find unique candidates and put them into a dictionary while adding number of votes
        if line[2] not in candidate_votes:
            #If unique, add them to list with a starting vote value of 1
            candidate_votes[line[2]] = 1
        else:
            #If already in list, add a vote to their count
            candidate_votes[line[2]] += 1

#print(candidate_votes) #test to see if counter worked

#-----Find percentages for each candidate-----
for candidate in candidate_votes:
    percent_vote = candidate_votes[candidate] / TotalVotes #divide candidate vote count by total votes
    percent_vote_changed = "{:.3%}".format(percent_vote) #changing format of percentage

    #Add candidate percentage to library to be referenced 
    percentages[candidate] = percent_vote_changed

    #Make a list and library to compare percentages to find winner
    percentages_compare.append(percent_vote_changed) #adding percentages to list
    compare_lib[percent_vote_changed] = candidate #reversing order of candidate for output

#-----Find winner-----
winning_candidate = compare_lib[max(percentages_compare)]
#print(winning_candidate) # Test print winning candidate

#test print all lists & dictionaries
# print(candidate_votes)
# print(percentages)
# print(percentages_compare)  
# print(compare_lib)

#-----Print results to terminal-----

print('') #spacing away from command line
print('Election Results')
print('-------------------------')
print(f'Total Votes: {TotalVotes}')
print('-------------------------')
for candidate in candidate_votes: #Loop through candidate_votes to get individual results
    print(f'{candidate}: {percentages[candidate]} ({candidate_votes[candidate]})')
print('-------------------------')
print(f'Winner: {winning_candidate}')
print('-------------------------')

#-----Print results to txt file-----

f = open("analysis/poll_analysis.txt", 'w')

f.write('Election Results\n')
f.write('-------------------------\n')
f.write(f'Total Votes: {TotalVotes}\n')
f.write('-------------------------\n')
for candidate in candidate_votes:
    f.write(f'{candidate}: {percentages[candidate]} ({candidate_votes[candidate]})\n')
f.write('-------------------------\n')
f.write(f'Winner: {winning_candidate}\n')
f.write('-------------------------\n')
f.close()
