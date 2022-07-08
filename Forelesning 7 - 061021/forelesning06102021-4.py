#Første og siste element i en liste skal bytte plass
talliste=[5,3,2,1,4]
print('Lista før bytte er:', talliste)
print('Første og siste element i lista skal bytte plass')
print()

#bytte er byttevariabelen vi bruker for å ta vare på første verdi
bytte=talliste[0]

#talliste av 0 får verdien til talliste av 4
talliste[0]=talliste[4]

#talliste av 4 får verdien som vi tok vare på i bytte variabelen
talliste[4]=bytte

#Lista etter bytte er
print('Lista etter bytte er', talliste)
