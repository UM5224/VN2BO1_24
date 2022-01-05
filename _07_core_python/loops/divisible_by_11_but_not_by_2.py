num1 = int(input("enter the first num"))
num2 = int(input("enter the second num"))
for i in range(num1,num2+1):
    if i%2 != 0 and i%11 == 0:
        print(i)