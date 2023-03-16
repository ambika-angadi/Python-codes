txt = "Hallo Ihr"
print (txt)

x:int = 5; y:float = 7.34
#x = 5; y = 7.34
sum = x + y
print (sum)
print (type(x))
print (str(x))
print (type(y))
print (type(sum))
x = "Danke, hat spass gemacht"
print (type(x))

#Boolean values
value1 = 100
value2 = 23
if (value1 > value2):
    print ("value1 is greater than value2")
else:
    print ("value1 is smaller as value2")
isLoggedIn = True
if (isLoggedIn == True):
    print ("User is logged in")
else:
    print ("User is not logged in")

Kind = 16
if (Kind < 6):
    print ("Go to bed at 7")
elif ((Kind >= 6) & (Kind <= 12)):

    print ("Go to bed at 10pm")
else:
    print ("Off the lights when you come home")

no_of_guests = 33
isVegetarian = True
mercimek = ["onions", "oil", "tomato paste", "red lentils", "potatoes", "mint"]
print (type(mercimek))
print (mercimek)
mercimek.append("chilly powder")
print (mercimek)
print (mercimek[0])
print (mercimek[4])
print (mercimek[3])
print ("Anzahl der Zutaten" +  str(len(mercimek)))
mercimek.insert(2, "salt")
for zutat in mercimek:
    print (zutat)
    print (len(zutat))

krimskrams = {"Knöpfe", "Aufnaeher", "Stifte"}
#krimskrams[1] = "neu"
print (type(krimskrams))
for zeugs in krimskrams:
    print (zeugs)

Gruppe = ("Anja", "Mohanad", "Florian")
print (type(Gruppe))
for teilnehmer in Gruppe:
    print (teilnehmer)