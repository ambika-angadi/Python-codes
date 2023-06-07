#declare the first 2 terms in the series and count variable
n1 = 0
n2 = 1
count = 0
#print the first term
print (n1)
#iterate to generate the fibonacci series
while count < 10:
    fib = n1 + n2
    n1 = n2
    n2 = fib
    print(n1)
    count += 1
    
