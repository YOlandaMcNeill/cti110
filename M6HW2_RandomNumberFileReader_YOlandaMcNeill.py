# This progrsm will read, display, and add a series of random numbers.
# 7.11.2017
# CTI-110 M6HW2 - Random Number File Reader
# YOlanda McNeill
#

import random
total = 0.0

def main():
    #Get number of integers that will be read.
    num_of_integers = int(input('How many numbers do you want to read? ' ))
    
    #Open file for reading.
    myfile = open('numbers.txt', 'r')

    #Read a series of random numbers.
    myfile.read(int(random.randint(1,23)))
    num_read = int(myfile.readline())
        
    #Close file.
    myfile.close

    #Add the numbers read.
    total = 0.0
    total = total + num_read

    #Display the numbers read and their total.
    print(num_read, 'were read from the file')
    print('Their total is: ', total)
    

 #Call the main function.
main()
    
    



