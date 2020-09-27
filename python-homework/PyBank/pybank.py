""" PyBank Homework assignment

This script reads in provided budget_data.csv from ./Resources subdir.
The dataset has two columns: Monthly Date, Profit/Loss. From this dataset
the script:
- tallies total number of months in dataset
- calcs net total amount of P/L over entire period
- calcs avg P/L change over entire period
- determines which date had greatest increase in profits
- determines which date had greatest decrease in profits

The script prints the analysis results to the terminal and to results.txt in
Results subdir.
"""

from pathlib import Path
import csv

# Set path to input dataset
input_dataset = Path('./Resources/budget_data.csv')

# Init variables 
month_cnt = 0
total_profit = 0
max_gain_delta = 0
max_gain_month = ""
max_loss_delta = 0
max_loss_month = ""
avg_delta = 0
month_list = []
profit_list = []

# Open input dataset and build list for each of two columns
with open(input_dataset,'r') as csvinput:
    csvreader = csv.reader(csvinput, delimiter=',')
    next(csvreader)
    # Read every data row after header row
    # convert types and append to respective list
    for row in csvreader:
        date = str(row[0])
        month_list.append(date)
        profit = int(row[1])
        profit_list.append(profit)

# Analyze the profit list 
for i in range(len(profit_list)):
    month_cnt += 1
    total_profit += profit_list[i]
    # Determine delta between current and last profit values
    if i == 0:
        profit_delta = profit_list[i]
    else:
        # Calc delta and average only after first month
        profit_delta = profit_list[i] - profit_list[i-1]
        avg_delta += profit_delta        
    # Determine if present delta is greater or less than previous
    # extreme values. If so save delta value plus current month
    if profit_delta < max_loss_delta:
        max_loss_delta = profit_delta
        max_loss_month = month_list[i]
    elif profit_delta > max_gain_delta:
        max_gain_delta = profit_delta
        max_gain_month = month_list[i]
     
# Calculate average and print scan results
# reduce month count by 1 since first line not included in avg sum
avg_delta /= (month_cnt - 1)

# Create results string array for use to both terminal and file
results_txt_list = [
            "Analysis of Financial Results",
            "--------------------------------------------------------",
            f"Total months: {month_cnt}",
            f"Total profit: ${total_profit}",
            f"Average profit delta: ${avg_delta:.2f}",
            f"Greatest profit increase: ${max_gain_delta} in {max_gain_month}",
            f"Greatest profit decrease: ${max_loss_delta} in {max_loss_month}"
            ]

# Print out analytic results to terminal & results.txt in Results subdir
results_path = Path('./Results/results.txt')
with open(results_path,'w') as file:
    for line in results_txt_list:
        print(line)
        file.write(line)
        file.write("\n")

