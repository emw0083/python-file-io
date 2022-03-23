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

hertiable =

findline('herit')

file.close()


print('Opening dummy.txt')
with open('dummy.txt', 'r') as in_stream:
    print('Opening output.txt')
    with open('output.txt', 'w') as out_stream:
        for line in in_stream:
            line = line.strip()
            word_list = line.split()
            word_list.sort()
            for word in word_list:
                out_stream.write('{0}\n'.format(word))
print("Done!")
print('dummy.txt is closed?', in_stream.closed)
print('output.txt is closed?', out_stream.closed)
