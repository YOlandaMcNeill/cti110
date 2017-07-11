# This program will display all the numbers in a file named:
# numbers.txt
# 7.10.2017
# CTI-110 M5T1 - File Display
# YOlanda McNeill
#

# Open the file with variable named 'myfile'.
# 'numbers.txt' is the file name that will be open as READ ONLY.

myfile = open('numbers.txt', 'r')

# Once file is open it can be processed.
# Read and display the file's contents.
# 'For' loop already knows how many lines are in the file.
# 'myfile' is file object we are reading from.
# Convert line that is read from the fie into an integer for future
# text problems.

for line in myfile:
    number = int(line)
    print(number)

#Close the file.
myfile.close()


