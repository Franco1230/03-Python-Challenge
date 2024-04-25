import os, csv

def calculate_financial_metrics(csv_reader):
    total_months = 0
    total_profit = 0
    previous_profit = 0
    total_change = 0
    changelist = []
    monthslist = []

    for row in csv_reader:
        # Increment total months
        total_months += 1

        # Add profit to total
        profit = int(row[1])
        total_profit += profit
        
        # Track changes in profit
        if total_months > 1:
            change = profit - previous_profit
            total_change += change
            changelist.append(change)
        previous_profit = profit

        # Store months
        monthslist.append(row[0])

    # Calculate average change
    average_change = total_change / (total_months - 1)
    
    # Find greatest increase and decrease
    max_increase = max(changelist)
    max_decrease = min(changelist)

    max_increase_month = monthslist[changelist.index(max_increase) + 1]
    max_decrease_month = monthslist[changelist.index(max_decrease) + 1]

    return total_months, total_profit, average_change, max_increase, max_increase_month, max_decrease, max_decrease_month

def print_results(total_months, total_profit, average_change, max_increase, max_increase_month, max_decrease, max_decrease_month):
    print("Financial Analysis")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})")
    print(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})")

def write_results_to_file(total_months, total_profit, average_change, max_increase, max_increase_month, max_decrease, max_decrease_month):
    # output_file = os.path.join("03-Python-Challenge", "PyBank", "Summary - refactored.txt")
    output_file = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyBank\Summary - refactored.txt'
    with open(output_file, "w") as file:
        file.write("Financial Analysis\n")
        file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${total_profit}\n")
        file.write(f"Average Change: ${average_change:.2f}\n")
        file.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
        file.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")

# Set file path
pybank = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyBank\Resources\budget_data.csv'

# Open and read CSV
with open(pybank) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip header
    next(csv_reader)

    # Calculate financial metrics
    total_months, total_profit, average_change, max_increase, max_increase_month, max_decrease, max_decrease_month = calculate_financial_metrics(csv_reader)

# Print results
print_results(total_months, total_profit, average_change, max_increase, max_increase_month, max_decrease, max_decrease_month)

# Write results to file
write_results_to_file(total_months, total_profit, average_change, max_increase, max_increase_month, max_decrease, max_decrease_month)