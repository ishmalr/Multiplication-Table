print ("Multiplication Table")
for i in range(1,10):
    print(i,"|  ",end='')
    for j in range(1,10):
        a=i*j
        if a>9:
           print(a," ",end='')
        else:
           print(a,"  ",end='')
    print("\n")

