# This program will calculate a person's BMI and determine if their weight is opimal, underweight, or over weight.
# 6.14.2017
# CTI-110 M3HW1 - Body Mass Index
# YOlanda McNeill
#

#Get user's height.
height = int(input('Enter your height in inches: '))

#Get user's weight.
weight = int(input('Enter your weight in pounds: '))

#Calculate BMI.
BMI = float(weight * 703/height**2)
print('BMI=',BMI)

if BMI < 18.5:
    print('UNDERWEIGHT.')

elif BMI >= 18.5 or BMI < 25:
        print('Weight is OPTIMAL.')

else:
    print('OVERWEIGHT.')
