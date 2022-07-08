#Lag en visuel visning av kilometer og prisene

print('Kilometer\tPris 1\tPris 2\t Pris 3')
print('---------------------------------------')

#Sett opp verdiene og utregningene for så å printe det ut

for kilometer in range(0,550,50):
    fastpris1=750
    fastpris2=kilometer*2+300
    fastpris3=kilometer*4+150
    print(f'{kilometer}\t\t{fastpris1}\t{fastpris2}\t{fastpris3}')


    #if alternativ 1<2 og 1<3 else if 2<1 og 2<3 alternativ 2 else 3
