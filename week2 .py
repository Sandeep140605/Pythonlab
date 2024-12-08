#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(dir(list))


# In[2]:


help(list)


# In[4]:


a=input()
if a.isdigit():
    print("digit")
elif a.isupper():
    print("upper")
elif a.islower():
    print("lower")


# In[8]:


a=0
b=1
i=0
n=int(input())
print(a)
print(b)
while i<=n-3:
    c=a+b
    print(c)
    a=b
    b=c
    i=i+1

    


# In[9]:


i=0
j=0
a=5
for i in range(5):
    for j in range(j<=i):
        print(a)
    a=a-1
       


# In[17]:


n = int(input())

for i in range(n, 0, -1):
    for j in range(n-i+1):
        print(i, end=' ')
    
    print()


# In[18]:


import math
a=int(input())
b=int(input())
print(math.lcm(a,b))


# In[23]:


n=int(input())
i=0
for i in range(2,n):
    for j in range(2,(i//2)+1):
        if i%j==0:
            break
    else:
            print(i)


# In[ ]:





# In[ ]:




