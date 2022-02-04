#!/usr/bin/env python
# coding: utf-8

# In[1]:


def listDivide(numbers, divide = 2):
    divisibleCount = 0
    for everyNum in numbers:
        if everyNum % divide == 0:
            divisibleCount += 1
  
    return divisibleCount

class ListDivideException(Exception):
    pass

def testListDivide():
    try:
        if not listDivide([1,2,3,4,5]) == 2:
            raise ListDivideException
        if not listDivide([2,4,6,8,10]) == 5:
            raise ListDivideException
        if not listDivide([30,54,63,98,100], divide = 10) == 2:
            raise ListDivideException
        if not listDivide([]) == 0:
            raise ListDivideException
        if not listDivide([1,2,3,4,5],1) == 5:
            raise ListDivideException
        
    except ListDivideException:
        print("Division exception occured")

testListDivide()


# In[2]:


print (testListDivide())


# In[ ]:




