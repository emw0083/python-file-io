#! /usr/bin/env python3

#for some reason it will not let me commit my changes so I am uploading a new file

import re
import sys

def findline(word):
    for i in range(len(arr)):
        if word in arr[i]:
            print(i+1, word, end=", ")


if __name__ == '__main__':
    print('Opening origin.txt file')
    file = open('origin.txt')
    read = file.read()
    file.seek(0)
    read
    
    in_stream = 'origin.txt'
    out_stream = 'final.txt'
    #re_pattern_string = r'\w**herit**.'
    #re_pattern_obj = re.compile(re_pattern_string)
    
    arr = []
    line = 1

    for word in read:
        if word == '\n':
            line += 1
    print("Number of lines in file is: ", line)
    for i in range(line):
        arr.append(file.readline())
   
    herit = 'herit'
   
    findline(herit)
    beta = findline(herit)
    
    
    with open('origin.txt', 'r') as in_stream:
        print('Opening origin.txt')
        with open('final.txt', 'w') as out_stream:
                for line in in_stream:
                    line = line.strip()
                    word_list = line.split()
                    word_list.sort()
                    #print(beta)
                    for word in word_list:
                        out_stream.write('{0}\n'.format(word))

    
    print("Done!")
    print('origin.txt is closed?', in_stream.closed)
    print('final.txt is closed?', out_stream.closed)

