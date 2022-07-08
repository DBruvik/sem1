#INtroduksjon til GUI-programmering
#Grunnstruktur
#Med komponentene ledetekst, inndatafelt, utdatafelt, knapp
#Så legger vi til kode for å foreta "beregningene"
#Variabler må knyttes til inndatafeltene og utdatafeltene, før plassering i grid
#Lager en avslutt-knapp for å slippe å bruke "lukk vindu [x]"


from tkinter import *

def beregnLan():
    if (int(egenkapital.get())/int(kjopesum.get()))>=0.35:
        lanetilsagn.set('Lån innvilges')
    else:
        lanetilsagn.set('Lån innvilges ikke')
        


window=Tk()

#Vi gir vinduet ett navn
window.title('Lånekalkulator Billån')

#Vi lager ledetekster for kjøpesum, egenkapital og lånetilsagn
lblKjopesum=Label(window, text='Kjøpesum: ')
lblKjopesum.grid(row=0, column=0, padx=100, pady=15)

lblEgenkapital=Label(window,text='Egenkapital: ')
lblEgenkapital.grid(row=1, column=0, padx=100, pady=15)

lblLanetilsagn=Label(window, text='Lånetilsagn')
lblLanetilsagn.grid(row=3, column=0, padx=100, pady=15)

#Vi lager inndatafelt for kjøpesum og egenkapital
kjopesum=StringVar()
entKjopesum=Entry(window, width=9, textvariable=kjopesum)
entKjopesum.grid(row=0, column=1, padx=100, pady=15)

egenkapital=StringVar()
entEgenkapital=Entry(window,width=9, textvariable=egenkapital)
entEgenkapital.grid(row=1, column=1, padx=100, pady=15)

#Vi lager knapp for å beregne lånetilsagnet
btnBeregn=Button(window, text='Beregn lånetilsagn', command=beregnLan)
btnBeregn.grid(row=2, column=0, columnspan=2, pady=15)

#Vi lager et utdatafelt/visningsfelt for konklusjonen på lånetilsagnet
lanetilsagn=StringVar()
entLanetilsagn=Entry(window, width=20, state='readonly', textvariable=lanetilsagn)
entLanetilsagn.grid(row=3, column=1, padx=100, pady=15)

#Knapp for å avslutte
btnAvslutt=Button(window, text='Avslutt', command=window.destroy)
btnAvslutt.grid(row=5, column=0, columnspan=2, pady=15)



window.mainloop()


#Arbeidsliste
#1) Samle definisjon av ledetekst, komponent og variabel for de som hører sammen
#2) Bruke lokale variabler på get'ere og set'ere
#   endre linje 12 til "normaliserte" variabler ek=int(egenkapital.get()) forkorte de
#3) Lage GUI-basert grensesnitt på (enkle) programmer fra tidligere i høst












