# Import CSV
import csv

# Open specific CSV file
with open('Samplecomments2.csv') as csvfile:
    commentreader = csv.DictReader(csvfile, delimiter=",")
    # Assigning function name commentrows
    commentrows = list(commentreader)
    # For every other row, print what's in the "Comment" column;
    # can remove [::] to print all, or put [0:4] to print the first 4
    for row in commentrows[::2]:
        print(row['Comment'])

# Test to find membership of key word in rows (does not currently work)
    # for row in commentrows:
    #     if 'training' in commentrows[1:4]:
    #         print('Training is here!') 
    #     else:
    #         print('Training is not here!')

# Test to find frequency of word "training" in comments (does not currently work)
    # for row in commentrows:
    #     print(commentrows.count('Training'))