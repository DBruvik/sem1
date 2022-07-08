#evig loop

keepGoing='y'
while keepGoing=='y':
    sales=float(input('Enter the amount of sales:'))
    commRate=float(input('Enter the commission rate'))
    commission=sales*commRate

    print (f'The commission is ${commission:,.2f}.')
