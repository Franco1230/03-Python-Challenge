# Import Dependencies 
import os, csv

# Set file path (change between "paragraph_1" or "paragraph_2")
inputfile = os.path.join("Python-Challenge", "PyParagraph", "raw_data", "test_paragraph.txt")
inputfile = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyParagraph\raw_data\test_paragraph.txt'

# Open file and read txt 
with open(inputfile) as text:
    paragraph = text.read()

# Use list comprehension to split the text file into words using space as the delimeter and return the appended array "words" and count length of array
words = len([word for word in paragraph.split(sep = " ")])

# Use list comprehension to split the text file into sentences by using ".", "!" and "?" as the delimeters and return the appended array "sentences" and count length of array
sentences = len([word for word in paragraph if word is "."]) + len([word for word in paragraph if word is "?"]) +  len([word for word in paragraph if word is "!"])

# Use isalpha function to calculate the average letters in words 
letterperword = round(len([c for c in paragraph if c.isalpha()])/words, 2)

# Calculate the average words in sentences 
wordspersentence = round(words/sentences, 2)

# Print result
print(f"Paragraph Analysis")
print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Approximate Word Count: {words}")
print(f"Approximate Sentence Count: {sentences}")
print(f"Average Letter Count (per word): {letterperword}")
print(f"Average Sentence Length (in words): {wordspersentence}")


# Set Output files
outputfile = os.path.join("Python-Challenge", "PyParagraph", "tp_analysis.txt")
outputfile = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\Python-Challenge\PyParagraph\tp_analysis.txt'

with open(outputfile,"w") as file:
    
# Write methods to export paragraph analysis
    file.write(f"Paragraph Analysis\n")
    file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    file.write(f"Approximate Word Count: {words}\n")
    file.write(f"Approximate Sentence Count: {sentences}\n")
    file.write(f"Average Letter Count (per word): {letterperword}\n")
    file.write(f"Average Sentence Length (in words): {wordspersentence}\n")
