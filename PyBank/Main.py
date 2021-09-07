# Import Dependencies
import os,csv

# Set file path
pybank = os.path.join("PyBank", "Resources", "budget_data.csv")
pybank = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyBank\Resources\budget_data.csv'

# Open and read CSV
with open(pybank) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Skip header
    pybank_header = next(csv_reader)
    
    # Count total number of rows in CSV
    totalmonths = len(list(csv_reader))

    # Reset CSV pointer
    csv_file.seek(0)
    
    # Skip header
    pybank_header = next(csv_reader)

    # Calculate the total of "Profit/Losses"    
    profit = 0
    for row in csv_reader:
        profit += float(row[1])
    
    # Reset CSV pointer
    csv_file.seek(0)
    
    # Skip header
    pybank_header = next(csv_reader)
    
    # Calculate monthly change
    change = 0
    previousprofit = 0
    averageprofit = 0
    changelist = []
    profitdiff = []
    for row in csv_reader:
        change = float(row[1]) - previousprofit
        changelist.append(change)
        previousprofit = float(row[1])
    changelist.remove(changelist[0])
    averageprofit = sum(changelist) / (len(changelist))

    # Reset CSV pointer
    csv_file.seek(0)
   
    # Skip header
    pybank_header = next(csv_reader)
    monthslist = []
    for row in csv_reader:
        monthslist.append(row[0])
       
    maxincrease = max(changelist)
    maxdecrease = min(changelist)

    maxincreasemonth = changelist.index(maxincrease) + 1
    maxdecreasemonth = changelist.index(maxdecrease) + 1
    
    # Print results
    print(f"Financial Analysis")
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Total Months:", totalmonths)
    print(f"Total: {profit}")
    print(f"Average Change: {round(averageprofit,2)}")
    print(f"Greatest Increase in Profits: {monthslist[maxincreasemonth]} (${(str(maxincrease))})")
    print(f"Greatest Decrease in Profits: {monthslist[maxdecreasemonth]} (${(str(maxdecrease))})")

# Set output file path
output_file = os.path.join("Python-Challenge", "PyBank", "Summary.txt")

output_file = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyBank\Summary.txt'

with open(output_file,"w") as file:
    
    # Write result into txt file 
    file.write(f"Financial Analysis\n")
    file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    file.write(f"Total Months: {(totalmonths)}\n")
    file.write(f"Total: ${profit}\n")
    file.write(f"Average Change: {round(averageprofit,2)}\n")
    file.write(f"Greatest Increase in Profits: {monthslist[maxincreasemonth]} (${(str(maxincrease))})\n")
    file.write(f"Greatest Decrease in Profits: {monthslist[maxdecreasemonth]} (${(str(maxdecrease))})\n")