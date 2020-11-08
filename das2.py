a = int(input("a:"))
b = int(input("b:"))
niilber = 0
ma = max(a,b)
mi = min(a,b)
while mi<=ma:
    print(mi)
    mi+=1
    if mi%2==0:
        niilber=niilber+mi

print(niilber)