import os
import csv

# Locate the file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
# Initialize an empty list to store the header row
header_row = []

# Reading with CSV module
with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    header = next(csvreader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(csvreader)

    # Define variables to store total_months, total_profit, and max_increase
    total_months = 0
    total_profit = 0
    max_increase_month = ""
    max_increase = float("-inf")  # Initialize to negative infinity to ensure any increase will be greater
    min_decrease_month = ""  # Initialize for greatest decrease
    min_decrease = float("inf")  # Initialize to positive infinity to ensure any decrease will be smaller

    # Increment total_months for the first row
    total_months += 1

    # Read the first row and initialize prev_profit
    prev_profit = int(first_row[1])

    # Add the profit from the first row to total_profit
    total_profit += int(first_row[1])

    # Initialize a list to store changes in profit
    profit_changes = []

    # Iterate over each row in the CSV file
    for row in csvreader:
        # Increment total_months
        total_months += 1

        # Add the profit for the current row to total_profit
        total_profit += int(row[1])

        # Calculate the change in profit from the previous month
        current_profit = int(row[1])
        change_profit = current_profit - prev_profit

        # Add the change in profit to the list
        profit_changes.append(change_profit)

        # Update prev_profit for the next iteration
        prev_profit = current_profit

        # Check if the change in profit is greater than the current maximum increase
        if change_profit > max_increase:
            max_increase = change_profit
            max_increase_month = row[0]  # Store the month of the maximum increase

        # Check if the change in profit is less than the current minimum decrease
        if change_profit < min_decrease:
            min_decrease = change_profit
            min_decrease_month = row[0]  # Store the month of the maximum decrease

    # Calculate the average change
    average_change = sum(profit_changes) / (total_months - 1)

# Print financial analysis
print("Financial Analysis")
print("-----------------------")
print("Total Months:", total_months)
print(f"Total: ${total_profit}")
print(f"Average Change: $ {average_change:.2f}")  # Average change is total profit divided by total months
print("Greatest Increase in Profits:", max_increase_month, "($", max_increase, ")")
print("Greatest Decrease in Profits:", min_decrease_month, "($", min_decrease, ")")
