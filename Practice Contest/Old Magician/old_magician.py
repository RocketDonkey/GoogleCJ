#!/usr/bin/Python26

"""Google Code Jam
Practice Contest
11.3.2011

***Old Magician***

A magician does the following magic trick. He puts W white balls and B black balls in his hat and asks someone from the audience, say Bob, to remove pairs of balls in whatever order Bob would desire. After removing a pair of balls, Bob is asked to place a white ball back into the hat if they are the same color. Otherwise he is asked to place a black ball into the hat.

When Bob is left with only one ball in the hat, he asks the magician what color the last ball is. Needless to say, the magician can't see the order by which Bob does the replacements.

The problem is that the magician, like most magicians, is old and sometimes forgets how to do the trick. Being the kind person you are, you are going to help the magician.

For each pair of numbers (W,B) you are asked to output one of the following:

"WHITE" - if the last ball in the hat will be white for sure.
"BLACK" - if the last ball in the hat will be black for sure.
"UNKNOWN" - if you can't be sure of the last ball's color.
Input

The first line of the input file contains the number of cases, N. N test cases follow.

Each case contains W and B on a line separated by a space.

Output

For each input case, you should output:

Case #X: Y
where X is the number of the test case and Y is either "WHITE", "BLACK" or "UNKNOWN" as explained above. (quotes for clarity)
Limits

0 < N ≤ 1000
W + B > 0

Small dataset

0 ≤ W ≤ 1000
0 ≤ B ≤ 1000

Large dataset

0 ≤ W ≤ 109
0 ≤ B ≤ 109

Sample
Input 
2
3 1
3 6

Output 
Case #1: BLACK
Case #2: WHITE
"""

#import random <-Old way
import re
    
def main():
    """
    Old attempt is in prior versions (I was class-happy). Problem is that when
    you have millions/billions of additions/subtractions, it takes
    forever to add/remove one at a time.

    Easy way to solve is to use the evenness/oddness of the black balls.
    """

    #Read the input file and output the results
    input_file = open('A-large-practice.in', 'rU')
    file_contents = input_file.readlines()

    #Open the output file
    output_file = open('A-large-output.txt', 'w')
    
    #Determine the number of cases (even this is unnecessary)
    cases_regex = re.search('(\d+)\n', file_contents.pop(0))
    cases = cases_regex.group(1)

    """Focus only on the number of black balls"""
    i = 1
    for line in file_contents:
        
        #Black balls
        num_black = re.search('\d+\s+(\d+)\n', line).group(1)

        #Check if the balls are even/odd
        black_eo = str(bool(int(num_black)& 1))

        #Black balls govern what will be left - only need to check their evenness/oddness
        output_dict = {'True': 'BLACK', 'False': 'WHITE'}

        #Write the output
        output_file.write('Case #' + str(i) + ': ' + output_dict[black_eo] + '\n')
        print 'Case #' + str(i) + ': ' + output_dict[black_eo]

        #Increment case
        i += 1
    
if __name__ == '__main__':
    main()
