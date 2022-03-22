"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
texts_calls = texts.copy()
texts_calls.extend(calls)


unique_numbers = []

for record in texts_calls:
    unique_numbers.append(record[0])
    unique_numbers.append(record[1])

no_unique_numbers = len(set(unique_numbers))

print ('There are ' + str(no_unique_numbers) + ' different telephone numbers in the records.')