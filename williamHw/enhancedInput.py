#05-20-2020
#Casting: changes the data type of a value
#int(...) whatever is inside , changes to inger

#cat = int(input("Enter:"))
#print("ILove  " + cat)


avocados = int(input("How many avocados  do you have?"))# stores the number of avocados
strawberries = int(input("How many strawberries do you have?"))#stores the number of strawberries

#objective: Determine if we have more, equal to or less avocados than strawberries

print(avocados > strawberries)#checks our if condition
print(avocados == strawberries)#checks our elif condition
print(avocados < strawberries)# checks our else condition

if avocados > strawberries:
    print("We have more avocados that Strawberries")
elif avocados == strawberries:
    print("We have the same number of avocados and strawberries")
else:
    print("We have less avocados than strawberries")


