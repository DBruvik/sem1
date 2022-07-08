from tkinter import *


def beregnMarginalskatt():
    inntekt=int(lonnsinntekt.get())
    if inntekt>=964801:
        marginalskatt.set('46.4%')
    else:
        if inntekt>=617501:
            marginalskatt.set('43.4%')
        else:
            if inntekt>=245651:
                marginalskatt.set('34.4%')
            else:
                if inntekt>=224001:
                    marginalskatt.set('32.1%')
                else:
                    if inntekt>=174501:
                        marginalskatt.set('22.2%')
                    else:
                        if inntekt>=102819:
                            marginalskatt.set('20.3%')
    if inntekt<102819:
        marginalskatt.set('Nah')

window=Tk()
window.title('Marginalskattkalkulator')

#Ledetekst, inndatafelt og knapp for rad 0
#Ledetekst
lblLonnsinntekt=Label(window, text='Lønnsinntekt: ')
lblLonnsinntekt.grid(row=0, column=0, padx=15, pady=15)

#Inndatafelt
lonnsinntekt=StringVar()
entLonnsinntekt=Entry(window,width=11, textvariable=lonnsinntekt)
entLonnsinntekt.grid(row=0, column=1, padx=10, pady=15)

#Beregningsknapp
btnBeregn=Button(window, text='Beregn marginalskatteprosent', command=beregnMarginalskatt)
btnBeregn.grid(row=0, column=2, padx=10, pady=15)

#Ledetekst og utdatafelt rad 1
#Ledetekst
lblMarginalskatt=Label(window, text='Marginalskatt: ')
lblMarginalskatt.grid(row=1, column=0, padx=0, pady=15)

#Utdatafelt
marginalskatt=StringVar()
entMarginalskatt=Entry(window, width=5, state='readonly',textvariable=marginalskatt)
entMarginalskatt.grid(row=1,column=1, padx=0, pady=15)

#Avslutt knapp rad 2
btnAvslutt=Button(window, text='Avslutt', command=window.destroy)
btnAvslutt.grid(row=3, column=2, columnspan=2, pady=15)
