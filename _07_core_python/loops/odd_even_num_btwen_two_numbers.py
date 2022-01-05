num1 = int(input("enter the first num "))
num2 = int(input("enter the second num "))
sum1 = 0
sum2 = 0
for i in range(num1,num2+1):
    if i%2 == 0:
        sum1 = sum1 + i
    else:
        sum2 = sum2 + i
print("sum of even numbers",sum1)
print("sum of odd numbers",sum2)
print("sum of both even and odd numbers",sum1+sum2)