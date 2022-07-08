tall=int(input('Skriv inn ett positivt eller negativt tall: '))
if tall>=0:
    print('Tallet',tall,'er positivt!')
    if (tall%2)==0:
        print('Dette er ett partall!')
    else:
        print('Dette er oddetall!')
else:
    print('Tallet',tall,'er negativt!')
    if (tall%2)==0:
        print('Dette er ett partall!')
    else:
        print('Dette er oddetall!')
          
