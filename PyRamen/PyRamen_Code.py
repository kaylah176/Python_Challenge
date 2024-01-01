#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import libraries 
import csv 
from pathlib import Path


# In[25]:


menu_filepath = ('/Users/kaylahoffman/UCB-VIRT-FIN-PT-12-2023-U-LOLC/Python_Challenge/PyRamen/menu_data.csv')
sales_filepath = ('/Users/kaylahoffman/UCB-VIRT-FIN-PT-12-2023-U-LOLC/Python_Challenge/PyRamen/sales_data.csv')


# In[26]:


# Initialize list objects to hold our menu and sales data 
menu = []
sales = []


# In[27]:


import pandas as pd

def read_csv(menu_filepath):
    # Read the CSV file using pandas
    df = pd.read_csv(menu_filepath)

    # Assuming the first three columns are 'item', 'category', 'description'
    # and the last two columns are 'price', 'cost'
    # We will create a new DataFrame with these specific columns
    desired_columns = ['item', 'category', 'description', 'price', 'cost']
    df_selected = df[desired_columns]
    
    # Convert the DataFrame into a dictionary format
    result_dict = df_selected.to_dict(orient='records')

    return df_selected

# Replace 'your_file.csv' with the path to your CSV file
df_result = read_csv(menu_filepath)

# Display the resulting DataFrame
print(df_result)


# In[28]:


## Read in the sales data into the sales list 
import pandas as pd

def read_csv(sales_filepath):
    # Read the CSV file using pandas
    df = pd.read_csv(sales_filepath)

    # Assuming the first three columns are 'item', 'category', 'description'
    # and the last two columns are 'price', 'cost'
    # We will create a new DataFrame with these specific columns
    desired_columns = ['Line_Item_ID', 'Date', 'Credit_Card_Number', 'Menu_Item']
    df_selected = df[desired_columns]
    
    # Convert the DataFrame into a dictionary format
    result_dict = df_selected.to_dict(orient='records')

    return df_selected

# Replace 'your_file.csv' with the path to your CSV file
df_result = read_csv(sales_filepath)

# Display the resulting DataFrame
print(df_result)


# In[29]:


# Import libraries
import csv
from pathlib import Path

# Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('menu_data.csv')
sales_filepath = Path('sales_data.csv')

# Initialize list objects to hold our menu and sales data
menu = []
sales = []

# Read in the menu data into the menu list
with open(menu_filepath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header
    for row in csv_reader:
        menu.append(row)

# Read in the sales data into the sales list
with open(sales_filepath, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header
    for row in csv_reader:
        sales.append(row)

# Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# Loop over every row in the sales list object
for sale in sales:
    # Initialize sales data variables
    line_item_id, date, credit_card_number, quantity, menu_item = sale
    quantity = int(quantity)

    # If the item value not in the report, add it as a new entry with initialized metrics
    if menu_item not in report:
        report[menu_item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
        }

    # For every row in our sales data, loop over the menu records to determine a match
    for item in menu:
        # Initialize menu data variables
        item_name, category, description, price, cost = item
        price = float(price)
        cost = float(cost)

        # Calculate profit of each item in the menu data
        profit = price - cost

        # If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if menu_item == item_name:
            # Cumulatively add up the metrics for each item key
            report[menu_item]["01-count"] += quantity
            report[menu_item]["02-revenue"] += price * quantity
            report[menu_item]["03-cogs"] += cost * quantity
            report[menu_item]["04-profit"] += profit * quantity
            break

    # Increment the row counter by 1
    row_count += 1

# Print total number of records in sales data
print(f"Total number of records in sales data: {row_count}")


# In[30]:


# Define the correct output file path 
output_file_path = '/Users/kaylahoffman/UCB-VIRT-FIN-PT-12-2023-U-LOLC/Python_Challenge/PyRamen/PyRamen_analysis.txt'

# Write the analysis report to a text file
with open('report.txt', 'w') as file:
    for key, value in report.items():
        file.write(f"{key} {value}\n")

# Usage
output_file_path = 'PyRamen_analysis.txt'  # Path for the output text file

