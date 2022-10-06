#!/usr/bin/env python
# coding: utf-8

# # Multiple Subplots
# 
# Simple Line Plot,
# Multiple Subplots dengan OO Style,
# Multiple Subplots dengan pyplotes Style

# # Import Modules

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.__version__)
print(np.__version__)


# # Simple Line Plot

# In[4]:


x = np.arange(0.0, 2.0, 0.01)
x


# In[5]:


s = np.sin(2 * np.pi * x)
s


# In[11]:


fig, ax = plt.subplots() ## OO Style

ax.plot(x,s)
ax.set(xlabel='nilai x',
      ylabel='nilai sin(x)',
      title='Visualisasi nilai sin')
ax.grid()

plt.show()


# In[19]:


fig, ax = plt.subplots() ## OO Style

ax.plot(x,s)
ax.set(xlabel='nilai x',
      ylabel='nilai sin(x)',
      title='Visualisasi nilai sin')
##ax.grid()

plt.show()


# # Multiple Sublpot

# In[8]:


x1 = np.linspace(0.0, 5.0, 100)
x2 = np.linspace(0.0, 2.0, 100)

y1 = np.cos(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)


# In[9]:


x1


# In[ ]:


Multiple Subplot dengan OO Style


# In[18]:


fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Multiple Subplots')

ax1.plot(x1, y1, 'ro-')
ax1.set_ylabel('Nilai cos(x1)')

ax2.plot(x2, y2, 'g.-')
ax2.set_ylabel('Nilai cos(x2)')

ax2.set_xlabel('Nilai x')

plt.show()


# In[25]:


fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Multiple Subplots')

ax1.plot(x1, y1, 'ro-')
ax1.set_ylabel('Nilai $cos(x1)$')

ax2.plot(x2, y2, 'g.-')
ax2.set_ylabel('Nilai cos(x2)')

ax2.set_xlabel('Nilai x')

plt.show()


# In[ ]:





# In[23]:


fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Multiple Subplots')

ax1.plot(x1, y1, 'ro-')
ax1.set_ylabel('Nilai $cos(x1)$')

ax2.plot(x2, y2, 'g.-')
ax2.set_ylabel('Nilai $cos(x2)$')

ax2.set_xlabel('Nilai x')

plt.show()


# In[24]:


fig, (ax1, ax2) = plt.subplots(2, 1)
fig.suptitle('Multiple Subplots')

ax1.plot(x1, y1, 'ro-')
ax1.set_ylabel('Nilai $cos(x1)$')

ax2.plot(x2, y2, 'g.-')
ax2.set_ylabel('Nilai $cos(x2)$')

ax2.set_xlabel('Nilai $x$')

plt.show()

