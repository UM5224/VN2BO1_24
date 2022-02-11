l = [1,2,3,"python",True,10]
print(len(l))
print(type(l))
print(l[3])
print(l[2:])
if 3 in l:
    print("yes")
l[3]="java"
print(l)
l[0:3]=4,5,6
print(l)
m = ["sda","jdfy"]
n = m+l
print(n)
l.insert(5,12)
print(l)
l.append("R")
print(l)
l.clear()
print(l)
list = l.copy()
print(list)
y = [45,54,"maths","subject",45,54]
num = y.count(54)
print(num)
z = ['telugu', 'tamil', 'english']
y.extend(z)
print(y)
index_value = y.index(54)
print(index_value)
y.insert(5,"2020")
print(y)
y.pop(1)
print(y)
y.pop()
print(y)
y.reverse()
print(y)
z.sort()
print(z)
