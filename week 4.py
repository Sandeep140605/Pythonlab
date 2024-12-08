#!/usr/bin/env python
# coding: utf-8

# In[5]:




def is_sorted(s):
    sort_set=sorted(s)
    if s==sort_set:
        print("True")
    else:
        print("False")
        
a=[2,5,1,8,4]
is_sorted(a)

b=[1,2,3,4,5]
is_sorted(b)


# In[6]:


a=[1,1,2,3,4,5,5]
b=set(a)

if a==b:
    print("False")
else:
    print("True")


# In[8]:


a=list(input().split())
b=set(a)

print(b)


# In[21]:


str1=input()
str2=input()

str3=str1+str2
print(str3)


# In[18]:


thisdict={}
newdict={}
n=int(input("Size of dictionary:"))
for i in range(n):
    key=input()
    value=input()
    thisdict[key]=value

print("dictionary is:")
print(thisdict)

for key,value in thisdict.items():
   
    newdict[value]=key
    
print("Inverted dictionary is:")
print(newdict)
    


# In[23]:


a=input()

print(a.replace("hi","Hello"))


# In[24]:


str1=input()
str2=str1[:-1]
if str1==str2:
    print("Palindrome")
else:
    print("Not palindrome")


# In[25]:


a=input()
b=",".join(a)
print(b)


# In[38]:


a=set(map(int,input().split()))

a.add(10)
print(a)
a.remove(2) 
a.discard(1) 
print(a) 

a.pop() 
print(a)


# # a=set(input())
# 
# a.add(10)
# print(a)
# 
# a.remove(2)
# a.discard(1)
# print(a)
# a.pop(3)
# a.pop()
# print(a)

# In[46]:


words=input("enter the sectence:")
w=words.split()
new_word=[word[0].upper()+word[1:].lower() for word in w]
print(new_word)
old_word=" ".join(new_word)
print(old_word)


# In[42]:





# In[ ]:




