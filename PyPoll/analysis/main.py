import os
import csv

# Construct the file path
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Initialize an empty list to store the header row
header_row = []
# Reading with CSV module
with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')
    total_votes = 0
    Charles_votes=0
    Diana_votes=0
    Raymon_votes=0

# Skipping header
    next(csvreader)

# Loop through each row in the CSV file
    for row in csvreader:
    # Counting votes
        total_votes += 1
    
    #finding total Charles Japser Stockham votes
        if row[2]== "Charles Casper Stockham":
            Charles_votes+=1
    #finding diana
        if row[2]== "Diana DeGette":
            Diana_votes+=1
    #finding Raymon
        if row[2]== "Raymon Anthony Doane":
            Raymon_votes+=1
            
    #calculating percentages
    Charles_percentage= (Charles_votes/ total_votes) *100
    diana_percentage= (Diana_votes/ total_votes) *100
    raymon_percentage= (Raymon_votes/ total_votes) *100
    
    #determining winner
    if Charles_percentage > diana_percentage and Charles_percentage> raymon_percentage:
        winner = "Charles Casper Stockham"
    elif diana_percentage> Charles_percentage and diana_percentage>raymon_percentage:
        winner="Diana DeGette"
    elif raymon_percentage>diana_percentage and raymon_percentage>Charles_percentage:
        winner = "Raymon Anthony Doane"
    
    
# Printing
print("Election Results")
print("-----------------------")
print("Total Votes:", total_votes)
print("--------------------")
print(f"Charles Casper Stockham:,{Charles_percentage:.3f}%,({Charles_votes})")
print(f"Diana DeGette:,{diana_percentage:.3f}%,({Diana_votes})")
print(f"Raymon Anthony Doane:,{raymon_percentage:.3f}%,({Raymon_votes})")
print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")

# Write financial analysis to the text file
with open('election_results.txt', 'w') as txtfile:

 # Write election results to the text file
    txtfile.write("Election Results\n")
    txtfile.write("-----------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-----------------------\n")
    txtfile.write(f"Charles Casper Stockham: {Charles_percentage:.3f}%, ({Charles_votes})\n")
    txtfile.write(f"Diana DeGette: {diana_percentage:.3f}%, ({Diana_votes})\n")
    txtfile.write(f"Raymon Anthony Doane: {raymon_percentage:.3f}%, ({Raymon_votes})\n")
    txtfile.write("-----------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-----------------------\n")

# Print confirmation message
print(f"Election analysis results have been saved to 'election_results.txt'")
