# -*- coding: UTF-8 -*-
""" PyRamen Homework assignment

This script reads in provided menu_data.csv and sales_data.csv into 
separate list objects. And then aggregates calculated per product results
into report dictionary:
    01-count : total quantity for each ramen type
    02-revenue : total revenue for each ramen type
    03-cogs : total cost of goods sold for each ramen type
    04-profit : total profit for each ramen type

The script finishes by publishing the results dictionary into results.txt in
Results subdir.

"""
from pathlib import Path
import csv

# Set path to input datasets
menu_filepath = Path('./Resources/menu_data.csv')
sales_filepath = Path('./Resources/sales_data.csv')

# Init objects
menu = {}
sales = []
report = {}

# Open input menu dataset and build dict of lists
with open(menu_filepath,'r') as menu_csv:
    csvreader = csv.reader(menu_csv, delimiter=',')
    next(csvreader)
    # Read every data row after header row
    for row in csvreader:
        menu[row[0]] = row[1:]

# Open input sales dataset and build list of lists
with open(sales_filepath,'r') as sales_csv:
    csvreader = csv.reader(sales_csv, delimiter=',')
    next(csvreader)
    # Read every data row after header row
    for row in csvreader:
        sales.append(row)

# Loop thru every row in sales list to determine if its a menu item, and
# if so add to report dictionary (if not already there) and record quantity
# sales_list format: Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
row_count = 0
unknown_item = 0
for row in sales:
    row_count +=1
    menu_item = str(row[-1])
    item_quantity = int(row[-2])
    # Is this sales item on the menu?
    if menu_item in menu:
        # If so, check if menu_item already in report dict
        if menu_item in report:
            # increment quantity with sales order amount
            report[menu_item]["01-count"] += item_quantity
        # otherwise create a new dictionary for menu_item 
        # and use current sales order amount
        else:
            report[menu_item] = {
                                "01-count": item_quantity,
                                "02-revenue": 0,
                                "03-cogs": 0,
                                "04-profit": 0
                                }       
    else:
        print(f"Didnt find {menu_item} in menu!")
        unknown_item +=1

# Now loop thru report and use menu dictionary to update report's revenue, cogs fields.
# For each report entry use (quantity * revenue) - (quantity * cogs) to calc total profit
for item in report:
    if item in menu:
        item_price = int(menu[item][-2])
        item_cost = int(menu[item][-1])
        report[item]["02-revenue"] = item_price * report[item]["01-count"]
        report[item]["03-cogs"] = item_cost * report[item]["01-count"]
        report[item]["04-profit"] = report[item]["02-revenue"] - report[item]["03-cogs"]
    else:
        print(f"How did we get this far with {item} ???")
        break   

# Print out analytic results to terminal & results.txt in Results subdir
results_path = Path('./Results/results.txt')
results_hdrtxt_list = [
            "Sales Analysis Results",
            "--------------------------------------------------------",
            f"Couldnt find {unknown_item} items on the menu!",
            "--------------------------------------------------------"
            ]

with open(results_path,'w') as file:
    for line in results_hdrtxt_list:
        print(line)
        file.write(line)
        file.write("\n")

    for item in report:
        print(f"{item}:{report[item]}")
        file.write(f"{item}:{report[item]}")
        file.write("\n")
