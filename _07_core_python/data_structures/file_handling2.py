with open("this.txt","r+") as f:
    print(f.read())
    f.write("\nhello python")
    print(f.read())

with open("demo2.txt","w+") as f:
    f.write("this is file handling")
    print(f.read())

with open("new.txt","a+") as f:
    f.write("hello new file")
    print(f.read())