# This program will convert kilometers to miles.
# 6.25.2017
# CTI-110 M5T1_KilometerConverter 
# YOlanda McNeill
#

CONVERSION_FACTOR = 0.6214

def main():
    kilometers = float (input('Enter the distace in kilometers: '))

    show_miles (kilometers)

def show_miles (km):
    miles = km * CONVERSION_FACTOR

    print (km,  'kilometers equal', miles, 'miles.')

main()
