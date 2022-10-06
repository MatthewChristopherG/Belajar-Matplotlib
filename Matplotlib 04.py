#!/usr/bin/env python
# coding: utf-8

# # Histogram
# Dalam sesi ini kita akan belajar cara membuat histogram dengan Matplotlib

# # Import Modules

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)


# # Sample Data

# In[9]:


mu, sigma = 100, 15 # nilai mean dan nilai standart Deviation

x = mu + sigma * np.random.randn(10000) # normal distribution
x


# In[10]:


x.shape


# # Histogram dengan pyplot Style

# In[18]:


plt.hist(x,
        bins=25,
        facecolor='b',
         alpha=0.50)

plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Contoh Histogram')

plt.text(45, 500, r'$\mu=100,\ \sigma=15$')
plt.grid()

plt.show()


# In[17]:


plt.hist(x,
        bins=100,
        facecolor='y',
         alpha=0.25)

plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Contoh Histogram')

plt.text(45, 500, r'$\mu=100,\ \sigma=15$')
plt.grid()

plt.show()


# In[14]:


plt.hist(x,
        bins=50,
        facecolor='g',
         alpha=0.75)

plt.xlabel('Sumbu X')
plt.ylabel('Sumbu Y')
plt.title('Contoh Histogram')

plt.text(45, 500, r'$\mu=100,\ \sigma=15$')
plt.grid()

plt.show()


# nilai alpha 0.75 -> 75%
# nilai alpha 0.50 -> 50%
# nilai alpha 0.25 -> 25%

# In[ ]:


Histogram dengan OO Style


# In[22]:


fig, ax = plt.subplots()

ax.hist(x,
       bins=50,
       facecolor='r',
       alpha=0.75)

ax.set_xlabel('Sumbu X')
ax.set_ylabel('Sumbu Y')
ax.set_title('Contoh Histogram')

ax.text(45, 500, r'$\mu=100,\ \sigma=15$')
ax.grid()

plt.show()


# In[23]:


fig, ax = plt.subplots()

ax.hist(x,
       bins=50,
       facecolor='b',
       alpha=0.25)

ax.set_xlabel('Sumbu X')
ax.set_ylabel('Sumbu Y')
ax.set_title('Contoh Histogram')

ax.text(45, 500, r'$\mu=100,\ \sigma=15$')
ax.grid()

plt.show()

