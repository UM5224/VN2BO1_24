#python_file_opening_modes
'''
r Mode in Python File Opening
r+ Mode in Python File Opening
w Mode in Python File Opening
w+ Mode in Python File Opening
a Mode in Python File Opening
a+ Mode in Python File Opening
x Mode in Python File Opening
'''
file = open("this.txt","r")
print(file.read())
file.close()

file = open("this.txt","r")
print(file.read(12))
file.close()

f1 = open("demo.txt","w")
f1.writelines(["its a demo file\n","it stores no data\n"])
f1.close()

with open("demo2.txt","w") as myFile:
    myFile.write("this is my text file\n")


with open("demo2.txt","a") as myFile:
    myFile.write("this is my text file\n")
    myFile.write("this is my text file\n")
