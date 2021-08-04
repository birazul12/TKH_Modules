#!/usr/bin/env python
# coding: utf-8

#  # Module-5 Hands on exercise
#  ## MD ISLAM

# In[8]:


print ("Hello TKH")


# In[14]:


input()


# In[15]:


a = 5
if a == 5:
    print("a equal 5")


# In[16]:


myString = 'hello world'
print(type(myString))


# In[17]:


n =10
print(type(n))


# In[18]:


n_float = 7.5
print(type(n_float))


# In[20]:


single_string = 'It's a single quote string'
print(single_string)


# In[21]:


single_string = 'Its a single quote string' #the correct one of the previous code
print(single_string)


# In[22]:


double_string = "It's a double quote string"
print(double_string)


# In[23]:


n1 = 5
n2 = 7.5
print(n1+n2)


# In[32]:


nstr1 = "abc"
print(nstr1 + n1)


# In[25]:


nstr2 = "def"
print(nstr1 + nstr2)


# In[26]:


n1, n2 = 10, 11


# In[27]:


n1


# In[28]:


n2


# In[29]:


result = 3 + 4.0 / 2 * 5  # DMAS
print(result)


# In[30]:


# module operator %
remainder = 17%10
print(remainder)


# In[31]:


# x ^ n
x = 5
n = 4
print(x ** n)


# In[34]:


nstr = "abc"
ans = nstr * 10


# In[35]:


print(len(ans))


# In[36]:


name = "Harshit"
print("%s is a data scientist!" %name)


# In[37]:


name.upper()


# In[38]:


name.lower()


# In[39]:


nstr = "it is a nice day today."
nstr.capitalize()


# In[40]:


name.index('s')


# In[41]:


name[2:5]


# In[42]:


alist = [3,4,5]
print(alist)


# In[43]:


alist = ['harshit', 2, 5.5]
print(alist)


# In[44]:


alist.append(10)
alist.append(15)
print(alist)


# In[45]:


alist.pop()
print(alist)


# In[46]:


alist[3]


# In[47]:


alist[1:]


# In[48]:


alist.append([1,2,3])
print(alist)


# In[49]:


alist*2


# In[50]:


alist + alist

