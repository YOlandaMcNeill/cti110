# This program will convert feet into inches.
# 6.26.2017
# CTI-110 M5T2_FeetToInches 
# YOlanda McNeill
#

CONVERSION_FACTOR = 12

def main():
    feet = float(input('Enter the number of feet: '))

    show_inches (feet)

def show_inches (ft):
    inches = ft * CONVERSION_FACTOR

    print (ft, 'feet equal', inches, 'inches.')

main()
