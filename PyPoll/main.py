import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

    #Pre-Loop variables
    vote_count = 0
    candidate = []
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0


    for row in csv_reader:
        
        #Adds one to vote count for each row looped
        vote_count += 1

        #Adds candidate to List called candidate if row[2] is not already in the list
        if row[2] not in candidate:
            candidate.append(row[2])
        
        #Increases vote count if row[2] matches respective candidate from list (probably should utilize 'candidate' list instead of hard coding names)
        if row[2] == "Khan":
            khan_count += 1
        
        if row[2] == "Correy":
            correy_count += 1

        if row[2] == "Li":
            li_count += 1
        
        if row[2] == "O'Tooley":
            otooley_count += 1
    
    #Finds percentages(candidates votes / total votes * 100), rounds to two decimals
    khan_percentage = round(khan_count / vote_count * 100,2)
    correy_percentage = round(correy_count / vote_count * 100,2)
    li_percentage = round(li_count / vote_count * 100,2)
    otooley_percentage = round(otooley_count / vote_count * 100,2)

    #Uses max function to find the key associated with the highest vote count in our dictionary
    respective_vote_count = {candidate[0]: khan_count, candidate[1]: correy_count,candidate[2]: li_count,candidate[3]: otooley_count,}
    vote_winner = max(respective_vote_count, key=respective_vote_count.get)

    #Print out our results
    print("Election Results")
    print("-----------------")
    print("Total Votes: " + str(vote_count))
    print("-----------------")
    print("Khan: " + "%" + str(khan_percentage) + " (" + str(khan_count) + ")")
    print("Correy: " + "%" + str(correy_percentage) + " (" + str(correy_count) + ")")
    print("Li: " + "%" + str(li_percentage) + " (" + str(li_count) + ")")
    print("O'Tooley: " + "%" + str(otooley_percentage) + " (" + str(otooley_count) + ")")
    print("-----------------")
    print("Winner: " + str(vote_winner))

    output_path = os.path.join("output", "PyBankReport.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')

    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(["----------------"])
    csvwriter.writerow(["Total Votes: " + str(vote_count)])
    csvwriter.writerow(["----------------"])
    csvwriter.writerow(["Khan: " + "%" + str(khan_percentage) + " (" + str(khan_count) + ")"])
    csvwriter.writerow(["Correy: " + "%" + str(correy_percentage) + " (" + str(correy_count) + ")"])
    csvwriter.writerow(["Li: " + "%" + str(li_percentage) + " (" + str(li_count) + ")"])
    csvwriter.writerow(["O'Tooley: " + "%" + str(otooley_percentage) + " (" + str(otooley_count) + ")"])
    csvwriter.writerow(["-----------------"])
    csvwriter.writerow(["Winner: " + str(vote_winner)])