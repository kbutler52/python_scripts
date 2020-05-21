#05-21-2020
avocados= int(input("How many avocados do you have?  "))#stores the number of avocados
strawberries = int(input("How many strawberries do you have?  "))#stores the number of strawberries
#objective determine if we have more, equal to or less than strawberries

print(avocados > strawberries)#check our if condition
print(avocados == strawberries)#check our elif condition
print(avocados < strawberries)#check our else condition

if avocados > strawberries:
    print("We have more avocados that strawberries")
elif avocados == strawberries:
    print("We have the same number of Avocados as Strawberries")

else:
    print("We have less Avocados than Strawberries")

