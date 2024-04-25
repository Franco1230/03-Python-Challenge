# Import Dependencies 
import os, csv
from itertools import zip_longest

# Set input file path 
# employeedata = os.path.join("03-Python-challenge", "PyBoss", "employee_data.csv")
employeedata = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyBoss\employee_data.csv'

# Set empty lists
data = []

# Make a dictionary with state names as keys and abbreviations as values 
usstateabbrev = {
    'Alabama': 'AL', 
    'Alaska': 'AK', 
    'Arizona': 'AZ', 
    'Arkansas': 'AR', 
    'California': 'CA', 
    'Colorado': 'CO',
    'Connecticut': 'CT', 
    'Delaware': 'DE', 
    'Florida': 'FL', 
    'Georgia': 'GA', 
    'Hawaii': 'HI', 
    'Idaho': 'ID',
    'Illinois': 'IL', 
    'Indiana': 'IN', 
    'Iowa': 'IA', 
    'Kansas': 'KS', 
    'Kentucky': 'KY', 
    'Louisiana': 'LA',
    'Maine': 'ME', 
    'Maryland': 'MD', 
    'Massachusetts': 'MA', 
    'Michigan': 'MI', 
    'Minnesota': 'MN', 
    'Mississippi': 'MS',
    'Missouri': 'MO', 
    'Montana': 'MT', 
    'Nebraska': 'NE', 
    'Nevada': 'NV', 
    'New Hampshire': 'NH', 
    'New Jersey': 'NJ',
    'New Mexico': 'NM', 
    'New York': 'NY', 
    'North Carolina': 'NC', 
    'North Dakota': 'ND', 
    'Ohio': 'OH', 
    'Oklahoma': 'OK',
    'Oregon': 'OR', 
    'Pennsylvania': 'PA', 
    'Rhode Island': 'RI', 
    'South Carolina': 'SC', 
    'South Dakota': 'SD',
    'Tennessee': 'TN', 
    'Texas': 'TX', 
    'Utah': 'UT', 
    'Vermont': 'VT', 
    'Virginia': 'VA', 
    'Washington': 'WA',
    'West Virginia': 'WV', 
    'Wisconsin': 'WI', 
    'Wyoming': 'WY'
}

# Open CSV in read mode with context manager
with open(employeedata, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile) 

    # Skip header 
    header = next(csvreader)     
    
    # Loop through each row in csvreader
    for row in csvreader:
        
        # Split full name into firstname and lastname
        firstname, lastname = row[1].split(" ")
        
        # Split birthday by "/", reformat it
        DOB = '/'.join(row[2].split('/')[1:] + row[2].split('/')[0:1])
        
        # Show only the last four digits of SSN
        ssn = '***-**-' + row[3].split("-")[2]
        
        # Get state abbreviation
        state = usstateabbrev[row[4]]
        
        # Append modified row to data list
        data.append([row[0], firstname, lastname, DOB, ssn, state])

# Sort the data by employee id
sorted_data = sorted(data, key=lambda x: int(x[0]))

# Set output file path
# converteddata = os.path.join("03-Python-Challenge", "PyBoss", "converted_data.csv")
converteddata = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyBoss\converted_data - refactored.csv'

# Write sorted data to CSV
with open(converteddata, "w", newline='', encoding='utf-8') as file:
    
    # Initialize csv.writer
    csvwriter = csv.writer(file)
    
    # Write the first row (headers)
    csvwriter.writerow(["Employee Id", "First Name", "Last Name", "DOB", "SSN", "State"])
    
    # Write the sorted data rows
    csvwriter.writerows(sorted_data)