# This program will add random numbers to an existing file.
# 7.10.2017
# CTI-110 M6HW1 - Random Number File Writer
# YOlanda McNeill
#

import random

def main():
    #Get number of integers that will be entered.
    num_of_integers = int(input('How many numbers will be entered? ' ))

    #Open file for writing.
    myfile = open('numbers.txt', 'w')    

    #Write series of random integers to file.
    #Random integers range from 1 through 500.
    myfile.write(str(random.randint(1,500)) + '\n')    

    #Close the file.
    myfile.close()
    print(num_of_integers, 'random integers were added to numbers.txt')

#Call the main function.
main()



