# This program will keep a running total of the number of bugs collected in
# 7 days.
# 6.19.2017
# CTI-110 M4T1 - Bug Collector
# YOlanda McNeill
#

#Initialize the accumulator
total = 0 

#Get the bugs collected for each day.
for day in range(1, 8):
    #prompt the user.
    print('Enter the bugs collected on day', day)
    
    #Input the number of bugs.
    bugs = int(input())

    #Add bugs to total
    total += bugs

#Display the total bugs.
    print('You collected a total of', total, 'bugs.')
