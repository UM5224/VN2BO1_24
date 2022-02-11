#sets
'''
 set is a collection of items which is unordered,unindexed and unchangeble
'''
#properties
'''
1)sets are mutable but elements in sets are immutable
2)duplicate items in a set is not possible
#)elements in a set is not accessible,so it does not support any indexing and slicing operations'''

#creating a set
'''
 a set can be created by using set() function or by adding elements in curly braces
 '''
set1 = set("a")
print(set1)
print(type(set1))
set2 = {1,2,"five","set"}
print(set2)

#we can get the list of individual elements by looping through the set

for i in set2:
    print(i)

#adding items to a list
set2.add(5)
set2.add("msg")
print(set2)

#updating items to a list
set2.update(set1)
print('after updating set2 with set1',set2)
list = ["listele",False,250]
set2.update(list)
print('after updating list',set2)

#removing item from a list
set2.discard(1)
set2.discard("msg")
print(set2)

#removing using remove
set2.remove(250)
print(set2)

#using pop method - it removes last item -since sets are unordered-any element can be removed
ele =set2.pop()
print(ele)

#clear method- delete all elements in a set
set2.clear()
print(set2)

#delete function will delete set completly
del set2

#union of sets
'''produces a new set will all the distinct elements from both the sets'''

setA = {"a","v",34,45,7,8,'z'}
setB = {10,5,7,'v','k','l'}
newset = setA | setB
print("union",newset)

# intersection of sets
'''intersection of two sets contains common elements from both sets'''

intersec = setA&setB
print("intersection",intersec)

#difference of sets
'''it produces newset which has only elements from the first set which are not common in second set'''
setA - setB
print("after diff",setA-setB)

#comparision
set4 = {1,2,3,4}
set5 ={1,2,3,4,'a','b','c'}
result = set4.issubset(set5)
print("is set4 subset to set5",result)
result1 = set4.issuperset(set5)
print("is set4 superset to set5",result1)
#isdisjoint method-return wheter two sets have intersection or not
s=set4.isdisjoint(set5)
print(s)
s1 = set1.isdisjoint(set4)
print(s1)
