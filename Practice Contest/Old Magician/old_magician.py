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
    Old attempt is below (I was class-happy). Problem is that when
    you have millions/billions of additions/subtractions, it takes
    forever. Easy way to solve is to use the evenness/oddness of the black balls.
    """

    #Read the input file and output the results
    input_file = open('A-large-practice.in', 'rU')
    file_contents = input_file.readlines()

    #Open the output file
    output_file = open('A-large-output.txt', 'w')
    
    #Determine the number of cases
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
    
    """THIS IS THE HARD WAY - TRY THE EASY WAY
#This whole class if full of awesome-sounding references, all related to balls.
class SackOfBalls:
    def __init__(self, wballs, bballs):
        self.wballs = int(wballs)
        self.bballs = int(bballs)
        
        #Define a dictionary that will be used for random ball selection
        self.ball_dict = {1:'W', 2:'B'}


    def addBall(self, color, num_balls):
        #Add a ball depending on the color
        if color == 'W':
            self.wballs += 1
        elif color == 'B':
            self.bballs += 1
        else:
            print 'No balls added.'


    def pullBalls(self):
        #Randomly generate a ball color
        ball_color_1 = self.ball_dict[random.randint(1,2)]

        #Remove the first ball
        if ball_color_1 == 'W':
            self.wballs -= 1
        else:
            self.bballs -= 1

        #Now check to see if there are still balls of each color in the sack
        if self.wballs > 0 and self.bballs > 0:
            #If so, no restrictions on second ball removal
            ball_color_2 = self.ball_dict[random.randint(1,2)]

            #Second ball color is white
            if ball_color_2 == 'W':
                #If first ball also white, end because you've already removed one white ball
                if ball_color_1 == 'W':
                    pass
                #If the first ball is black, remove the white ball and then add back the black
                elif ball_color_1 == 'B':
                    self.wballs -= 1
                    self.bballs += 1

                #Second ball color is black
            elif ball_color_2 == 'B':
                #If first ball white, don't do anything (instead of just removing the black and replacing it)
                if ball_color_1 == 'W':
                    pass

                #If first ball also black, remove the second black and add a white
                if ball_color_1 == 'B':
                    self.bballs -=1
                    self.wballs +=1
                
        #If there is only one of either color left in the sack, 
        elif self.wballs == 0:
            #If this is zero, first ball must be white and next will be black. Pass.
            pass

        #Only white balls left
        elif self.bballs == 0:
            #Means that the first ball was black, next must be white. Subtract white, add black.
            self.wballs -= 1
            self.bballs += 1


    def sumBalls(self):
        return self.wballs + self.bballs


    def __str__(self):
        return 'White balls: ' + str(self.wballs) + '\n' + \
               'Black balls: ' + str(self.bballs)

    #The bag will be instantiated as a class.
    #The addition/removal of balls will be methods.
    #A random number generator will be used to simulate which balls are removed

    i = 1
    #for i in range (1, 6):
    for line in file_contents:
        #Determine how many of each ball to add
        #White balls
        print line
        num_white = re.search('(\d+)\s+\d+\n', line).group(1)

        #Black balls
        num_black = re.search('\d+\s+(\d+)\n', line).group(1)
        
        #Add initial balls to the sack (NSFW?)
        sack = SackOfBalls(num_white, num_black)
        #print sack.sumBalls()
        #print sack
        
        #Pull balls from your sack, filthy bird
        #If more than one ball is left, proceed
        while sack.sumBalls() > 2:

            #Remove two balls from the sack
            if sack.wballs > 0 and sack.bballs > 0:
                #print sack.sumBalls()
                sack.pullBalls()
            elif sack.wballs == 0:
                #print sack.sumBalls()
                sack.bballs -= 2
                sack.wballs += 1
            elif sack.bballs == 0:
                #print sack.sumBalls()
                sack.wballs -= 1

        #If there are two balls left, there is a fixed set of outcomes
        #They be tricky - if there are two balls left, do below - otherwise, return the only ball
        if sack.sumBalls() > 1:
            outcomes = {1.5:'BLACK', 1:'WHITE', 2:'WHITE'}

            #To get each key, divide the # of white balls by two and add the # of black balls
            lookup = (sack.wballs/2.0) + sack.bballs #Convert division to float

            output_file.write('Case #' + str(i) + ': ' + outcomes[lookup] + '\n')
        elif sack.sumBalls() == 1:
            if sack.wballs > 0:
                output_file.write('Case #' + str(i) + ': WHITE\n')
            else:
                output_file.write('Case #' + str(i) + ': BLACK\n')
        else:
           output_file.write('Case #' + str(i) + ': UNKNOWN\n')
        i += 1
   """ 

if __name__ == '__main__':
    main()
