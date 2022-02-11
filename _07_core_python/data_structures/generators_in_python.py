#generators
'''
A generator is a function that acts like an iterator
generator generates elements in a loop
a function that uses yeild instead of return is generator function or generator

'''
import string


def gener():
    yield 10
    yield 20
    yield 30

print(gener())

for x in gener():
    print(x)

def letters():
    for c in string.ascii_lowercase:
        yield c

for letter in letters():
    print(letter,end='')

import itertools
def prime_num():
    yield 2
    prime_cache =[2]

    for n in itertools.count(3,2):
        is_prime =True

        for p in prime_cache:
            if n%2 == 0:
                is_prime = False
                break
        if is_prime:
            prime_cache.append(n)
            yield n

for p in prime_num():
    print(p,end='')
    if p>100:
        break

#generator expression

squares = (x*x for x in itertools.count(1))

for sq_value in squares:
    print(sq_value)
    if sq_value>30:
        break