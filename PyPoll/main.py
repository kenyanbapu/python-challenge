# import libraries
import os
import csv

# set file path
csvpath = os.path.join('raw_data', 'election_data_2.csv')

# declaring variables
vote_count = 0
candidates = {}
candidates_percent = {}
winner = ""
winner_count = 0

# reading file
with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None)

    # finding total vote count; finding individual vote counts
    for row in csvreader:
        vote_count += 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

# percentages for each candidate
for key, value in candidates.items():
    candidates_percent[key] = round((value/vote_count) * 100, 2)

# finding the winner
for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

# tests
# print(total_vote_count)
# print(candidates)
# print(candidates_percent)
# print(winner)

# printing to the terminal
print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(vote_count))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")

# creating new text file
new_file = open("Election Results_1.csv", "w")

# writing the new file
new_file.write("Election Results \n")
new_file.write("------------------------------------- \n")
new_file.write("Total Votes: " + str(vote_count) + "\n")
new_file.write("------------------------------------- \n")
for key, value in candidates.items():
    new_file.write(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ") \n")
new_file.write("------------------------------------- \n")
new_file.write("Winner: " + winner + "\n")
new_file.write("------------------------------------- \n")
