import csv

with open('Samplecomments2.csv') as csvfile:
    commentreader = csv.DictReader(csvfile, delimiter=",")
    rows = list(commentreader)
    for row in rows[2:4]:
        print(row['Comment'])