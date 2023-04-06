#!/usr/bin/env python
# coding: utf-8

# In[8]:


def factorial(a):
    if a == 0:
        return 1
    else:
        return a * factorial(a-1)

    
    
    
def main():
    for i in range(0, 15, 2):
        print("factorial of", i, " =", factorial(i))

        
        
        
if __name__ == "__main__":
    main()


# In[ ]:




