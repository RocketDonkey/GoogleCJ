#!/usr/bin/Python26
# -*- coding: utf-8 -*-

"""
10.29.2011
Google CodeJam Challenges
Event: Qualification Round Africa - 2010

Problem A: Store Credit

You receive a credit C at a local store and would like to buy two items.
You first walk through the store and create a list L of all available items.
From this list you would like to buy two items that add up to the entire value
of the credit. The solution you provide will consist of the two integers indicating
the positions of the items in your list (smaller number first).

Input

The first line of input gives the number of cases, N.
N test cases follow. For each test case there will be:

One line containing the value C, the amount of credit you have at the store.
One line containing the value I, the number of items in the store.
One line containing a space separated list of I integers. Each integer P indicates the price of an item in the store.
Each test case will have exactly one solution.
Output

For each test case, output one line containing "Case #x: " followed by
the indices of the two items whose price adds up to the store credit.
The lower index should be output first.

Limits

5 ≤ C ≤ 1000
1 ≤ P ≤ 1000

Small dataset

N = 10
3 ≤ I ≤ 100

Large dataset

N = 50
3 ≤ I ≤ 2000
"""
import re

def Store_Credit():
    #Open the data file
    f = open('A-large-practice.in', 'rU')
    f_contents = f.readlines()

    #Open the results output file
    o = open ('Store Credit - Large.txt', 'w')

    #Store info in a list
    f_list = []
    for line in f_contents:
        f_list.append(line)

    #Extract the number of cases (on the first line)
    cases = re.search(r'\d+', f_list[0]).group()

    """PRIMARY LOOP***
    This is the main loop.
    It since the data appears in groups of 3, start at item 1 (0 is the cases)
    and increment by 3 each time
    """
    mlint = 1 #Location in the master list
    case_num = 1 #Case number

    while mlint < (len(f_list)-2):
        #Sum you are seeking
        sum_total = int(re.search(r'\d+', f_list[mlint]).group())

        #Number of terms
        terms = re.search(r'\d+', f_list[mlint+1]).group()

        #Number set
        numbers = re.findall(r'(\d+)', f_list[mlint+2])

        #Calculate
        #General pattern is to add 1+2, 1+3...1+n, 2+3, 2+4...2+n
        for i in range(0, len(numbers)):
            for j in range(i+1, len(numbers)):
                test_total = int(numbers[i]) + int(numbers[j])
                if test_total == sum_total:
                    print 'Case #' + str(case_num) + ': '  + str(i + 1) + ' ' + str(j + 1)
                    o.write('Case #' + str(case_num) + ': '  + str(i + 1) + ' ' + str(j + 1) + '\n')
            i += 1
            j = 0

        mlint += 3 #Increment position in master list
        case_num += 1 #Increment case number

def main():
    Store_Credit()

if __name__ == '__main__':
    main()
