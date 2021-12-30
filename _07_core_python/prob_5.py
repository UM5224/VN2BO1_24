num = int(input("enter no of days "))

if num<=5:
    print(f"charge = {num*2}")
elif 6<=num<=10:
    print(f"charge = {num*3}")
elif 11<=num<=15:
    print(f"charge = {num*4}")
else:
    print(f"charge = {num*5}")

