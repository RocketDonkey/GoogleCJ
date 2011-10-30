#!/usr/bin/Python26
# -*- coding: utf-8 -*-

"""
***SOLVED***
10.29.2011

Google CodeJam Challenges
Event: Qualification Round Africa - 2010

Problem B: Reverse Words

Given a list of space separated words, reverse the order of the words.
Each line of text contains L letters and W words.
A line will only consist of letters and space characters.
There will be exactly one space character between each pair of consecutive words.

Input

The first line of input gives the number of cases, N.
N test cases follow.
For each test case there will a line of letters and
space characters indicating a list of space separated words.
Spaces will not appear at the start or end of a line.

Output

For each test case, output one line containing "Case #x: " followed by the list of words in reverse order.

Limits

Small dataset

N = 5
1 ≤ L ≤ 25

Large dataset

N = 100
1 ≤ L ≤ 1000
"""

import re

#Open input file
f = open('B-small-practice.in', 'rU')
f_read = f.readlines()

#Open output file
o = open('Reverse Words - Small.txt', 'w')

#Add each line to a list
f_list = []
for line in f_read:
    f_list.append(line)

#Determine number of cases
cases = re.search(r'(\d+)', f_list[0]).group()

#Set main case sentinel
case = 1

"""PRIMARY LOOP***
Loop through each list item (i), reversing and outputting
"""
for i in range(1, len(f_list)):
    #Split into a list of words
    list_words = f_list[i].rsplit(' ')

    #Reverse the list
    list_reversed = list_words
    list_reversed.reverse()

    #Remove '\n' from first term (if present)
    #Interesting - \n appears to be treated as one character
    list_reversed[0] = list_reversed[0].replace('\n', '')
    
    #Determine how many words are in the list
    list_len = len(list_words)

    #Starting at the endmost value in the original list, add each to list_reversed
    o.write('Case #' + str(case) + ': ' + (' ').join(list_reversed) + '\n')
    print 'Case #' + str(case) + ': ' + (' ').join(list_reversed) + '\n'

    #Move to the next case
    case += 1
