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


    print(total_months)
    print(total_profits_losses)
    print(average_change)
    print(greatest_increase_date, greatest_increase)
    print(greatest_decrease_date, greatest_decrease)
