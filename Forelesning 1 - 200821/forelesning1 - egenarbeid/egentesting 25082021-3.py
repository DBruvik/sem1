min_liste = [1,4,6,8,9,3,2,5,7,0]
min_liste = sorted(min_liste, reverse=True)
print (min_liste)

#ovenfor er fra høyeste til laveste fordi reverse = rekkefølgen

min_liste=[1,4,6,8,9,3,2,5,7,0]
min_liste=sorted(min_liste, reverse=False)
print(min_liste)

min_liste.sort(reverse=False)
print(min_liste[::-1])

# Ovenfor er alternativ måte og løse det på

min_liste=[1,4,6,8,9,3,2,5,7,0]
print ('Summen er totalt', sum(min_liste))

min_liste=[1,4,6,8,9,3,2,5,7,0]
min_liste=sorted(min_liste, reverse=False)
print (min_liste)
print ('Største tallet er:', max(min_liste))
print ('Summen av tallene er', sum(min_liste))
