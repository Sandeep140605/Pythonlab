#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=10
b=20
print(a+b)


# In[9]:


a=int(input())
b=int(input())
print(a+b)


# In[11]:


a=int(input())
b=int(input())
print(a*b)


# In[19]:


import math
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
d=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(d)


# In[23]:


name=input()
phone=int(input())
address=input()
email=input()
print(name)
print(phone)
print(address)
print(email)


# In[27]:



principal=int(input())
rate=float(input())
time=int(input()) 
times_compounded=int(input())
    
amount = principal * (1 + rate / times_compounded) ** (times_compounded * time)
compound_interest = amount - principal
print( compound_interest)






# In[ ]:




