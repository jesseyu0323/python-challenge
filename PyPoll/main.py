import os
import csv


with open("election_data.csv", 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    total_votes = 0
    list_of_candidates = []
    percent_won = {}
    winner = ''
    most_voted = 0

    for row in csvreader:
   
    	total_votes = total_votes + 1
    	candidate_name = row[2]

    	if candidate_name not in list_of_candidates:
    		list_of_candidates.append(candidate_name)
    		percent_won[candidate_name] = 1
    	else:
    		percent_won[candidate_name] = percent_won[candidate_name] + 1
	
    print("Election Results")
    print("---------------------------")
    print("Total Votes " + str(total_votes))
    print("---------------------------")
    
    for candidate in percent_won:
    	number_of_votes = percent_won.get(candidate)
    	vote_percentage = number_of_votes / total_votes * 100

    	if (number_of_votes > most_voted):
    		most_voted = number_of_votes
    		winner = candidate
    	
    	print(candidate + ": " + "{0:.3f}".format(vote_percentage) + "%" + " " "(" + str(number_of_votes) + ")")
   
    print("---------------------------")
    print("Winner: " + winner)
    print("---------------------------")

    with open("output_file.txt" , "w") as text_file:
    	text_file.write("Election Results")
    	text_file.write("\n")
    	text_file.write("---------------------------")
    	text_file.write("\n")
    	text_file.write("Total Votes " + str(total_votes))
    	text_file.write("\n")
    	text_file.write("---------------------------")
    	text_file.write("\n")
    	text_file.write(candidate + ": " + "{0:.3f}".format(vote_percentage) + "%" + " " "(" + str(number_of_votes) + ")")
    	text_file.write("\n")
    	text_file.write("---------------------------")
    	text_file.write("\n")
    	text_file.write("Winner: " + winner)
    	text_file.write("\n")
    	text_file.write("---------------------------")
    

