str = "VAmseedhar\treddy{}"
print(len(str))
print(str.capitalize())
print(str.endswith("reddy"))
print(str.count("e"))
print(str.replace("reddy",'buddy'))
print(str.find("reddy"))
print(str.casefold())
print(str.center(30,"@"))
x = str.encode()
print(x)
print(str.expandtabs())
print(str.expandtabs(1))
print(str.expandtabs(2))
print(str.expandtabs(3))
print(str.expandtabs(10))
print(str.format("gudur"))
print(str.index("see"))
str1 = "python001200"
print(str1.isalnum())
print(str1.isdecimal())
print(str1.isalpha())
str3 = "vamsi"
print(str3.isalpha())
print(str3.islower())
print(str3.isnumeric())
print(str.isnumeric())
str4 = "71234"
print(str4.isnumeric())
print(str.isprintable())
print(str3.isprintable())
str5 = " "
print(str5.isspace())
print(str.isspace())
str6 = "Hey You"
print(str6.istitle())
print(str.istitle())
str7 = "USYFUY"
print(str7.isupper())
y = "#$%".join(str6)
print(str6)
v = ("apple","lap","True","device")
z = "*=@".join(v)
print(z)
txt = "banana"

x = txt.ljust(15)

print(x, "is my favorite fruit.")
print(str.lower())
txt = "         hello banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")
txt = "Hello Sam!"

mytable = txt.maketrans("S", "P")

print(mytable)
print(txt.translate(mytable))

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

def gold():
    print("gold")