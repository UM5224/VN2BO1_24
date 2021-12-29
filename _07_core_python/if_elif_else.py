#correct or incorrect name
name = input('Enter name ')
if name == "abc":
    print("Correct name")
else:
    print("Incorrect name")

#find out wheter it is positive or negative or zero
num =int(input("enter the number"))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# greatest of three numbers
n1,n2,n3 = int(input("enter the number1 ")),int(input("enter the number2 ")),int(input("enter the number3 "))

if n1>n2 and n1>n3:
    print("n1 is greatest")
elif n2>n1 and n2>n3:
    print("n2 is greatest")
else:
    print("n3 is greatest")

#find wheter it is onedigit,twodigit or three digit number
n = int(input("enter the number "))

if n>=0 and n<10:
    print("one digit number")
elif n>10 and n<=100:
    print("two digit number")
elif n>100 and n<1000:
    print("three digit number")
else:
    print("either 1000 or greater than 1000")