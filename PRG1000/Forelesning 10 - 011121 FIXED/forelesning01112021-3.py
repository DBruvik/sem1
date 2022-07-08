#INtroduksjon til GUI-programmering
#Grunnstruktur
#Med komponentene ledetekst, inndatafelt, utdatafelt, knapp

from tkinter import *
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
entKjopesum=Entry(window, width=9)
entKjopesum.grid(row=0, column=1, padx=100, pady=15)

entEgenkapital=Entry(window,width=9)
entEgenkapital.grid(row=1, column=1, padx=100, pady=15)

#Vi lager knapp for å beregne lånetilsagnet
btnBeregn=Button(window, text='Beregn lånetilsagn')
btnBeregn.grid(row=2, column=0, columnspan=2, pady=15)

#Vi lager et utdatafelt/visningsfelt for konklusjonen på lånetilsagnet
entLanetilsagn=Entry(window, width=20, state='readonly')
entLanetilsagn.grid(row=3, column=1, padx=100, pady=15)


window.mainloop()
