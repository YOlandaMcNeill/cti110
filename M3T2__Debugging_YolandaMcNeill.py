# This example code will show proper alignment and indentation of nested if-else statements.
# 6.14.2017
# CTI-110 M3T2 - Debugging
# YOlanda McNeill
#

if score >= A_score:
    print('Your grade is A.')

else:
    if score >= B_score:
        print('Your grade is B.')

    else:
        if score >= C_score:
          print('Your grade is C.')

        else:
            if score >= D_score:
              print('Your grade is D.')

            else:
                  print('Your grade is F.')
    
