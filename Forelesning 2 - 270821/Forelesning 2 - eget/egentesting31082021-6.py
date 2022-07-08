#Get a number of seconds from the user

totalSeconds=float(input('Enter a number of seconds: '))

#Get the number of hours
hours=totalSeconds//3600

#get the remaining minutes
minutes=(totalSeconds//60)%60

#Get the number of remaining seconds
seconds=totalSeconds%60

#Display
print('Here is the time in hours, minutes and seconds: ')
print('Hours: ', hours)
print('Minutes: ', minutes)
print('Seconds: ', seconds)
