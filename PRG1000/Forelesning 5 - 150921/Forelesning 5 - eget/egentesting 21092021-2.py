#This program averages test scores. It asks the user for the number
#of students and the number of test scored per student.

#Get the number of students
numStudents=int(input('How many students do you have?'))

#Get the number of test scores per student.
numTestScores=int(input('How many test scores per student? '))

#determine each student's average test score.
for student in range (numStudents):
    #initialize an accumulator for the test scores.
    total=0.0

    #display the stundet number
    print(f'Student number {student+1}')
    print('-------------')

    #Get the students test scores
    for testNum in range (numTestScores):
        print (f'Test numer {testNum+1}', end='')
        score=float(input(': '))

        #Add the score to the accumulator
        total+=score

    #Calculate the average test score for this student
    average=total/numTestScores

    #Display the average.
    print(f'The average for student number{student+1} '
          f' is:{average:.1f}')
    print()
