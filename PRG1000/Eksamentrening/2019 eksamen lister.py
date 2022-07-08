#Program for å slå sammen to tabeller/lister til en
#etter gitt kriterie i oppgasveteksten

#l1 og l2 defineres med ulikt antall elementer i hver, nyliste defineres
#som en tomliste
l1=[1,14,26,37,100,86,77,99]
l2=[2,13,27,38,99,85,78,101,4,47,56]
nyliste=[]

#Utskrift av lister før fletting
print('Utskrift av liste 1 og liste 2, sammen med den tomme lista')
print(l1)
print(l2)
print(nyliste)
print()

listeEn=len(l1)
listeTo=len(l2)


for indeks in range(0,listeEn,1):
    listetall=l1[indeks]
    nyliste+=[listetall]

for indeks in range(0,listeTo,1):
    listetall=l2[indeks]
    nyliste+=[listetall]


print ('Den nye listen ser nå slik ut')
print (nyliste)
