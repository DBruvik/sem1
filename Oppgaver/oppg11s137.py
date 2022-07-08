kvinne=int(input('Hvor mange kvinner er det i klassen? '))
menn=int(input('Hvor mange menn er det i klassen? '))
klasseAntall=kvinne+menn
kvinneProsent=kvinne/klasseAntall*100
mennProsent=menn/klasseAntall*100

print (f'Det er {kvinneProsent:.0f} % kvinner og {mennProsent:.0f} % menn') 
