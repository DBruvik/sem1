#This program gets an item's original price and calculates
#its sale price, with a 20% discount
#get thye item's original price
originalPrice=float(input('Enter the items original price: '))

#Calculate the amount of the discount
discount=originalPrice*0.2

#Calculate the sale price
salePrice=originalPrice-discount

#Display
print('The sale price is',salePrice)
