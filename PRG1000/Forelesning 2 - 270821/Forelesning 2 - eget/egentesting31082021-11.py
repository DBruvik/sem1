#Named constants to represent the base hours and the overtime multiplier
BASE_HOURS=40
OT_MULTIPLIER=1.5

#Get hours worked and then hourly pay rate.
hours=float(input('Enter the number of hours worked: '))
payRate=float(input('Enter the hourly pay rate: '))

#Calculate and display the gross pay.
if hours > BASE_HOURS:
    #Calculate the gross pay with overtime
    #First, get the number of overime hours worked
    overtimeHours=hours-BASE_HOURS

    #Calculate the amount of overtime pay.
    overtimePay=overtimeHours*payRate*OT_MULTIPLIER

    #Calculate the gross pay
    grossPay=BASE_HOURS*payRate+overtimePay
else:
    #Calculate the gross pay without overtime
    grossPay=hours*payRate

#Display
print(f'THe gross pay is ${grossPay:,.2f}.')
