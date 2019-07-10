#!/usr/bin/env python
# coding: utf-8

# In[1]:


#dictionaries
di ={"name":"gitam","email":"gitam@gmail.com","address":"hyderabad"}
print(di)


# In[2]:


di["name"]


# In[3]:


di["email"]="gitam-python@gmail.com"#update the data


# In[6]:


di["email"]


# In[5]:


del di ["email"]


# In[7]:


di


# In[9]:


di.keys()


# In[10]:


di.values()


# In[13]:


#tuples
contacts ={}
def addcontact(name,phone):
    if name not in contacts:
        print("contact is added ")
    else:
        print("contact details are there")
    return
addcontact('hemanth','9701871161')


# In[14]:


def search(name):
    if name not in contacts:
        print("contact is not present")
    else:
        print(contact[name])
    return


# In[15]:


#merging dictionaries 
def importcontacts(new):
    contacts.update(new)
    print(len(new.keys()),"contacts added")
    return
new={"ba":12345678901}
importcontacts(new)


# In[16]:


contacts


# In[18]:


def delete(name):
    if name in contacts:
        del contacts[name]
        print(name,"deleted")
    else:
        print("-_-")
delete("bc")


# In[29]:


def fibnoci(n):
    fib = [0,1]
    a=0
    b=1
    for i in range(1,n-1):
        c=a+b
        fib.
        a=b
        b=c
    fib.reverse()
    print(fib)
    return
fibnoci(12)
        


# In[2]:


def strs(s1,s2):
    li=[]
    if (len(s1)<len(s2)):
        print("-_-")
        t=s1
        s1=s2
        s2=t
    for i in range(0,len(s1)):
        print(i)
        print(len(s2))
        if i>len(s2):
            print("__")
            li.append(s1[i]+"*")
        elif i<len(s2):
            li.append(s1[i]+s2[i])
    print(li)
strs("bad","water")
s1.
        
        
        
        
    
    


# In[3]:


s1='gitam'
print(s1.upper())


# ###### 

# In[9]:


s1='Gitam'
print(s1.islower())


# # string handling function

# In[10]:


print(s1.istitle())


# In[12]:


print(s1.isalnum())


# In[13]:


print(s1.isalpha())


# In[14]:


print("2".join(s1))


# In[17]:


li = ['python',"me",'yes']
print(','.join(li))


# In[18]:


li.append(list(s1))
li


# In[20]:


print(len(s1.split())


# In[ ]:


# 2. Series Generations 1, 3, 9, 27, 81, ...
a = int(input("enter the end of series"))
s = 1
i = 1
while(s <= a):
    print(s,end=" ")
    s =s*3


# In[ ]:


# 3. Series Generations:-  1, 2, 4, 8, 16, 32, 64, 128, 256, ...
n = int(input("enter the end of series"))
sum = 1
i = 1
while(sum <= n):
    print(sum,end=" ")
    sum =sum * 2


# In[ ]:


# 4. Series Generations:-  1 3 8 15 27 50 92 169 311
n = int(input("enter the end of series"))
s=0
a=1
b=3
c=4
print(a,b,end=" ")
while(s <= n):
    s = a+b+c
    print(s,end=" ")
    a = b
    b = c
    c = s


# In[ ]:


# 5. Series Generations:-  2 15 41 80 132 197 275 366 470 587
n = int(input("enter the end of series"))
s=0
a=2
i=1
b=0
print(a,end=" ")
while(s <= n):
    b =(13*i)
    s = a + b
    print(s,end=" ")
    a = s
    i=i+1


# In[7]:


# 6. Series Generations:-  1,9,17, 33,49,73,97
n = int(input("enter the end of series"))
s=0
a=1
i=1
b=0
print(a,end=" ")
while(s <= n):
    d=0
    while(d <= 2):
        b =(8*i)
        s = a + b
        print(s,end=" ")
        a = s
        d = d+1
    i = i + 2


# In[4]:


def digits(n):
    li =[]
    while(n>0):
        li.append(n%10)
        n=n//10
    li.reverse()
    return(li)
li=digits(41325)
for i in li:
    print("*"*i)
    


# In[6]:


import math
math.floor(123.45)


# In[ ]:


import random
def rando(n,lb,ub):
    for i in range(0,n):
        print(r)


# In[ ]:


random.

