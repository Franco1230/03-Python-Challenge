import os, csv

# Define a function to process the election results
def process_election_results(input_csv_path):
    # Initialize vote counters
    total_votes = 0
    candidates = {"Khan": 0, "Correy": 0, "Li": 0, "O'Tooley": 0}

    # Open the CSV file and process the data
    with open(input_csv_path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        # Skip the header row
        header = next(csv_reader)

        # Loop through the CSV rows and count votes
        for row in csv_reader:
            total_votes += 1
            candidate_name = row[2]  # Assuming candidate name is in the 3rd column
            if candidate_name in candidates:
                candidates[candidate_name] += 1

    return total_votes, candidates

# Define a function to summarize the election results
def summarize_results(total_votes, candidates):
    # Calculate the percentage of votes for each candidate
    results = {}
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        results[candidate] = {
            "votes": votes,
            "percentage": round(percentage, 3),
        }

    # Determine the winner
    winner = max(candidates, key=candidates.get)

    return results, winner

# Define a function to print the results
def print_results(total_votes, results, winner):
    print("Election Results")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Total Votes: {total_votes}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for candidate, data in results.items():
        print(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Winner: {winner}")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# Define a function to write the results to a text file
def write_results(output_path, total_votes, results, winner):
    with open(output_path, "w") as file:
        file.write("Election Results\n")
        file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        file.write(f"Total Votes: {total_votes}\n")
        file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        for candidate, data in results.items():
            file.write(f"{candidate}: {data['percentage']:.3f}% ({data['votes']})\n")
        file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        file.write(f"Winner: {winner}\n")
        file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

# Define file paths
# input_csv_path = os.path.join("..", "PyPoll", "Resources", "budget_data.csv")
input_csv_path = r"C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyPoll\Resources\election_data.csv"
# output_summary_path = os.path.join("..", "03-Python-Challenge", "PyPoll", "Summary - refactored.txt")
output_summary_path = r"C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyPoll\Summary - refactored.txt"

# Process election results
total_votes, candidates = process_election_results(input_csv_path)

# Summarize results and determine the winner
results, winner = summarize_results(total_votes, candidates)

# Print results
print_results(total_votes, results, winner)

# Write results to a text file
write_results(output_summary_path, total_votes, results, winner)