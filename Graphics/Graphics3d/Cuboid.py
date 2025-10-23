#!/usr/bin/env python
# coding: utf-8

# In[2]:


#cuboid.py
def area_cub(l,b,h):
    print("Area of cuboid:",2*((l*b)+(l*h)+(b*h)))
def peri_cub(l,b,h):
    print("Perimeter of the cuboid:",4*(l+b+h))


# In[3]:


get_ipython().system('jupyter nbconvert --to python cuboid.ipynb')


# In[ ]:




