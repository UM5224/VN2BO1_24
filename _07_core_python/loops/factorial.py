n=int(input("enter the number"))
if n<0:
    fact =0
    print(fact)
elif n==0 or n==1:
    fact =1
    print(fact)
else:
    fact=1
    while n>1:
        fact=fact*n
        n=n-1
    print(fact)
