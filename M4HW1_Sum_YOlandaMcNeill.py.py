# This program will calculate the sum of a series of numbers
# 6.19.2017
# CTI-110 M4HW1 - Sum of Numbers
# YOlanda McNeill

#Initialize the accumulator.
total = 0.0
number = 0

#Explain what's happening
print('This program will calculate the sum of a series of numbers.')

#Get a number.
while not (number <0):
    print('Enter a number: ')
    number = int(input())
    if number >0:
        total = total + number
    

#Display the total of the numbers.
print('The total is', total)


