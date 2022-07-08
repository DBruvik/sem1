#This program fets a numeric test score from the
#user and displays the corresponding letter grade.

#Named constants to represent te grade thresholds.
AScore=90
BScore=80
CScore=70
DScore=60

#Get a test score from the user
score=int(input('Enter your test score: '))

#Determine the grade.
if score>=AScore:
    print('Your grade is A.')
else:
    if score>=BScore:
        print('Your grade is B.')
    else:
        if score>=CScore:
            print('Your grade is C.')
        else:
            if score>=DScore:
                print('Your grade is D.')
            else:
                print('Your grade is F.')

                
