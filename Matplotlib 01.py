#!/usr/bin/env python
# coding: utf-8

# # Pengenalan Matplotlib
# 
# Matplotlib adalah salah satu module dalam Pemrograman Python yang dapat digunakan untuk memvisualisasikan data dalam bentuk graphs.
#  
# Dengan Matplotlib, graphsakan digambarkan pada suatu figure yang di dalamnya dapat terdiri dari satu atau lebih axes. 
# 

# Import modules

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np


# Membuat plotting sederhana
# 
# Membuat sebuah figure yang memiliki sebuah axes; melakukkan plotting data pada axes

# In[6]:


import matplotlib.pyplot as plt
import numpy as np

# persiapan sample data
x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

fig, ax = plt.subplots() #membuat sebuah figure dan sebuah axes
ax.plot(x,y) #melakukan plotting data pada axes


# Alternatif lain, kita bisa langsung memanfaatkan method plot() pada pyplot untuk melakukan plotting sederhana.

# In[7]:


import matplotlib.pyplot as plt
import numpy as np

# persiapan sample data
x = [1, 2, 3, 4]
y = [1, 4, 2, 3]

plt.plot(x, y)


# Figure merupakan media dasar/container dasar untuk melakukan visualisasi data dengan menggunakan matplotlib.
# Didalam 1 figure kita bisa memiliki beberapa axes.
# Axes merupakan area gambarnya, dan axes itu akan selalu berada dalam suatu figure.
# Sebuah figure bisa memiliki lebih dari satu axes.
# Axis mengindikasikan sumbu (x dan y).

# Berikut adalah beberapa cara untuk membuat figure dan axes:

# In[8]:


fig = plt.figure() #figure tanpa axes


# In[9]:


fig, ax = plt.subplots() #sebuah figure  dengan sebuah axes


# In[10]:


fig, axs = plt.subplots(2, 3) #sebuah figure dengan 2x3 grid axes


# Dua cara dalam menggunakan Matplotlib
# 
# Pada dasarnya terdapat dua cara dalam menggunakan Matplotlib, yaitu:
#     
#     OO Style (Object Oriented Style)
#     pyplot Style

# Mengenal eksplisit membuat figures beserta axes dan memanggil methods dari keduanya.

# In[11]:


x = np.linspace(0, 2, 100)
x


# In[12]:


fig, ax = plt.subplots() #membuat sebuah figure dan sebuah axes.

#plotting  tiga variant data pada axes
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x, label='cubic')

ax.set_xlabel('x label') #menyertakan  x-label pada axes
ax.set_ylabel('y label') #menyertakan  y-label pada axes
ax.set_title("Simple Plot") #menyertakan  title pada axes
ax.legend() # menyertakan legend


# In[13]:


fig, ax = plt.subplots() #membuat sebuah figure dan sebuah axes.

#plotting  tiga variant data pada axes
ax.plot(x, x, label='linear')
ax.plot(x, x**2, label='quadratic')
ax.plot(x, x, label='cubic')

ax.set_xlabel('sumbu x') #menyertakan  x-label pada axes
ax.set_ylabel('y label') #menyertakan  y-label pada axes
ax.set_title("Simple Plot") #menyertakan  title pada axes
ax.legend() # menyertakan legend


# Mengenal pyplot Style untuk melakukan plotting
# 
# Mengandalkan pyplot untuk membuat dan mengelola figures dan axes, serta
# menggunakan fungsi pada pyplot untuk melakukan plotting.

# In[14]:


x = np.linspace(0, 2, 100)
x


# In[18]:


#plotting  tiga variant data pada axes
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x, label='cubic')

plt.xlabel('x label') #menyertakan  x-label pada axes
plt.ylabel('y label') #menyertakan  y-label pada axes
plt.title("Simple Plot") #menyertakan  title pada axes
plt.legend() # menyertakan legend

