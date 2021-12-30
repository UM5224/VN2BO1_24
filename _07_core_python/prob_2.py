p = int(input("please enter your percentage "))

if p<25:
    print("your grade is D")
elif 25<=p<45:
    print("your grade is C")
elif 45<=p<50:
    print("your grade is B")
elif 50<=p<60:
    print("your grade is B+")
elif 60<=p<80:
    print("your grade is A")
else:
    print("your grade is A+")