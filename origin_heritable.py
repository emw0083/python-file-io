#! /usr/bin/env python3

import re

print('Opening origin.txt file')
#with open('origin.txt', 'r') as in_stream:
#    print('Opening heritable_output.txt')
#    with open('heritable_output.txt', 'w') as out_stream:
#        for line in in_stream:
#            term = 'herit'
#            re.findall(term, text, flags=re.IGNORECASE)
#
   
file = open('origin.txt')
read = file.read()
file.seek(0)
read

# create empty list
arr = []
 
line = 1
for word in read:
    if word == '\n':
        line += 1
print("Number of lines in file is: ", line)
 
for i in range(line):
    arr.append(file.readline())

def findline(word):
    for i in range(len(arr)):
        if word in arr[i]:
            print(i+1, end=", ")
            
findline('..herit..')



file.close()
