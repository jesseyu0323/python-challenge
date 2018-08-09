import os
import csv


with open("budget_data.csv", 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    total_months = 0 
    total_profits_losses = 0
    first_month = 0
    change_in_profitslosses = 0
    total_change = 0
    average_change = 0
    greatest_increase = 0
    greatest_increase_date = ''
    greatest_decrease = 0
    greatest_decrease_date = ''

    for row in csvreader:
    	total_months = total_months + 1
    	total_profits_losses = total_profits_losses + int(row[1])
    	change_in_profitslosses = (int(row[1]) - first_month) 
    	first_month = int(row[1])
    	total_change = change_in_profitslosses + total_change
    
    	if change_in_profitslosses > greatest_increase:
    		greatest_increase = change_in_profitslosses
    		greatest_increase_date = row[0]

    	if change_in_profitslosses < greatest_decrease:
    		greatest_decrease = change_in_profitslosses
    		greatest_decrease_date = row[0]

    average_change = total_change/total_months

    print()
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_profits_losses))
    print("Average Change: " + "$" + str(average_change))
    print("Greatest Increase in Profits:" + greatest_increase_date + " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits:" + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")

    with open("output_file.txt" , "w") as text_file:
    	text_file.write("Financial Analysis")
    	text_file.write("\n")
    	text_file.write("----------------------------")
    	text_file.write("\n")
    	text_file.write("Total Months: " + str(total_months))
    	text_file.write("\n")
    	text_file.write("Total Revenue: " + "$" + str(total_profits_losses))
    	text_file.write("\n")
    	text_file.write("Average Change: " + "$" + str(average_change))
    	text_file.write("\n")
    	text_file.write("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")")
    	text_file.write("\n")
    	text_file.write("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")")

