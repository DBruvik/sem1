#This program gets three test scores and displays their average.
#It congratulates the user if the avarage is
#a high score.

#The HIGH_SCORE named constan holds the value that is considered a high score
HIGH_SCORE=95

#Get the three test scores
test1=int(input('Enter the score for test1: '))
test2=int(input('Enter the score for test2: '))
test3=int(input('Enter the score for test3: '))

#Calculate the average
average=(test1+test2+test3)/3

#Print the average
print(f'The average score is {average}.')

#If the average is a high score
#Congratulate the user
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')

