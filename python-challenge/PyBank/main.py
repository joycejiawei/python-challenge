import csv

file_to_input = "budget_data.csv"
file_to_output = "financial_analysis.txt"

total_months = 0
total_profits = 0
prev_profits = 0
month_of_change = []
profits_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_profits = 0

with open(file_to_input) as profits_data:
    reader = csv.DictReader(profits_data)

    for row in reader:

        # The total number of months included in the dataset
        total_months = total_months + 1

        # The net total amount of "Profit/Losses" over the entire period
        total_profits = total_profits + int(row["Profit/Losses"])

        # Track the profit/losses change
        profits_change = int(row["Profit/Losses"]) - prev_profits
        prev_profits = int(row["Profit/Losses"])
        profits_change_list = profits_change_list + [profits_change]
        month_of_change = month_of_change + [row["Date"]]

        # The greatest increase in profits (date and amount) over the entire period
        if (profits_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = profits_change

        # The greatest decrease in losses (date and amount) over the entire period
        if (profits_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = profits_change


# The average of the changes in "Profit/Losses" over the entire period
profits_avg = sum(profits_change_list) / len(profits_change_list)

output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_proftis}\n"
    f"Average Change: ${profits_avg}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)