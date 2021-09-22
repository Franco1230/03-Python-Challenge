# Import Dependencies 
import os, csv
from itertools import zip_longest

# Set input file path 
employeedata = os.path.join("Python-challenge", "PyBoss", "employee_data.csv")
employeedata = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyBoss\employee_data.csv'

# Set empty lists)
employeeid = []
fullname = []
firstname = []
lastname = []
birthday = []
DOB = []
ssn = []
hiddenssn = []
stateabbrev = []

# Make a dictionary with states names as keys and abbreviations as values 
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
    'Wyoming': 'WY',
}

# Open CSV in read mode with context manager
with open(employeedata) as csvfile:
    csvreader = csv.reader(csvfile) 

    # Skip header 
    header = next(csvreader)     
    
    # Loop through each row in csvreader
    for row in csvreader:

        # Append employee id into list
        employeeid.append(row[0])


        # Split full name into firstname and lastname lists 
        fullname = row[1].split(" ")   
        firstname.append(fullname[0])
        lastname.append(fullname[1])

        # Split birthday by "/", three lists are indexed and stored in birthday
        # Append and transform birthday into DOB list
        birthday = row[2].split("/")
        DOB.append(birthday[1]+ "/" + birthday[0] + "/" + birthday[2])
         
        

        # Split the SSN by "-"
        # Append and transform ssn into hiddenssn list 
        ssn = row[3].split("-")
        hiddenssn.append("***-**-" + ssn[2])

        # Matching state list item to a dictionary value, append dictionary key to list stateabbrev if match
        stateabbrev.append(usstateabbrev[row[4]])

# Set output file path
converteddata = os.path.join("Python-Challenge", "PyBoss", "converted_data.csv")
converteddata = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyBoss\converted_data.csv'

# Initiat each column to be in order
Rows = [employeeid, firstname, lastname, DOB, hiddenssn, stateabbrev]

# Converting lists into columns into a CSV file
exportdata = zip_longest(*Rows, fillvalue = '')

with open(converteddata,"w", newline = '', encoding = "utf-8") as file:

    # Initialize csv.writer
    csvwriter = csv.writer(file)

    # Write the first row (headers)
    csvwriter.writerow(["Employee Id", "First Name", "Last Name", "DOB", "SSN", "State"])
    
    # Write the the rest or the rows
    csvwriter.writerows(exportdata)
