#Import the os module and csv file module
import os
import csv

#set path
csvpath = os.path.join("Resources", "budget_data.csv")

#Set starting values
number_of_months = 0
month_number = []
amount_change_list = []
net_total = 0
greatest_increase_profit = ["", 0]
greatest_decrease_losses = ["", 10000000000000000000]


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first
    csv_header = next(csvreader)

    # First row information
    row_one = next(csvreader)
    number_of_months += 1
    net_total += int(row_one[1])
    previous_amount = int(row_one[1])

    # Read each row of data after the header
    for row in csvreader:
        number_of_months += 1
        net_total += int(row[1])
        
        amount = int(row[1]) - previous_amount
        previous_amount = int(row[1])
        amount_change_list += [amount]
        month_number = [month_number] + [row[0]]

        # Find the greatest increase
        if amount > greatest_increase_profit[1]:
            greatest_increase_profit[1] = amount
            greatest_increase_profit[0] = row[0]

        # Find the greatest decrease
        if amount < greatest_decrease_losses[1]:
            greatest_decrease_losses[1] = amount
            greatest_decrease_losses[0] = row[0]


# The average of the changes in "Profit/Losses" over the entire period
average_change = sum(amount_change_list) / len(amount_change_list)


#Summary Analysis
financial_analysis = (
    f"Financial Analysis\n"
    f"--------------------------------------------------\n"
    f"Total Months: {number_of_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_profit[0]} (${greatest_increase_profit[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_losses[0]} (${greatest_decrease_losses[1]})")

# Print the analysis to terminal
print(financial_analysis)

# Export to text file
financial_output = os.path.join("Resources", "financial_analysis.txt")

with open(financial_output, "w") as txt_file:
    txt_file.write(financial_analysis)