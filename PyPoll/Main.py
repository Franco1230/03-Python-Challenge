# Import dependencies
import os, csv

# Declare file path
# pypoll = os.path.join("..", "PyPoll", "Resources", "budget_data.csv")
pypoll = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyPoll\Resources\election_data.csv'

# Set variables 
totalvotes = 0
khan = 0
correy = 0
li = 0
otooley = 0

# Open and read CSV
with open(pypoll) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Skip header
    pybank_header = next(csv_reader) 

    # Loop thru the rows in the file
    for row in csv_reader: 

        # Count the unique Voter ID's and store in variable into totalvotes
        totalvotes +=1

        # Count thru the times each candidates's name appears and store in a list
        # This value will be used to print the result
        if row[2] == "Khan": 
            khan +=1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li": 
            li +=1
        elif row[2] == "O'Tooley":
            otooley +=1

 # Make a dictionary out of the two lists we to find the winner
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan, correy, li, otooley]

# Zip the the list of candidate(key) and the total votes(value) together 
# Use the Max function to find the winner 
candidatesandvotes = dict(zip(candidates,votes))
key = max(candidatesandvotes, key = candidatesandvotes.get)

# Summarizing the analysis
khanrate = (khan/totalvotes) *100
correyrate = (correy/totalvotes) * 100
lirate = (li/totalvotes) * 100
otooleyrate = (otooley/totalvotes) * 100

# Print the result
print(f"Election Results")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Total Votes: {totalvotes}")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Khan: {khanrate:.3f}% ({khan})")
print(f"Correy: {correyrate:.3f}% ({correy})")
print(f"Li: {lirate:.3f}% ({li})")
print(f"O'Tooley: {otooleyrate:.3f}% ({otooley})")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Winner: {key}")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Set output file
# summaryfile = os.path.join("..", "03-Python-Challenge", "PyPoll", "Summary.txt")
summaryfile = r"C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyPoll\Summary.txt"

with open(summaryfile,"w") as file:

# Write result to txt file 
    file.write(f"Election Results\n")
    file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    file.write(f"Total Votes: {totalvotes}\n")
    file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    file.write(f"Khan: {khanrate:.3f}% ({khan})\n")
    file.write(f"Correy: {correyrate:.3f}% ({correy})\n")
    file.write(f"Li: {lirate:.3f}% ({li})\n")
    file.write(f"O'Tooley: {otooleyrate:.3f}% ({otooley})\n")
    file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    file.write(f"Winner: {key}\n")
    file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")