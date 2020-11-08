n = int(input("n:"))
niilber = 0
while n>0:
    niilber+=n%10
    n=n//10

print(niilber)