# Import Dependencies
import os

# Define the input file paths (absolute paths)
inputfilep1 = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyParagraph\raw_data\paragraph_1.txt'
inputfilep2 = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyParagraph\raw_data\paragraph_2.txt'
inputfiletp = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyParagraph\raw_data\test_paragraph.txt'

# Define the output file paths (absolute paths, in the same directory as the input files)
outputfilep1 = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyParagraph\p1_analysis - refactored.txt'
outputfilep2 = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyParagraph\p2_analysis - refactored.txt'
outputfiletp = r'C:\Users\franc\OneDrive\Desktop\Data Bootcamp assignments\Homework - Assignment\03-Python-Challenge\PyParagraph\tp_analysis - refactored.txt'

# List of input files and corresponding output files
paragraphs = [inputfilep1, inputfilep2, inputfiletp]
outputfile_paths = [outputfilep1, outputfilep2, outputfiletp]

# Ensure the directories for the output files exist
for outputfile_path in outputfile_paths:
    output_directory = os.path.dirname(outputfile_path)
    os.makedirs(output_directory, exist_ok=True)

# Loop through each pair of input and output files
for inputfile, outputfile_path in zip(paragraphs, outputfile_paths):
    # Open the input file and read the paragraph
    with open(inputfile, 'r') as text:
        paragraph = text.read()

    # Count words and sentences
    words = len(paragraph.split())
    sentences = sum(paragraph.count(p) for p in ".?!")

    # Calculate the average letter count per word and words per sentence
    letterperword = round(sum(len(word) for word in paragraph.split() if word.isalpha()) / words, 2)
    wordspersentence = round(words / sentences, 2)

    # Print the analysis results
    print(f"Paragraph Analysis for {inputfile}:")
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Approximate Word Count: {words}")
    print(f"Approximate Sentence Count: {sentences}")
    print(f"Average Letter Count (per word): {letterperword}")
    print(f"Average Sentence Length (in words): {wordspersentence}")
    print()

    # Write the analysis results to the output file
    with open(outputfile_path, "w") as file:
        file.write(f"Paragraph Analysis for {inputfile}:\n")
        file.write(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        file.write(f"Approximate Word Count: {words}\n")
        file.write(f"Approximate Sentence Count: {sentences}\n")
        file.write(f"Average Letter Count (per word): {letterperword}\n")
        file.write(f"Average Sentence Length (in words): {wordspersentence}\n")