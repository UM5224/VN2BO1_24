num = int(input("please enter your number "))

if num>1:
    for i in range(2,num):
        if num%i == 0:
            print("its not prime")
            break
    else:
        print("its a prime")
else:
    print("its not prime")