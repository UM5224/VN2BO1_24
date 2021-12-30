salary = int(input("enter your salary "))
years = int(input("enter your service "))

if years>10:
    print(f"your bonus = {salary*0.10}")
elif 6<=years<=10:
    print(f"your bonus = {salary*0.08}")
else:
    print(f"your bonus = {salary*0.06}")


