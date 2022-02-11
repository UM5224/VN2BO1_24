#dictionary
'''
Dictionaries are used to store data values in key:value pairs
A dictionary is a collection which is ordered, changeable and do not allow duplicates
key must be unique and values can be anything
'''

dic1 = {"1":"map",
        "2":"place",
        "3":"colour"}
print(dic1)
#adding item to the dictionary
dic1[4]="industry"
print(dic1)
#update the data
dic1["1"]='zone'
print(dic1)

#deleting the data
del dic1["1"]
print(dic1)

#clear
dic1.clear()
print(dic1)
dic2 ={"5":"map",
        "6":"place",
        "7":"colour" }

#dictionary functions
print(len(dic2))
print(type(dic2))
str_dic2 = str(dic2)
print(str_dic2)
print(type(str_dic2))
print(dic2.keys())#To retrieve all keys from dictionary
print(dic2.values()) #To retrieve all values from dictionary
print(dic2.items())#To retrieve all items from dictionary

#update
dict4 = {'a': 1, 'b': 2}
dict5 = {'c': 3, 'd': 4}
dict4.update(dict5)
print("Dictionary Update  : ", dict4, dict5)
#copy
dic3 = dic2.copy()
print(dic3)
print(dic2)
#get() method to get values of dict4
print(dict4.get("a"))
print(dict4.get("f","nokey"))#if there is no key default given value will print


