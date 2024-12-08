#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
list1=[1,2,3]
tuple2=(5,10)
a1=np.array(list1)
a2=np.array(tuple2)
print("list converted to array is :",a1)
print("tuple converted to array is :",a2)


# In[9]:


import numpy as np
list1=[1,2,3]
tuple2=(3,5,10)
a1=np.array(list1)
a2=np.array(tuple2)
a3=np.intersect1d(a1,a2)
print(a3)


# In[11]:


import math
def gcdab(a,b):
    c=math.gcd(a,b)
    print ("gcd is ",c)
gcdab(2,4)


# In[18]:


a=input()
b=a[::-1]
if a == b:
    print("true")
else:
    print("false")


# In[25]:


import statistics as s
list1=[1,1,3,4,5,5,5,8,9]

print(list1)
#mean
print("mean :",(sum(list1)/len(list1)))

#median
print("median :",s.median(list1))

#mode
print("mode :",s.mode(list1))


# In[28]:


#creating tuple
#1
tuple1=("name",1,"true",1+3j)
print(tuple1)

#2
a=[1,2,3,4,5]
x=tuple(a)
print(x)
print(type(x))

#3
y=tuple(("a",1,1+2j))
print(y)


# In[29]:


tuple1=("name",1,"true",1+3j)
print(tuple1)
print("check whether 1 is there or not")
print(1 in tuple1)


# In[37]:


tuple1=("name",1,"true",1+3j)
print(tuple1)
print("check whether 1 is there or not")
print(2 in tuple1)


# In[ ]:





# In[ ]:




