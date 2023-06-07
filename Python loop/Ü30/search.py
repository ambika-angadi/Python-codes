def print_list(list1, list2):
    l2 = len(list2)    
    l1 = len(list1)
    for i in range(0, l1):
            print(i+1, list1[i])
    
    for a in range(0, l2):
        print(a+1, list2[a])

obst = ["Banane","Kirsche","Apfel","Mango","Ananas"]
autos = ["BMW","Mercedes","Volkswagen","Audi"]

print_list(obst, autos)


