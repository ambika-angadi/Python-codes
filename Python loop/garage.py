#Liste der Autos in der Garage
autos = ["BMW", "Audi", "VW", "Fiat", "Seat", "Porsche", "Trabi", "Mercedes", "Opel"]

#Alle Autos in der Garage ausgeben
print ("Autos in der Garage:")
for auto in autos:
    print(auto)
ausgeliehene_autos = input("Geben Sie die ausgeliehene Autos ein, getrennt durch Kommas:")
ausgeliehene_autos = ausgeliehene_autos.split(",")

#Liste der verbliebenen Autos in der Garage erstellen
verbliebenen_autos = [auto for auto in autos if auto not in ausgeliehene_autos]

#Verbleibende Autos in der Garage ausgeben
print ("Verbleibende Autos in der Garage:")
for auto in verbliebenen_autos:
    print(auto)