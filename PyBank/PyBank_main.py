# Import Modules

import os
import csv
os.getcwd()

# Set path
budget_data = r"C:\Users\Owner\Documents\Data Boot Camp\Challenge_3\Python-Challenge\PyBank\Resources\budget_data.csv"

# Set lists and read data from csv file
with open(budget_data, 'r') as csvfile:
    month_count = []
    pl_list = []
    g_profit = 0
    g_loss = 0
    total = 0
    average = 0
    # Split the data on commas
    csvreader =csv.reader(csvfile, delimiter=',')
    next(csvreader)

    # Set for loop to append lists
    for row in csvreader:
        month_count.append(row[0])      
        pl_list.append (int(row[1]))

    #Find greatest profit/loss with month it occured    
    difference =  [pl_list [i + 1] - pl_list[i] for i in range(len(pl_list)-1)]             
    g_profit = max (difference)
    g_loss = min(difference)

    # Find index for greatest profit/loss
    gp_index = difference.index(g_profit)
    gl_index = difference.index(g_loss)

    # Set greates profit/loss months
    g_profit_m = month_count[gp_index + 1]
    g_loss_m = month_count[gl_index +1]

    # Find total profit/loss and average difference change
    total = [total + float(pl_list[i]) for i in range (0,len(pl_list))]
    total_pl = sum(total)
    average = sum(difference) / len(difference)
    total_months = len(month_count)
    
    # Print analysis
    print()
    print (f"Financial Analysis")
    print()
    print (f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (f"Total Months: {total_months}")
    print(f"Total: ${total_pl}")
    print(f"Average Change: ${round(average, 2)}")
    print (f"Greatest Increase in Profits: {g_profit_m} (${g_profit}) ")
    print (f"Greatest Decreasenin Profits: {g_loss_m} (${g_loss})")
    

    