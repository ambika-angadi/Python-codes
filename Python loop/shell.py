#msh
while True:
    eingabe = input("$>> ") #echo hallo
    x = eingabe.split(" ")
    if x[0] == "echo":
        for i in range(1, len(x)):
            print(x[i], end=" ")
        print()
    elif x[0] == "exit":
        break
    elif x[0] == "touch": #touch datei1.txt
        if len(x) >= 2:
            for i in range(1, len(x)):
                open(x[i], "x")
        else:
            print("bitte gib einen dateiname an")




