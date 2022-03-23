#! /usr/bin/env python3

import re

def findline(word):
    for i in range(len(arr)):
        if word in arr[i]:
            print(i+1, word, end=", ")
            
print('Opening origin.txt file')
   
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

#def findline(word):
#    for i in range(len(arr)):
#        if word in arr[i]:
#            print(i+1, end=", ")
            
findline('herit')



file.close()
