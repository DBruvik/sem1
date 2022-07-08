#Get the desired future value.
futureValue=float(input('Enter the desired future value: '))

#Get the annual interest rate
rate=float(input('Enter the annual interest rate: '))

#get the number of years that the money will appreciate
years=int(input('Enter the number of years the money will grow: '))

#Calculate the amount needed to deposit
presentValue=futureValue/(1.0+rate)**years

#Display the amount needed to deposit
print('You will need to deposit this amount: ', presentValue)

