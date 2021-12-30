a = int(input("enter the amount "))
prod =input("please enter your product ")

if 0<=a<=100:
    if prod == "pants":
        d = a*0.03
        print("discount",d)
        print(f"amount ={a-d}")
    elif prod=="shirts":
        d= a*0.05
        print("discount",d)
        print(f"amount ={a-d}")
    else:
        d= 0
        print("discount",d)
        print(f"amount ={a-d}")
elif 101<=a<=200:
    if prod=="shorts":
        d= a*0.05
        print("discount",d)
        print(f"amount ={a-d}")
    elif prod=="pants":
        d=a*0.08
        print("discount",d)
        print(f"amount ={a-d}")
    else:
        d=a*0.10
        print("discount",d)
        print(f"d={a*0.10}")
elif 201<=a<=300:
    if prod=="shorts":
        d=a*0.10
        print("discount",d)
        print(f"amount={a-d}")
    elif prod=="pants":
        d=a*0.12
        print("discount",d)
        print(f"amount ={a-d}")
    else:
        d=a*0.15
        print("discount",d)
        print(f"amount={a-d}")
else:
    if prod=="shorts":
        d=a*0.18
        print("discount",d)
        print(f"amount={a - d}")
    elif prod=="pants":
        d=a*0.20
        print("discount",d)
        print(f"amount={a - d}")
    else:
        d=a*0.22
        print("discount",d)
        print(f"amount={a-d}")

