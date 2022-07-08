#This program converts the speeds 60 kph through 130 kph
#in 10 kph increments to mph
START_SPEED = 60
END_SPEED = 131
INCREMENT = 10
CONVERSIONFACTOR = 0.6214

#print the table headings
print('KPH\MPH')
print('------------')

#print the speeds

for kph in range(START_SPEED, END_SPEED, INCREMENT):
    mph=kph*CONVERSIONFACTOR
    print(f'{kph}\t{mph:.1f}')

