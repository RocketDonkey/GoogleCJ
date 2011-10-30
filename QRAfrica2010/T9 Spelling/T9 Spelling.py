#!/usr/bin/Python26
# -*- coding: utf-8 -*-

"""
***SOLVED***
10.29.2011

Google CodeJam Challenges
Event: Qualification Round Africa - 2010

Problem C: T9 Spelling

Problem

The Latin alphabet contains 26 characters and telephones only have ten digits on the keypad.
We would like to make it easier to write a message to your friend using a sequence of
keypresses to indicate the desired characters.
The letters are mapped onto the digits as shown below.
To insert the character B for instance, the program would press 22.
In order to insert two characters in sequence from the same key, the user must pause before
pressing the key a second time. T
he space character ' ' should be printed to indicate a pause.
For example, 2 2 indicates AA whereas 22 indicates B.

Input

The first line of input gives the number of cases, N.
N test cases follow. Each case is a line of text formatted as

desired_message

Each message will consist of only lowercase characters a-z and space characters ' '.
Pressing zero emits a space.

Output

For each test case, output one line containing "Case #x: " followed by the message
translated into the sequence of keypresses.

Limits

1 ≤ N ≤ 100.

Small dataset

1 ≤ length of message in characters ≤ 15.

Large dataset

1 ≤ length of message in characters ≤ 1000.

"""

import re

def Spelling():
    #Open input file
    f = open('C-large-practice.in', 'rU')
    f_read = f.readlines()

    #Open output file
    o = open('T9 Spelling - Large.txt', 'w')

    #Add file contents to a list
    list_contents = []
    for line in f_read:
        list_contents.append(line)

    #Determine the number of cases
    cases = re.search(r'(\d+)', list_contents[0]).group()

    #Set up dictionary and add space character
    num_dict = {}
    num_dict[chr(32)] = str(0)
    j = 2
    i = 97
    
    """
    Char 97 is 'a'
    Create loop that creates the key dictionary
    Multiply the string of the value by how much you want to repeat it
    """
    while i < 123: #Character after z
        #If it is a 4-digit key...
        if i in (112, 119):
            for k in range(1, 5):
                num_dict[str(chr(i))] = str(j) * k
                i += 1

        #3-digit key
        else:
            for k in range(1, 4):
                num_dict[str(chr(i))] = str(j) * k
                i += 1
        j += 1

    #Set main loop sentinel and create empty list
    #Clean this up because it is filthy
    case = 1
    letter_map = []
    final_output = []
    for p in range(1, len(list_contents)):
        for letter in list_contents[p]:
            if letter not in (chr(10)):
                if letter in num_dict:
                    letter_map.append(num_dict[letter])

        for i in range(0, len(letter_map)):
            if i > 0:
                if letter_map[i][0] == letter_map[i-1][0]:
                    final_output.append(' ')
            final_output.append(letter_map[i])
        print 'Case #' + str(case) + ': ' + ''.join(final_output)
        o.write('Case #' + str(case) + ': ' + ''.join(final_output) + '\n')

        #Prepare for next cycle
        case += 1
        letter_map = []
        final_output = []
    
def main():
    Spelling()

if __name__ == '__main__':
    main()
