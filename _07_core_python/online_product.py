online =["pen","book","chocolate"]

product = input("please enter your product ")

if product in online:
    print(f"you purchase {product}")
else:
    print("choose only from available products")