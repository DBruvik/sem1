from tkinter import *

def beregnPorto():

    vekt=int(vekten.get())
    if vekt<=20:
        porto.set('17 kr')
    elif vekt<=50:
        porto.set('24 kr')
    elif vekt<=100:
        porto.set('27 kr')
    elif vekt<=350:
        porto.set('45 kr')
    elif vekt<=1000:
        porto.set('88 kr')
    else:
        porto.set('125 kr')
        



window=Tk()
window.title('Portokalkulator')

#Ledetekst, inndatafelt og knapp for rad 0
#Ledetekst
lblForsendelse=Label(window, text='Forsendelsens vekt (i gram):')
lblForsendelse.grid(row=0, column=0, padx=2, pady=15)

#Inndatafelt
vekten=StringVar()
entVektForsendelse=Entry(window,width=8, textvariable=vekten)
entVektForsendelse.grid(row=0,column=1, padx=10)

#beregningsknapp
btnBeregn=Button(window, text='Beregn porto',command=beregnPorto)
btnBeregn.grid(row=0, column=2, padx=10)

#ledetekst og utdatafelt rad 1
#ledetekst
lblPorto=Label(window, text='Porto: ')
lblPorto.grid(row=1, column=0, padx=0, pady=15)

#utdatafalet
porto=StringVar()
entPorto=Entry(window, width=5, state='readonly',textvariable=porto)
entPorto.grid(row=1,column=1,padx=0,pady=15)

btnAvslutt=Button(window, text='Avslutt', command=window.destroy)
btnAvslutt.grid(row=3, column=2, columnspan=2, pady=15)
