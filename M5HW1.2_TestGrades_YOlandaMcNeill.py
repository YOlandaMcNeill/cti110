# This program will calculate the average of 5 test scores
# 6.27.2017
# CTI-110 M5HW1 - Test Average and Grade
# YOlanda McNeill
#


def main():
    print('Please enter 5 test scores.')
    score1 = int(input('Enter the test score: '))
    score2 = int(input('Enter the test score: '))
    score3 = int(input('Enter the test score: '))
    score4 = int(input('Enter the test score: '))
    score5 = int(input('Enter the test score: '))

    print('score 1:', determine_grade(score1))
    print('score 2:', determine_grade(score2))
    print('score 3:', determine_grade(score3))
    print('score 4:', determine_grade(score4))
    print('score 5:', determine_grade(score5))

    print('average: ',calc_average(score1, score2, score3, score4, score5))

def calc_average(score1, score2, score3, score4, score5):
    total = score1 + score2 + score3 + score4 + score5
    average = total / 5
    
    return average

def determine_grade(score):
    if score >= 90:
        letterGrade = 'A'
        return letterGrade     

    else:
        if score > 79 and score <= 89:
            letterGrade = 'B'
            return letterGrade

        else:
            if score > 69 and score <= 79:
                letterGrade = 'C'
                return letterGrade

            else:
                if score > 59 and score <= 69:
                    letterGrade = 'D'
                    return letterGrade

                else:
                    letterGrade = 'F'
                    

                return letterGrade

main()
    


    
