input1 = input("Does the system work?")
if (input1 == "ja"):
    print("Fummel nicht daran herum!")
    print("Alles ist gut")
elif (input1 == "nein"):
    input2 = input("Bist du Schuld?")
    if (input2 == "ja"):
        print("Du Idiot!")
        input3 = input("Hat es jemand gemerkt?")
        if (input3 == "ja"):
            print("Du bist am Arsch")
            input4 = input("Kannst Du einem Anderen die Schuld zuschieben?")
            if (input4 == "ja"):
                print ("Keine Sorge, jemand anderes ist im Arsch")
            elif (input4 == "nein"):
                print("Du bist wirklich im Arsch!!")
        elif (input3 == "nein"):
            print("Man wird dich nie finden")
    elif(input2 == "nein"):
        print("Dich trifft es nicht")

