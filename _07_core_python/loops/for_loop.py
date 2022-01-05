#for loop
'''
*It enables us to alter the flow of the program
*we can repeat the same code for a finite number of times
*It provides code re-usability
* we can traverse over the elements of data structures (lists,tuples,dics,sets)
*for loop is used in the case where we need to execute some part of the code
until the given condition is satisfied
*It is better to use for loop if the number of iteration is known in advance
# '''
#syntax
'''
        for <var> in <sequence>:
           # statements
'''
# for val in range(0):#nothing prints
#     print("Range val : ", val)
# for val in range(1):#prints only zero
#     print("Range val : ", val)
# # for val in range(1, 16, 2):#prints range values with difference 2
# #     print("Range val: ", val)
# for val in range(20, 1):#prints nothing
#     print("Range val: ", val)
# for val in range(20, 1, -1):#prints reverse from 20 to 2
#     print("Range val: ", val)
# for val in range(-20, -40):#prints nothing
#     print("Range val: ", val)
# for val in range(-20, -40, -1):#prints reverse from -20 to -39
#     print("Range val: ", val)
emp_details = {'eid': 100,
               'ename': 'MadhuN',
               'sal': 12500}
# for key, val in emp_details.items():#prints both key and its value
#     print(key, val)
for key, val in emp_details.values():#doubt(error comes)
    print(key, val)
for key, val in emp_details():#doubt(error comes)
    print(key, val)

#nested for loop
'''
Python allows us to nest any number of for loops inside a for loop. 
The inner loop is executed n number of times for every iteration of the outer loop. 
'''
#syntax
'''
for iterating_var1 in sequence:  #outer loop
    for iterating_var2 in sequence:  #inner loop
        #block of statements
    #other statements
#other statements
'''
#else statement with for loop
'''
Using else statement with for loop
Unlike other languages like C, C++, or Java, Python allows us to use the else statement 
with the for loop which can be executed only when all the iterations are exhausted. 
Here, we must notice that if the loop contains any of the break statement then the else statement will not be executed.
'''