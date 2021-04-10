#import bank data

import os
import csv

#path to bank data

csvpath=os.path.join('..','Resources','election_data.csv')

#csvreader

with open(csvpath,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)

#set empty list 

    votes=[]
    county=[]
    candidates=[]
    Khan=[]
    Correy=[]
    Li=[]
    Tooley=[]

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])  

#vote total 

    total_votes=(len(votes))
    print(f"The total votes are: {total_votes}")

#votes per candidate
    for candidate in candidates:
        if candidate == "Khan":
            Khan.append(candidates)
            Khan_votes = len(Khan)
        elif candidate == "Correy":
            Correy.append(candidates)
            Correy_votes = len(Correy)
        elif candidate == "Li":
            Li.append(candidates)
            Li_votes = len(Li)
        else:
            Tooley.append(candidates)
            Tooley_votes = len(Tooley)
 
#percentages of the total votes per candidate

    Khan_percent = round(((Khan_votes / total_votes) * 100), 2)
    Correy_percent = round(((Correy_votes / total_votes) * 100), 2)
    Li_percent = round(((Li_votes / total_votes) * 100), 2)
    Tooley_percent = round(((Tooley_votes / total_votes) * 100), 2)

#print winner 

    if Khan_percent> max(Correy_percent,Li_percent,Tooley_percent):
        Winner = "Khan"
    elif Correy_percent>max(Khan_percent,Li_percent,Tooley_percent):
        Winner= "Correy"
    elif Li_percent>max(Khan_percent,Correy_percent,Tooley_percent):
        Winner="Li"
    else:
        Winner="O'Tooley"

#print results

print("Election Results")
print("------------------")
print(f"Khan: {Khan_percent}% ({Khan_votes})")
print(f"Correy: {Correy_percent}% ({Correy_votes})")
print(f"Li: {Li_percent}% ({Li_votes})")
print(f"O'Tooley: {Tooley_percent}% ({Tooley_votes})")
print("------------------")
print(f"The winner is : {Winner}!")
