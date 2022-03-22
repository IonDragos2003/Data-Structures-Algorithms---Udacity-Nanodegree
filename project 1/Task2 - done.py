"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

longest_call_duration = 0
longest_call_number = ''

for record in calls:
    if (int(record[-1]) > int(longest_call_duration)):
        longest_call_duration = record[-1]
        longest_call_number = record[0]
        
print(str(longest_call_number) + ' spent the longest time, '+ str(longest_call_duration) + ' seconds, on the phone during September 2016.')