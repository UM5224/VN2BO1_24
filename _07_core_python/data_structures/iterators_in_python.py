#iterators
'''
Iterator in python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
The iterator object is initialized using the iter() method. It uses the next() method for iteration
'''
#iteration happens with two methods
'''
1)iter method - __iter--
    iter method returns an iterator object
2)next method - __next__
    next method returns next item from collection
        repeated call to __next()__ will go through collection one at a time
        when there is nothing to iterate over,a Stopiteration exception is raised
'''
#imitating for loop by calling iter and next method by ourself
usernames =('vamsi123','vamsi@55','vamsi###')
looper1 = usernames.__iter__()
print(type(looper1))
print(looper1.__next__())
print(looper1.__next__())
print(looper1.__next__())

#other way
looper2=iter(usernames)
print(next(looper2))
print(next(looper2))
print(next(looper2))

#using while loop
looper3 = iter(usernames)
while True:
    try:
        user = next(looper3)
        print(user)
    except StopIteration:
        break
