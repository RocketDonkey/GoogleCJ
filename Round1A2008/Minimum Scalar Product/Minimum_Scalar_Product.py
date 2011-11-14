#!/usr/bin/python

"""
Google CJ
Round 1A 2008
Minimum Scalar Product

Problem

You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn).
The scalar product of these vectors is a single number,
calculated as x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as you wish.
Choose two permutations such that the scalar product of your two new vectors
is the smallest possible, and output that minimum scalar product.

Input

The first line of the input file contains integer number
T - the number of test cases.
For each test case, the first line contains integer number n.
The next two lines contain n integers each, giving the coordinates of
v1 and v2 respectively.

Output

For each test case, output a line

Case #X: Y
where X is the test case number, starting from 1, and Y is the minimum scalar product of all permutations of the two given vectors.
"""

def pop_scalar(scalar):
    for index, item in enumerate(scalar):
        if item[-1:] == '\n':
            scalar[index] = item[:-1]
        scalar[index] = int(scalar[index])

    return scalar

#Input file
f = open('A-large-practice.in', 'rU')
f_contents = f.readlines()

#Output file
o = open('A-large-practice-solution.txt', 'w')

#Number of cases
cases = int(f_contents[0])

case_count = 1

#Primary loop
i = 1
while case_count < cases + 1:
    
    #Number of integers
    num_ints = f_contents[i]

    #Populate scalars
    scalar1 = pop_scalar(f_contents[i+1].split(' '))                  
    scalar2 = pop_scalar(f_contents[i+2].split(' '))


    #Create final solution list. The answer will be the sum of this list.
    solution_list = []

    #Multiple the max of one list by the min of the second, remove those items and contine
    item_count = len(scalar1)

    #Cycle through each vector, pulling out the max of s1 and the min of s2.
    #Multiply the two and add the result to solution_list.
    for j in range (0, item_count):
        #Max and Min
        max1 = max(scalar1)
        min2 = min(scalar2)

        #Append list
        solution_list.append(max1 * min2)

        #Remove from list
        scalar1.remove(max1)
        scalar2.remove(min2)

        #Increment
        j += 1

    solution = sum(solution_list)

    #Write the solution to the file
    o.write('Case #' + str(case_count) + ': ' + str(solution) + '\n')

    #Increment case count and master loop
    case_count += 1
    i += 3

f.close()
o.close()
