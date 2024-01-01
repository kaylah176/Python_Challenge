#!/usr/bin/env python
# coding: utf-8

# In[30]:


##Instructor Demo: CSV Reader.

##This script will use the Pathlib library to set the file path,
##use the csv library to read in the file, iterate over each
##row of the file to capture employee salaries, calculate min,
##max, avg metrics of employee salaries, and write the metrics
##to a csv file. 


# In[31]:


# Import the pathlib and csv library
from pathlib import Path
import csv

# Import pands library 
import pandas as pd 


# In[32]:


# Set the file path
csvpath = Path('/Users/kaylahoffman/UCB-VIRT-FIN-PT-12-2023-U-LOLC/Python_Challenge/PyBank/budget_data.csv')


# ### Total Number of Months in the Dataset

# In[54]:


# Print the total number of months in the dataset 
# The name of the column that contains the date information
month_column_name = 'Date'
# The name of the column that contains the Profit/Loss information
profit_loss_column = 'Profit/Losses'

# Set to store unique months
unique_months = set()

# Read the CSV file
## What does 'encoding ='utf-8' do: 
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract the month from the row
        month = row[month_column_name]
        unique_months.add(month)

# Print the total number of months
print(f"Total number of unique months in the dataset: {total_months}")


# In[34]:


# Initialize line_num variable
line_num = 0

# Open the input path as a file object
with open(csvpath, 'r') as csvfile:

    # Print the datatype of the file object
    print(type(csvfile))

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print the datatype of the csvreader
    print(type(csvreader))

    # Go to the next row from the start of the file
    # (which is often the first row/header) and iterate line_num by 1
    header = next(csvreader)
    line_num += 1
    # Print the header
    print(f"{header} <---- HEADER")
    
# Read each row of data after the header
    for row in csvreader:
        # Print the row
        print(row)
        # Set salary variable equal to the value in the 4th column of each row
        salary = int(row[1])


# ### Data Analysis

# In[50]:


import csv

# Define the path to the uploaded CSV file
file_path = '/Users/kaylahoffman/UCB-VIRT-FIN-PT-12-2023-U-LOLC/Python_Challenge/PyBank/budget_data.csv'

# Initialize variables
total_months = 0
net_total_profit_loss = 0
previous_month_profit_loss = None
total_change = 0
greatest_increase = ["", 0]  # [date, amount]
greatest_decrease = ["", 0]  # [date, amount]

# Read the CSV file
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)

    # Skip the header
    next(csv_reader)

    # Process each row in the CSV file
    for row in csv_reader:
        # Increment the total number of months
        total_months += 1

        # Current month's profit/loss
        current_month_profit_loss = int(row[1])
        net_total_profit_loss += current_month_profit_loss

        # Calculate the change from the previous month
        if previous_month_profit_loss is not None:
            change = current_month_profit_loss - previous_month_profit_loss
            total_change += change

            # Check for greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase = [row[0], change]

            # Check for greatest decrease in losses
            if change < greatest_decrease[1]:
                greatest_decrease = [row[0], change]

        # Update the previous month's profit/loss for next iteration
        previous_month_profit_loss = current_month_profit_loss

# Calculate the average change
average_change = total_change / (total_months - 1) if total_months > 1 else 0

# Output the results
# Assuming results is your dictionary
results = {
    "Total Months": total_months,
    "Net Total Amount of Profit/Losses": net_total_profit_loss,
    "Average Change in Profit/Losses": average_change,
    "Greatest Increase in Profits": greatest_increase,
    "Greatest Decrease in Losses": greatest_decrease
}

# Format the analysis report as a string
analysis_report = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {results['Total Months']}\n"
    f"Net Total Amount of Profit/Losses: ${results['Net Total Amount of Profit/Losses']}\n"
    f"Average Change in Profit/Losses: ${results['Average Change in Profit/Losses']:.2f}\n"
    f"Greatest Increase in Profits: {results['Greatest Increase in Profits'][0]} (${results['Greatest Increase in Profits'][1]})\n"
    f"Greatest Decrease in Losses: {results['Greatest Decrease in Losses'][0]} (${results['Greatest Decrease in Losses'][1]})\n"
)

# Usage
csv_file_path = '/Users/kaylahoffman/UCB-VIRT-FIN-PT-12-2023-U-LOLC/Python_Challenge/PyBank/budget_data.csv'  # Replace with the path to your CSV file
 
# Define the correct output file path 
output_file_path = '/Users/kaylahoffman/UCB-VIRT-FIN-PT-12-2023-U-LOLC/Python_Challenge/PyBank/financial_analysis.txt'

# Write the analysis report to a text file
with open(output_file_path, 'w') as file:
    file.write(analysis_report)

# Write the analysis report to a text file
with open(output_file_path, 'w') as file:
    file.write(analysis_report)

# Usage
csv_file_path = '/Users/kaylahoffman/UCB-VIRT-FIN-PT-12-2023-U-LOLC/Python_Challenge/PyBank/budget_data.csv'  # Replace with the path to your CSV file
output_file_path = 'financial_analysis_report.txt'  # Path for the output text file


# In[ ]:




