shareBought=2000
sharePrice1=40.00
moneySpent=shareBought*sharePrice1
stockbrokerPay1=moneySpent*0.03

print (f'Joe bought 2000 stocks for ${moneySpent}. He then paid \
his stockbroker $ {stockbrokerPay1}.')

print ('Two weeks later he sold all his shares')
sharePrice2=42.75
shareSold=shareBought*sharePrice2
stockbrokerPay2=shareSold*0.03
moneyEarned=shareSold-moneySpent-stockbrokerPay1-stockbrokerPay2

print (f'Joe sold his shares for ${shareSold}. \
He then paid ${stockbrokerPay2} to his stockbroker. \
In total Joe earned ${moneyEarned}')
if moneyEarned < -1:
    print ('Joe lost money on his stocks.')
if moneyEarned > 1:
    print ('Joe made money on his stocks!')
    
