#typecasting

#convert one data type to another using fuctions like int(),float(),bool(),str()

num = 100

f = float(num)
print(f)

b = bool(num)
print(b)

s = str(num)
print(s)

str2 = "laptop"

bool1 = bool("laptop")

print(bool1)

is_there = True

str1 = str(is_there)

print(is_there)
# string indexing and slicing
print(str2[0])
print(str2[4])
print(str2[0:])
print(str2[:])
print(str2[:5])
print(str2[:6])
print(str2[:7])
print(str2[-3:1])
print(str2[-3:3])
print(str2[-6:1])
print(str2[-5:3])
print(str2[-6:-1])
print(str2[-1:1])
print(str2[-2:2])
print(str2[-6:-2])
print(str2[-6:6])
print(str2[0:0])

#collections in python
#list are containers to store set of values of any data types
#lists-indexing and slicing

l1 = [1,2,3]

l2 = [20,l1,"name",is_there,None,[21,22,23],(31,32),{"key1":"data","key2":"meta"},{5,6,"man"}]

print(l2)

print(l2[1])
print(l2[1:6])
print(l2[0:4])

#tuple

#tuple is an immutable data type in python
#once defined,a tuple cannot be altered or manipulaterd

t1 = () #an empty tuple
t2 = (1,)  # a tuple with one element needs coma,otherwise it will become an integer data type
t3 = (1,l1,"sport")
print(t1)
print(t2)
print(t3)

#dictionary
#dictionary is a collection of key value pairs

dic = {}
dic1 = {"1":"integer","l1":"list","s1":"set"}
print(dic)
print(dic1)
print(dic1["l1"])
print(dic1.keys())

#sets
#set is a collection of non repetitive elements
#there is no way to change items in list

s={1,"python",True,20.5,1}
print(s)
s.add('java')
print(s)

