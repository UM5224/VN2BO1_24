#pickling and unpickling
'''
The process to converts any kind of python objects (list, dict, etc.) into byte streams
(0s and 1s) is called pickling or serialization or flattening or marshalling.

We can converts the byte stream (generated through pickling) back into python objects by a
process called as unpickling
'''
import pickle
dict = {'minutes':5,'daily':1,'weekly':7,}
f=open("dict.txt",'wb')
pickle.dump(dict,f)
f.close()
f2 =open("dict.txt","rb")
obj =pickle.load(f2)
print(obj)
f2.close()