total = int(input("enter the total no of working days "))
absent = int(input("enter no of days absent "))
a = (absent/total)*100
if a<=25:
    print("you can write exam")
else:
    print("you will not be able to sit in exam")