talliste=[]
for indeks in range(0,5,1):
    listeverdi=int(input('Oppgi tall: '))
    talliste+=[listeverdi]
listeverdi=sorted (talliste, reverse=False)
print(talliste)
print(listeverdi)
