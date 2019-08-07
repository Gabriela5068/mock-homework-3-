import os
import csv

csvpath = 'election_data.csv'
votes =[]
candidates =[]
candidatevotes = {} #dictionary
winner = 0

with open (csvpath,newline='') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
#total votes
    for row in csvreader:
        votes.append(float(row[0]))
        candidatename = row[2]
        if candidatename not in candidates:
            candidates.append(candidatename)
            candidatevotes[candidatename] = 0 
            #syntax to remember to add a new key into dictionary
            #d['newkey'] = newvalue. This will print multiple as inside the for loop 
        candidatevotes[candidatename] = candidatevotes[candidatename] + 1
    
    totalvotes = len(votes)
    print("Total Votes:", totalvotes)
    print("List of Candidates", candidates)
    

#get value from dictionary
    for candidate in candidatevotes:
        votes = candidatevotes.get(candidate)
        votepercentage = (votes/totalvotes)*100 
        if (votes > winner):
            winner = votes 
            win = candidate
        print("Vote Stats:", candidate, votes, votepercentage)    
    print("Winner:", win)

#create a text file
f = open("output.txt","w+")
f.write(str(totalvotes))
f.write(str(candidates))
f.write(str(candidate))
f.write(str(votes))
f.write(str(votepercentage))
f.write(str(win))
f.close()

