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

window.mainloop()
