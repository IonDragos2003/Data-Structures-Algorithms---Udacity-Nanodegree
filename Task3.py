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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0. #Done
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9. #Done
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140. #Irrelevant. They are not calling telemarketers

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# We need to find all records which have the number which CALLED (OUT) starting with (080) - meaning someone from Bangalore called somewhere else

calls_from_bangalore = []
for record in calls:
    if (record[0].startswith('(080)')):
        calls_from_bangalore.append(record)
        
print(calls_from_bangalore[:5]) # Few instances

# Now we need to get a list of all the outgoing numbers. Meaning, the numbers which people starting with code (080) calling other numbers

outgoing_calls = []

for record in calls_from_bangalore:
    outgoing_calls.append(record[1])

print('\n')    
print(outgoing_calls[:5]) # Few instances

# Now that we have a list of the numbers people from Bangalore called, we need to extract their area codes
# First instance, if it starts with a paranthesis, we know it's a fixed line, so we need to extract the number inside the paranthesis
# Second instance, if it has a space after the first digits, it's a mobile number, so we need to get the first set of digits before the space
# Third case is irrelevant in this case but we can verify it separately. 

prefixes = []

for prefix in outgoing_calls:
    if (prefix.startswith('(')):
        prefixes.append(prefix.split(sep = ')')[0].replace('(',''))
    elif (prefix.split(sep=' ')[1] != ''):
        prefixes.append(prefix.split(sep = ' ')[0])
        
print('\n')    
print(prefixes[:5])

for prefix in outgoing_calls:
    if (prefix.startswith('140')):
        print('We are here')
        print(prefix) #Nothing here

unique_prefixes = list(set(prefixes))
sorted_prefixes = sorted(unique_prefixes)

print('The numbers called by people in Bangalore have codes:')
for prefix in sorted_prefixes:
  print(prefix)
  
    
# PART B

