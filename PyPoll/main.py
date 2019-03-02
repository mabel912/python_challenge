import os
import csv

electionpath = os.path.join("..","..","Downloads","election_data.csv")

totalVotesCast = 0


with open(electionpath, newline ='') as csvfile:
    electioncsv = csv.reader(csvfile, delimiter =',')
    csv_header = next(electioncsv)

    electiondic = {}

    for row in electioncsv:
        totalVotesCast = 1 + totalVotesCast
        electiondic[row[0]] = {'County':row[1],'Candidate':row[2]}

   



print("Election Results")
print("-----------------------------------------------------------------------")
print("Total Votes: " + str(totalVotesCast))
print("-----------------------------------------------------------------------")


