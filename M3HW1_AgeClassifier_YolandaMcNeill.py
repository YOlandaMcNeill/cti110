# This program will classify a person based on their age.
# 6.14.2017
# CTI-110 M3HW1 - Age Classifier
# YOlanda McNeill
#

#Get user's age.
age = int(input('Enter your age: '))

#Classify user.
if age < 1:
    print('This person is an INFANT.')

elif age >= 1 or age < 13:
    print('This person is a CHILD.')

elif age >= 13 or age < 20:
    print('This person is a TEENAGER.')

else:
    print('This person is an ADULT.')
