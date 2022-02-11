#arrays
'''
1) an array is the data structure that contain fixed eelements of same data type
2) an array has index and elements ,index are where an element stores
3)stores multiple values in a single variable
4)it contains items stored in continuos memory locations
'''
import array

array1 = array.array('i',[1,2,3,4,5])
print(array1)
print(type(array1))

for k in array1:
    print(k)

for every in range(len(array1)):
    print(array1[1])

#adding elemets
array1.insert(1,20)
print(array1)

print(array1[3])
print(array1[4])